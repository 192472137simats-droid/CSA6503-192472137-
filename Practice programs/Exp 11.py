from transformers import BertTokenizer

# Load the pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input sentence
sentence = "Machine Learning is transforming the world."

# Tokenize the sentence
tokens = tokenizer.tokenize(sentence)

# Display the results
print("Original Sentence:")
print(sentence)

print("\nTokens:")
print(tokens)
