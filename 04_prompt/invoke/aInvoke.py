import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage


# 读取环境变量
load_dotenv()

# 实例化模型
model = init_chat_model(
    model="deepseek-v4-flash",
    model_provider="openai",
    api_key=os.getenv("deepseek-api"),
    base_url="https://api.deepseek.com"
)

# 消息列表
messages = "解释一下LangChain是什么，简洁回答100字以内"

async def main():
    # 异步调用模型
    response = await model.ainvoke(messages)

    # 打印结果
    print(response.content)

if __name__ == "__main__":
    asyncio.run(main())