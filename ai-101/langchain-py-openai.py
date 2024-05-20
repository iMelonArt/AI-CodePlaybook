import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Tell me more about Paris"
)

chat_completion = client.chat.completions.create(
    model="gpt-4",
    messages="<messages>"
)

embedding = client.embeddings.create(
    model="text-embedding-ada-002",
    input="<input>"
)