import os
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
    "什么是redis? 简洁回答, 字数控制在100以内",
    "Python的生成器是做什么的? 简洁回答, 字数控制在100以内",
    "解释一下Docker和Kubernetes的关系? 简洁回答, 字数控制在100以内"
]

# 批量调用模型
response = model.batch(messages)

# 遍历结果并格式化输出
for q, r in zip(messages, response):
    print(f"问题: {q}\n回答: {r.content}\n")