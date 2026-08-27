"""Streamlit front end for the Literary Companion chatbot."""

import streamlit as st

from chatbot import HELP_TEXT, LiteraryChatbot
from knowledge_base import BOOKS, POEMS

st.set_page_config(page_title="Literary Companion", page_icon="📚", layout="centered")


@st.cache_resource
def load_bot() -> LiteraryChatbot:
    """Build the TF-IDF index once and reuse it across reruns."""
    return LiteraryChatbot()


bot = load_bot()

st.title("📚 Literary Companion")
st.caption("A chatbot for books, novels and poems.")

with st.sidebar:
    st.header("About")
    st.write(
        f"Retrieval-based chatbot over a curated library of **{len(BOOKS)} books** "
        f"and **{len(POEMS)} poems**, plus literary concepts."
    )
    st.write("**How it works**")
    st.markdown(
        "1. Intent rules catch greetings, recommendations and quote requests.\n"
        "2. Everything else goes to a TF-IDF + cosine-similarity retriever.\n"
        "3. Low-confidence matches are refused rather than guessed."
    )
    show_debug = st.checkbox("Show match source and score", value=False)
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello. I'm your literary companion.\n\n" + HELP_TEXT,
        }
    ]

# Quick-start buttons for the first turn only, so the demo is one click away.
if len(st.session_state.messages) == 1:
    st.write("**Try one of these:**")
    samples = [
        "Who wrote 1984?",
        "Recommend a fantasy novel",
        "Show me the poem Ozymandias",
        "What is a sonnet?",
    ]
    columns = st.columns(len(samples))
    for column, sample in zip(columns, samples):
        if column.button(sample, use_container_width=True):
            st.session_state.pending = sample

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about a book, a novel or a poem...")
if not prompt and st.session_state.get("pending"):
    prompt = st.session_state.pop("pending")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = bot.respond(prompt)
    answer = reply["answer"]
    if show_debug:
        answer += f"\n\n---\n*Source: {reply['source']} - match score {reply['score']:.2f}*"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
