import os
import re

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI


# ==========================================
# 1. Configuration
# ==========================================

PDF_PATH = "sample.pdf"

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("ERROR: OPENROUTER_API_KEY is not set.")
    print("Set it using:")
    print("set OPENROUTER_API_KEY=your_key")
    exit()


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)


# ==========================================
# 2. Load PDF
# ==========================================

if not os.path.exists(PDF_PATH):
    print("ERROR: sample.pdf not found!")
    exit()


reader = PdfReader(PDF_PATH)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"


print("PDF loaded successfully.")


# ==========================================
# 3. Split document into chunks
# ==========================================

# Split into sentences
sentences = re.split(r'(?<=[.!?])\s+', text)

sentences = [
    sentence.strip()
    for sentence in sentences
    if len(sentence.strip()) > 20
]


# Group sentences into small chunks
chunks = []

current_chunk = ""

for sentence in sentences:

    if len(current_chunk) + len(sentence) <= 800:
        current_chunk += " " + sentence

    else:
        chunks.append(current_chunk.strip())
        current_chunk = sentence


if current_chunk:
    chunks.append(current_chunk.strip())


print("Number of document chunks:", len(chunks))


# ==========================================
# 4. Create lightweight retrieval vectors
# ==========================================

vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(chunks)

print("Document vectors created.")


# ==========================================
# 5. Ask question
# ==========================================

question = input("\nEnter your question: ")


# ==========================================
# 6. Retrieve relevant information
# ==========================================

question_vector = vectorizer.transform(
    [question]
)

similarities = cosine_similarity(
    question_vector,
    document_vectors
)[0]


# Get top 3 chunks
top_indices = similarities.argsort()[-3:][::-1]

retrieved_chunks = []

for index in top_indices:

    if similarities[index] > 0:
        retrieved_chunks.append(chunks[index])


if not retrieved_chunks:

    print("\nNo relevant information found.")
    exit()


context = "\n\n".join(retrieved_chunks)

print("\nRelevant information retrieved.")


# ==========================================
# 7. RAG Prompt
# ==========================================

prompt = f"""
You are a document question-answering assistant.

Use ONLY the information in the document context
to answer the question.

Do not invent facts.

If the answer is not present in the context,
say:

"The answer is not available in the document."

DOCUMENT CONTEXT:
{context}

QUESTION:
{question}

Provide a clear and concise answer.
"""


# ==========================================
# 8. Generate answer with OpenRouter
# ==========================================

print("Generating answer...")


response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "system",
            "content": "You answer questions using the supplied document context."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2,
    max_tokens=300
)


# ==========================================
# 9. Display answer
# ==========================================

answer = response.choices[0].message.content


print("\n======================================")
print("RAG DOCUMENT QUESTION ANSWERING")
print("======================================")

print("\nQuestion:")
print(question)

print("\nGenerated Answer:")
print(answer)

print("\nRetrieved Context:")
for i, chunk in enumerate(retrieved_chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)