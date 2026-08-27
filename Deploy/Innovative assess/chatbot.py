"""Literary Companion - the chatbot engine.

The bot answers questions about books, novels and poems using two layers:

1. A small rule/intent layer for greetings, recommendations and quote requests.
2. A TF-IDF + cosine-similarity retriever over the knowledge base, which is the
   fallback for everything else. If the best match scores below a confidence
   threshold the bot says so instead of inventing an answer.
"""

from __future__ import annotations

import random
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge_base import BOOKS, FAQS, GENRE_ALIASES, POEMS

# Below this cosine score the retriever is not trusted to have found anything.
CONFIDENCE_THRESHOLD = 0.12

GREETINGS = ("hi", "hello", "hey", "namaste", "good morning", "good evening", "yo")
FAREWELLS = ("bye", "goodbye", "see you", "exit", "quit", "good night")
THANKS = ("thanks", "thank you", "thx", "appreciate it")

# Questions asking for a general literary concept rather than a specific work.
DEFINITION_PATTERN = re.compile(
    r"^(what is|what are|what does|whats|define|explain|meaning of|difference between)\b"
)

HELP_TEXT = (
    "I'm a literary companion. Things you can ask me:\n\n"
    "- *Who wrote 1984?*\n"
    "- *Tell me about The Great Gatsby*\n"
    "- *Recommend a fantasy novel*\n"
    "- *Quote from The Alchemist*\n"
    "- *Show me the poem Ozymandias*\n"
    "- *What is a sonnet?* / *What is magical realism?*"
)


def _normalise(text: str) -> str:
    """Lowercase and strip punctuation so matching is forgiving."""
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).strip()


def _starts_with_any(text: str, options) -> bool:
    return any(text == opt or text.startswith(opt + " ") for opt in options)


