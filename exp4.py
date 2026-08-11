from langchain_core.documents import Document
from langchain_chroma import Chroma
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# -----------------------------
# 1. Domain-specific knowledge
# -----------------------------

documents = [
    Document(
        page_content="Artificial Intelligence is the simulation of human intelligence by machines."
    ),
    Document(
        page_content="Machine Learning is a branch of AI that allows computers to learn patterns from data."
    ),
    Document(
        page_content="Deep Learning uses artificial neural networks with multiple layers."
    ),
    Document(
        page_content="Natural Language Processing allows computers to understand and process human language."
    ),
    Document(
        page_content="Computer Vision enables computers to understand and analyze images and videos."
    ),
    Document(
        page_content="Generative AI can create new content such as text, images, audio and code."
    ),
]


# -----------------------------
# 2. Lightweight embeddings
# -----------------------------

class TfidfEmbeddings:

    def __init__(self, documents):
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(
            [doc.page_content for doc in documents]
        )

    def embed_documents(self, texts):
        vectors = self.vectorizer.transform(texts)
        return vectors.toarray().tolist()

    def embed_query(self, text):
        vector = self.vectorizer.transform([text])
        return vector.toarray()[0].tolist()


embeddings = TfidfEmbeddings(documents)


# -----------------------------
# 3. Create ChromaDB
# -----------------------------

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="ai_chatbot"
)

print("AI Domain-Specific Chatbot")
print("Knowledge base: Artificial Intelligence")
print("Type 'exit' to stop.")


# -----------------------------
# 4. Chatbot
# -----------------------------

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    results = vector_db.similarity_search(
        question,
        k=2
    )

    print("\nChatbot:")

    if results:
        for result in results:
            print("-", result.page_content)

    else:
        print("Sorry, I don't have information about that.")