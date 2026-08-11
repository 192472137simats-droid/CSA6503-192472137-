import chromadb

# Create a ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get a collection
collection = client.get_or_create_collection(name="documents")

# Sample documents
documents = [
    "Python is a popular programming language.",
    "Machine learning allows computers to learn from data.",
    "Artificial Intelligence is used in many industries.",
    "Deep learning uses neural networks to process information."
]

# Add documents to the vector database
collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3", "doc4"]
)

print("Documents added successfully!")

# Search the vector database
query = "What is machine learning?"

results = collection.query(
    query_texts=[query],
    n_results=2
)

print("\nQuery:")
print(query)

print("\nMost Relevant Documents:")
for document in results["documents"][0]:
    print("-", document)