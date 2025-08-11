# test_query.py
import os
from groq import Groq
from dotenv import load_dotenv

# Load the .env file where your API key is stored
load_dotenv()

# Retrieve the key from environment variable
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment or .env file.")

# Initialize the Groq client
client = Groq(api_key=api_key)

# Use a valid Groq model (pick one from Groq's docs or dashboard)
MODEL_NAME = "llama3-8b-8192"  # alternatives: "llama3-70b-8192", "mixtral-8x7b-32768", "gemma-7b-it"

# Make a simple test request
resp = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello from Groq!"}
    ],
    max_tokens=100
)

# Print the model's reply
print("Groq reply:", resp.choices[0].message.content.strip())
