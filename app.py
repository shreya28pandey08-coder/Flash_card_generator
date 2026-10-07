# Hugging Face Setup
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get Hugging Face token
TOKEN = os.getenv("TOKEN")

# Check whether token exists
if not TOKEN:
    raise ValueError("TOKEN was not found in the .env file.")

# Create Hugging Face client
client = InferenceClient(
    api_key=TOKEN,
    provider="auto"
)

# Hugging Face model
model = "Qwen/Qwen3-4B-Instruct-2507"


# Get flashcard details from the user
topic = input("Enter topic: ")
number = input("Number of flashcards: ")
difficulty = input("Difficulty: ")


# Create the prompt
prompt = f"""
You are an educational flashcard generator.

Create {number} flashcards about {topic}.

Difficulty: {difficulty}

For every flashcard provide:

Question:
Answer:

Rules:
- Questions must test important concepts.
- Answers must be concise.
- Avoid duplicate questions.
- Keep the content educational.
- Make the questions appropriate for the requested difficulty.
"""


# Send request to Hugging Face
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)


# Display the generated flashcards
print("\n===== AI FLASHCARDS =====\n")
print(response.choices[0].message.content)