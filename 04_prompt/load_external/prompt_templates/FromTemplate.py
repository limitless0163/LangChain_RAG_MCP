from langchain_core.prompts import PromptTemplate


# 方式2：使用 from_template 方法实例化提示词模板
template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

prompt = template.format(role="python开发",question="冒泡排序怎么写,只要代码其它不要，简洁")
print(prompt)
