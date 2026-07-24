from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Input text
text = "I love learning Artificial Intelligence."

# Perform sentiment analysis
result = classifier(text)

# Display the output
print("Input Text:")
print(text)

print("\nSentiment Analysis Result:")
print(result)
