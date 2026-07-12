import os
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello, 你是谁"},
]

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=messages,
    stream=False
)

print(response.choices[0].message.content)