from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import torch

# Load the Question Answering model and tokenizer
model_name = "distilbert/distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Context paragraph
context = """
Python is a high-level programming language created by Guido van Rossum.
It is widely used for web development, artificial intelligence,
data science, automation, and machine learning.
"""

# Question
question = "Who created Python?"

# Tokenize inputs
inputs = tokenizer(question, context, return_tensors="pt")

# Perform Question Answering
with torch.no_grad():
    outputs = model(**inputs)

# Get the answer span
answer_start = torch.argmax(outputs.start_logits)
answer_end = torch.argmax(outputs.end_logits) + 1
answer_tokens = inputs["input_ids"][0][answer_start:answer_end]
answer = tokenizer.decode(answer_tokens)
score = (torch.max(outputs.start_logits) + torch.max(outputs.end_logits)).item()

# Display the results
print("Context:")
print(context)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)

print("Confidence Score:")
print(score)
