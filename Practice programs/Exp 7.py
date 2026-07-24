from transformers import pipeline

# Load the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Input text
text = "I love learning Artificial Intelligence."

# Perform sentiment analysis
result = classifier(text)

# Display result
print("Input Text:", text)
print("Sentiment Analysis Result:")
print(result)