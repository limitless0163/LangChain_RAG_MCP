import time
from langchain_core.prompts import PromptTemplate
from datetime import datetime


# 方式3：部分提示词模板, 实例化过程中指定参数
template1 = PromptTemplate.from_template(
    "现在时间是：{time},请对我的问题给出答案，我的问题是：{question}",
    partial_variables={"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
)
prompt1 = template1.format(question="今天是几号？")
print(prompt1)

template2 = PromptTemplate.from_template("现在时间是：{time},请对我的问题给出答案，我的问题是：{question}")
partial = template2.partial(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
prompt2 = partial.format(question="今天是几号？")
print(prompt2)

template3 = PromptTemplate(
    template="{foo} {bar}",
    input_variables=["foo", "bar"],
    partial_variables={"foo": "hello"},  # 预先定义foo值为hello
)
prompt = template3.format(foo="li4",bar="world")
print(prompt)