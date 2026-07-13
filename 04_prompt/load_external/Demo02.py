from langchain_core.prompts import load_prompt


# 方式2：外部加载Prompt,将 prompt 保存为 yaml
template = load_prompt("04_prompt/load_external/prompt.yaml", encoding="utf-8")
message = template.format(name="年轻人", what="滑稽")

print(message)
