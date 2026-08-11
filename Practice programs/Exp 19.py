from transformers import pipeline

# Load the pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Input prompt
prompt = "The future of Artificial Intelligence"

# Generate text
result = generator(
    prompt,
    max_length=80,
    num_return_sequences=1,
    truncation=True
)

# Display the results
print("Prompt:")
print(prompt)

print("\nGenerated Text:")
print(result[0]["generated_text"])