class LiteraryChatbot:
    """Retrieval-based chatbot over a curated literary knowledge base."""

    def __init__(self) -> None:
        self.documents: list[str] = []
        self.payloads: list[dict] = []
        self.kinds: list[str] = []  # "book" | "poem" | "faq", used to scope searches
        self._index_knowledge_base()

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            sublinear_tf=True,
        )
        self.doc_matrix = self.vectorizer.fit_transform(self.documents)

    # -- indexing ----------------------------------------------------------

    def _add(self, text: str, answer: str, source: str, kind: str) -> None:
        self.documents.append(text)
        self.payloads.append({"answer": answer, "source": source})
        self.kinds.append(kind)

    def _index_knowledge_base(self) -> None:
        for book in BOOKS:
            searchable = " ".join(
                [
                    book["title"],
                    book["author"],
                    " ".join(book["genre"]),
                    book["summary"],
                    book["famous_line"],
                    f"who wrote {book['title']} summary of {book['title']} "
                    f"about {book['title']} plot theme novel book",
                ]
            )
            answer = (
                f"**{book['title']}** - {book['author']} ({book['year']})\n\n"
                f"{book['summary']}\n\n"
                f"*Genre:* {', '.join(book['genre'])}\n\n"
                f"> {book['famous_line']}"
            )
            self._add(searchable, answer, f"Book: {book['title']}", "book")

        for poem in POEMS:
            # Title and poet are repeated so name-led queries outrank prose matches.
            searchable = " ".join(
                [
                    poem["title"],
                    poem["title"],
                    poem["poet"],
                    poem["poet"],
                    "poem poetry verse",
                    poem["form"],
                    poem["theme"],
                    poem["extract"],
                    f"poem verse poetry lines of {poem['title']} "
                    f"who wrote {poem['title']} meaning of {poem['title']}",
                ]
            )
            answer = (
                f"**{poem['title']}** - {poem['poet']} ({poem['year']})\n\n"
                f"*Form:* {poem['form']}\n\n"
                f"*Theme:* {poem['theme']}\n\n"
                "```\n" + poem["extract"] + "\n```"
            )
            self._add(searchable, answer, f"Poem: {poem['title']}", "poem")

        for faq in FAQS:
            self._add(
                faq["question"] + " " + faq["question"] + " " + faq["answer"],
                faq["answer"],
                "Literary concepts",
                "faq",
            )

        # Titles and creator names, used to tell "what is a sonnet?" apart from
        # "what is the theme of Ozymandias?". Very short names are skipped
        # because they collide with ordinary words.
        self.known_names = {
            _normalise(name)
            for name in (
                [b["title"] for b in BOOKS]
                + [b["author"] for b in BOOKS]
                + [p["title"] for p in POEMS]
                + [p["poet"] for p in POEMS]
            )
            if len(_normalise(name)) >= 4
        }

    # -- intent handlers ---------------------------------------------------

    def _recommend(self, text: str) -> dict | None:
        """Handle 'recommend / suggest a <genre> book' style requests."""
        if not any(w in text for w in ("recommend", "suggest", "what should i read")):
            return None

        matched_genre = None
        for genre, aliases in GENRE_ALIASES.items():
            if any(alias in text for alias in aliases):
                matched_genre = genre
                break

        pool = [b for b in BOOKS if matched_genre in b["genre"]] if matched_genre else BOOKS
        if not pool:
            pool = BOOKS

        picks = random.sample(pool, min(3, len(pool)))
        label = f"{matched_genre} " if matched_genre else ""
        lines = [f"Here are some {label}reads worth your time:\n"]
        for book in picks:
            lines.append(f"- **{book['title']}** by {book['author']} - {book['summary']}")
        return {
            "answer": "\n".join(lines),
            "source": f"Recommendation ({matched_genre or 'any genre'})",
            "score": 1.0,
        }

    def _quote(self, text: str) -> dict | None:
        """Handle requests for a famous line or quote."""
        if not any(w in text for w in ("quote", "famous line", "famous quote")):
            return None

        for book in BOOKS:
            if _normalise(book["title"]) in text:
                return {
                    "answer": f"From **{book['title']}** by {book['author']}:\n\n"
                    f"> {book['famous_line']}",
                    "source": f"Book: {book['title']}",
                    "score": 1.0,
                }

        book = random.choice(BOOKS)
        return {
            "answer": f"From **{book['title']}** by {book['author']}:\n\n"
            f"> {book['famous_line']}",
            "source": f"Book: {book['title']}",
            "score": 1.0,
        }

    def _smalltalk(self, text: str) -> dict | None:
        if _starts_with_any(text, GREETINGS):
            return {
                "answer": "Hello. I talk about books, novels and poems - ask me for a "
                "summary, an author, a recommendation or a poem.",
                "source": "Greeting",
                "score": 1.0,
            }
        if _starts_with_any(text, FAREWELLS):
            return {
                "answer": "Goodbye, and happy reading.",
                "source": "Farewell",
                "score": 1.0,
            }
        if any(t in text for t in THANKS):
            return {
                "answer": "Glad to help. Anything else from the shelf?",
                "source": "Acknowledgement",
                "score": 1.0,
            }
        if "help" in text or "what can you do" in text:
            return {"answer": HELP_TEXT, "source": "Help", "score": 1.0}
        return None

    # -- retrieval ---------------------------------------------------------

    def _names_a_work(self, text: str) -> bool:
        """True if the query mentions a title or author/poet we hold."""
        padded = f" {text} "
        return any(f" {name} " in padded for name in self.known_names)

    def _retrieve(self, message: str, kinds: set[str] | None = None) -> dict:
        """Best match for a message, optionally scoped to certain entry kinds."""
        query_vector = self.vectorizer.transform([message])
        scores = cosine_similarity(query_vector, self.doc_matrix)[0]

        if kinds:
            scores = scores.copy()
            for i, kind in enumerate(self.kinds):
                if kind not in kinds:
                    scores[i] = 0.0

        best = int(scores.argmax())

        if scores[best] < CONFIDENCE_THRESHOLD:
            return {
                "answer": (
                    "I don't have that one in my library yet. I know about "
                    f"{len(BOOKS)} books and {len(POEMS)} poems - try asking about a "
                    "title, an author, a genre recommendation, or a term like "
                    "*sonnet* or *magical realism*."
                ),
                "source": "No confident match",
                "score": float(scores[best]),
            }

        payload = self.payloads[best]
        return {
            "answer": payload["answer"],
            "source": payload["source"],
            "score": float(scores[best]),
        }

    # -- public API --------------------------------------------------------

    def respond(self, message: str) -> dict:
        """Return {'answer', 'source', 'score'} for a user message."""
        if not message or not message.strip():
            return {
                "answer": "Ask me something about a book, a novel or a poem.",
                "source": "Empty input",
                "score": 0.0,
            }

        text = _normalise(message)
        for handler in (self._smalltalk, self._recommend, self._quote):
            result = handler(text)
            if result:
                return result

        # A definitional question that names no specific work ("what is a sonnet?")
        # should get the concept explanation, not a work that happens to share words.
        if DEFINITION_PATTERN.match(text) and not self._names_a_work(text):
            concept = self._retrieve(message, kinds={"faq"})
            if concept["score"] >= CONFIDENCE_THRESHOLD:
                return concept

        return self._retrieve(message)


if __name__ == "__main__":  # simple console mode for quick testing
    bot = LiteraryChatbot()
    print("Literary Companion - type 'quit' to leave.\n")
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            break
        if _normalise(user) in ("quit", "exit", "bye"):
            print("Bot: Goodbye, and happy reading.")
            break
        reply = bot.respond(user)
        print(f"Bot: {reply['answer']}\n     [{reply['source']} | {reply['score']:.2f}]\n")
