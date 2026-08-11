from sentence_transformers import SentenceTransformer
import torch

# Load a pre-trained sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Two sentences to compare
sentence1 = "I love programming in Python."
sentence2 = "Python is my favorite programming language."

# Generate embeddings
embedding1 = model.encode(sentence1, convert_to_tensor=True)
embedding2 = model.encode(sentence2, convert_to_tensor=True)

# Calculate cosine similarity
similarity = torch.nn.functional.cosine_similarity(
    embedding1.unsqueeze(0),
    embedding2.unsqueeze(0)
)

# Display results
print("Sentence 1:")
print(sentence1)

print("\nSentence 2:")
print(sentence2)

print("\nEmbedding Dimension:")
print(embedding1.shape)

print("\nCosine Similarity:")
print(similarity.item())