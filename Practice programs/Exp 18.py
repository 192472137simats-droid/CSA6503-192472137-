from transformers import BertTokenizer, BertModel
import torch
import torch.nn.functional as F

# Load the pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Two semantically similar sentences
sentence1 = "The cat is sleeping on the mat."
sentence2 = "A cat is resting on the mat."

# Tokenize the sentences
inputs1 = tokenizer(sentence1, return_tensors="pt")
inputs2 = tokenizer(sentence2, return_tensors="pt")

# Generate contextual embeddings
with torch.no_grad():
    outputs1 = model(**inputs1)
    outputs2 = model(**inputs2)

# Mean pooling to get sentence embeddings
embedding1 = outputs1.last_hidden_state.mean(dim=1)
embedding2 = outputs2.last_hidden_state.mean(dim=1)

# Compute cosine similarity
similarity = F.cosine_similarity(embedding1, embedding2)

# Display the results
print("Sentence 1:")
print(sentence1)

print("\nSentence 2:")
print(sentence2)

print("\nCosine Similarity:")
print(similarity.item())
