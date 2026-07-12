from langchain_ollama import ChatOllama


model = ChatOllama(
    model="qwen3.5:latest",
    base_url="http://localhost:11434",
    reasoning=False
)

messages = "什么是LangChain，100字以内回答"

response = model.invoke(messages)

print(response.content)