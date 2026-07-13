from langchain_core.prompts import PromptTemplate


# partial()方法可以格式化部分变量，并且继续返回一个模板
template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")
partial = template.partial(role="python开发")

print(partial)
print()

prompt = partial.format(question="冒泡排序怎么写？")
print(prompt)
