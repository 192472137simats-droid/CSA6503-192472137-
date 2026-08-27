# 📚 Literary Companion — AI Chatbot for Books, Novels & Poems

A simple conversational assistant that answers questions about literature: book
summaries, authors, genre recommendations, famous quotes, poems and literary
concepts.

Built as an assessment project. Streamlit front end, scikit-learn retrieval
back end, deployed on Railway.

---

## What it does

| Ask it | It replies with |
|---|---|
| *Who wrote 1984?* | Author, year, summary and a famous line |
| *Tell me about The Great Gatsby* | Full book card with genre and quote |
| *Recommend a fantasy novel* | Three curated picks from that genre |
| *Quote from The Alchemist* | The book's best-known line |
| *Show me the poem Ozymandias* | Poet, form, theme and an extract |
| *What is a sonnet?* | A plain-English explanation of the form |
| *How do I fix my car engine?* | An honest "that's outside my library" |

## How it works

```
user message
     |
     |--> intent rules ------> greeting / farewell / thanks / help
     |                         genre recommendation
     |                         quote request
     |
     |--> definition check --> concept questions answered from the FAQ set
     |                         ("what is a sonnet?" is not Sonnet 18)
     |
     `--> TF-IDF retriever --> cosine similarity over books + poems + concepts
                               score < 0.12  ->  refuse instead of guessing
```

1. **Intent layer** (`chatbot.py`) — regex and keyword rules catch small talk,
   recommendations and quote requests, which don't need retrieval.
2. **Retrieval layer** — every knowledge-base entry is turned into a searchable
   document and vectorised with `TfidfVectorizer` (unigrams + bigrams, English
   stop words, sublinear term frequency). An incoming message is vectorised the
   same way and matched by cosine similarity.
3. **Confidence threshold** — if the best cosine score is below `0.12`, the bot
   says it doesn't know rather than returning a bad match. This is the main
   guard against confident nonsense.

The knowledge base (`knowledge_base.py`) holds **18 books**, **10 poems** and
**14 literary concepts** as plain Python data — no database, no API keys, no
model downloads, so the app starts in about a second.

## Project structure

```
Innovative assess/
├── app.py               Streamlit chat UI
├── chatbot.py           Chatbot engine (intents + TF-IDF retrieval)
├── knowledge_base.py    Books, poems and literary concepts
├── test_chatbot.py      Behaviour tests
├── requirements.txt     Dependencies
├── Procfile             Start command for deployment
└── README.md
```

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501

Console-only mode, without the UI:

```bash
python chatbot.py
```

## Run the tests

```bash
python test_chatbot.py     # no pytest needed
# or
pytest test_chatbot.py
```

## Deployment

Deployed on **Railway**, which builds the app with Nixpacks from
`requirements.txt` and starts it using the `Procfile`:

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

Binding to `0.0.0.0` and reading `$PORT` from the environment is what lets the
platform route traffic to the container. The same repository deploys unchanged
to Streamlit Community Cloud, Render or Hugging Face Spaces.

## Tech stack

- **Python 3.10**
- **Streamlit** — chat interface
- **scikit-learn** — TF-IDF vectorisation and cosine similarity
- **Railway** — hosting

## Possible extensions

- Swap TF-IDF for sentence-transformer embeddings for better paraphrase handling
- Persist conversations and log unanswered questions to grow the knowledge base
- Add a generative fallback so unknown queries get a composed answer
