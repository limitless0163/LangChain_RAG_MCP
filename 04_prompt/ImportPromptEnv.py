from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate

from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate
from langchain_core.prompts import AIMessagePromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate

from langchain.messages import SystemMessage
from langchain.messages import HumanMessage
from langchain.messages import AIMessage
from langchain.messages import ToolMessage


messages = [
    SystemMessage(content="你是一位乐于助人的智能小助手"),
    HumanMessage(content="你好，请你介绍一下你自己"),
    AIMessage(content="我是一名人工智能助手，请问您有什么想问的嘛?"),
    ToolMessage(tool_call_id="call_abc123", content='{"population": 21540000, "area": "16410平方公里"}',)
]

print(messages)