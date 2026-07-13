from langchain_core.prompts import PromptTemplate


template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")
prompt = template.invoke({"role": "python开发", "question": "冒泡排序怎么写？"})
print(prompt)
print()

print(prompt.to_string())
print()

print(prompt.to_messages())
print()