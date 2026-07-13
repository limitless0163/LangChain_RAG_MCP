from langchain_core.prompts import load_prompt


# 方式1：外部加载Prompt,将 prompt 保存为 JSON
template = load_prompt("04_prompt/load_external/prompt.json", encoding="utf-8")
message = template.format(name="张三", what="搞笑的")

print(message)