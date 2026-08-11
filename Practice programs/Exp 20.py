from transformers import pipeline

# Load the pre-trained GPT-2 text generation model
generator = pipeline("text-generation", model="gpt2")

# List of prompts
prompts = [
    "Artificial Intelligence",
    "Machine Learning",
    "The future of Robotics"
]

# Generate and compare responses
for i, prompt in enumerate(prompts, start=1):
    print(f"\nPrompt {i}: {prompt}")
    print("-" * 50)

    result = generator(
        prompt,
        max_length=60,
        num_return_sequences=1,
        truncation=True
    )

    print(result[0]["generated_text"])
