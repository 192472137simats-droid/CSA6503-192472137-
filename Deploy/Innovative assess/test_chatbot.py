"""Minimal behaviour tests for the Literary Companion chatbot.

Run with:  python test_chatbot.py     (or)     pytest test_chatbot.py
"""

from chatbot import CONFIDENCE_THRESHOLD, LiteraryChatbot

bot = LiteraryChatbot()


def test_greeting_is_handled_by_intent_layer():
    assert bot.respond("hi")["source"] == "Greeting"


def test_author_lookup():
    assert "George Orwell" in bot.respond("Who wrote 1984?")["answer"]


def test_book_summary():
    reply = bot.respond("Tell me about The Great Gatsby")
    assert reply["source"] == "Book: The Great Gatsby"


def test_poem_lookup():
    reply = bot.respond("Show me the poem Ozymandias")
    assert "Shelley" in reply["answer"]


def test_genre_recommendation():
    reply = bot.respond("Recommend a fantasy novel")
    assert reply["source"] == "Recommendation (fantasy)"


def test_quote_request():
    reply = bot.respond("quote from The Alchemist")
    assert "conspires" in reply["answer"]


def test_definition_beats_similarly_named_work():
    # "What is a sonnet?" must explain the form, not return Sonnet 18.
    assert bot.respond("What is a sonnet?")["source"] == "Literary concepts"


def test_off_topic_question_is_refused():
    reply = bot.respond("how do I fix my car engine")
    assert reply["score"] < CONFIDENCE_THRESHOLD
    assert "library" in reply["answer"]


def test_empty_input():
    assert bot.respond("   ")["source"] == "Empty input"


if __name__ == "__main__":
    passed = 0
    for name, func in sorted(globals().items()):
        if name.startswith("test_") and callable(func):
            func()
            print(f"PASS  {name}")
            passed += 1
    print(f"\n{passed} tests passed.")
