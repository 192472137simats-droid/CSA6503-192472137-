import os
import re
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# 1. Load external document
# -----------------------------

PDF_PATH = "sample.pdf"

if not os.path.exists(PDF_PATH):
    print("sample.pdf not found!")
    exit()

reader = PdfReader(PDF_PATH)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"


# -----------------------------
# 2. Split document into sentences
# -----------------------------

sentences = re.split(r'(?<=[.!?])\s+', text)

sentences = [
    s.strip()
    for s in sentences
    if len(s.strip()) > 20
]

print("External document loaded.")
print("Number of sentences:", len(sentences))


# -----------------------------
# 3. Create TF-IDF vectors
# -----------------------------

vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(sentences)


# -----------------------------
# 4. AI Assistant
# -----------------------------

print("\nAI Assistant")
print("Ask questions about the document.")
print("Type 'exit' to stop.")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    # Convert question to vector
    question_vector = vectorizer.transform([question])

    # Calculate similarity
    similarity = cosine_similarity(
        question_vector,
        document_vectors
    )[0]

    # Get top 3 relevant sentences
    top_indices = similarity.argsort()[-3:][::-1]

    print("\nAssistant:")

    found = False

    for index in top_indices:

        if similarity[index] > 0.05:

            print("-", sentences[index])

            found = True

    if not found:
        print("I could not find relevant information in the document.")

    print("\nBest Relevance Score:",
          round(similarity[top_indices[0]], 3))