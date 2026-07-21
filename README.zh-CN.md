<div align="center">

# LangChain

</div>

<div align="center">

**简体中文** | [English](README.md)

</div>

**LangChain** 是一个用于构建大语言模型（LLM）应用的框架，提供了模型调用、提示词管理、输出解析、链式编排、记忆、工具集成等一整套标准化接口，帮助开发者快速组装 LLM 驱动的工作流。

本项目是我在学习 **LangChain** 过程中记录的代码，按照主题分为 12 个章节，内容由浅入深。

## 项目结构

```
.
├── 01_helloworld/         # 基础入门：模型调用、环境验证
├── 02_models/             # 不同模型的使用：DeepSeek、通义千问、OpenAI 兼容接口
├── 03_ollama/             # 通过 Ollama 运行本地模型
├── 04_prompt/             # 提示词模板：构造、参数化、外部文件加载
├── 05_parser/             # 输出解析器：字符串、JSON、Pydantic、TypedDict
├── 06_lcel/               # LangChain 表达式语言：链式调用、并行、分支
├── 07_memory/             # 对话记忆：内存存储、Redis 持久化
├── 08_tool/               # 工具定义与 LLM 工具调用
├── 09_embedding/          # 文本嵌入：DashScope、OpenAI、Redis 向量存储
├── 10_rag/                # 检索增强生成：文档加载、文本切分、向量检索
├── 11_mcp/                # MCP 协议：自定义服务端/客户端实现
└── 12_agent/              # Agent 模式：ReAct、工具选择策略
```

