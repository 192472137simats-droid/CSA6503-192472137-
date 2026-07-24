from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Artificial Intelligence is transforming the world."

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)

# Display tokens
print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)