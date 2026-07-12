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
messages = [
    SystemMessage(content="你叫小问，是一个乐于助人的AI人工助手"),
    HumanMessage(content="你是谁")
]

# 异步流式调用模型
async def async_stream_call():
    # astream 返回异步生成器，无需 await 修饰
    response = model.astream(messages)

    # 异步遍历异步生成器，必须使用 async for
    async for chunk in response:
        print(chunk.content, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(async_stream_call())


