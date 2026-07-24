from transformers import BertTokenizer, BertModel
import torch

# Load the pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Artificial Intelligence is transforming the world."

# Tokenize the sentence
inputs = tokenizer(sentence, return_tensors="pt")

# Generate contextual embeddings
with torch.no_grad():
    outputs = model(**inputs)

embeddings = outputs.last_hidden_state

# Display the embeddings
print("Input Sentence:")
print(sentence)

print("\nEmbedding Shape:")
print(embeddings.shape)

print("\nContextual Embeddings:")
print(embeddings)
