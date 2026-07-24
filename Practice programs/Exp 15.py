from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Deep Learning is a subset of Artificial Intelligence."

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)

# Convert tokens to token IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)

# Display the results
print("Original Sentence:")
print(sentence)

print("\nGenerated Tokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)
