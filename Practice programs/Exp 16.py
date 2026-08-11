from transformers import BertTokenizer, GPT2Tokenizer

# Load the pre-trained tokenizers
bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Input sentence
sentence = "Artificial Intelligence is transforming the world."

# Tokenize using BERT
bert_tokens = bert_tokenizer.tokenize(sentence)

# Tokenize using GPT-2
gpt2_tokens = gpt2_tokenizer.tokenize(sentence)

# Display the results
print("Original Sentence:")
print(sentence)

print("\nBERT Tokens:")
print(bert_tokens)

print("\nGPT-2 Tokens:")
print(gpt2_tokens)
