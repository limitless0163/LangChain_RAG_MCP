from langchain_core.prompts import PromptTemplate


template1 = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂，") + "内容不超过{length}个字"

# 使用format方法填充占位符, 生成提示词
prompt1 = template1.format(topic="LangChain", length=100)
print(prompt1)

# 分别创建两个独立的PromptTemplate模板
prompt_a = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂，")
prompt_b = PromptTemplate.from_template("内容不超过{length}个字")

# 将两个模板进行拼接组合
prompt_all = prompt_a + prompt_b

# 使用format方法填充占位符, 生成提示词
prompt2 = prompt_all.format(topic="LangChain", length=200)
print(prompt2)


