import os
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

completion = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="tell me more about Paris ?"
)

chat_completion = client.chat.completions.create(
    model="gpt-4",
    messages="<messages>"
)

embedding = client.embeddings.create(
    model="text-embedding-ada-002",
    input="<input>"
)

