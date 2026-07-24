from transformers import pipeline

# Load the pre-trained GPT-2 text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Input prompt
prompt = "Artificial Intelligence is"

# Generate text
result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1,
    truncation=True
)

# Display the output
print("Prompt:")
print(prompt)

print("\nGenerated Text:")
print(result[0]["generated_text"])
