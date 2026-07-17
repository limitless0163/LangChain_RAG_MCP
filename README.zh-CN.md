# LangChain RAG MCP — 学习代码

[English](README.md) | **简体中文**

本项目是我在学习 **LangChain**、**RAG**、**MCP** 和 **AI Agent** 过程中记录的代码，按照主题分为 12 个章节，内容由浅入深。

> LLM 供应商：DeepSeek、阿里云 DashScope、Ollama

## 目录结构

```text
├── 01_helloworld/    入门与环境配置
├── 02_models/        模型初始化与多供应商
├── 03_ollama/        本地模型
├── 04_prompt/        提示词工程
├── 05_parser/        输出解析器
├── 06_lcel/          LCEL 链式表达式
├── 07_memory/        对话记忆
├── 08_tool/          自定义工具
├── 09_embedding/     文本嵌入
├── 10_rag/           RAG 检索增强生成
├── 11_mcp/           MCP 模型上下文协议
├── 12_agent/         AI Agent
```

## 章节概览

| 章节 | 主题 | 要点 |
|------|------|------|
| **01** | Hello World | 检查 LangChain 版本，首次调用 `init_chat_model()`，通过标准化封装支持日志、流式输出和异常处理 |
| **02** | 模型初始化 | 使用 `init_chat_model`、兼容 DeepSeek 的 `ChatOpenAI`、`ChatDeepSeek`、面向千问的 `ChatTongyi` 以及 OpenAI 原生 SDK |
| **03** | Ollama 本地模型 | 通过 `ChatOllama` 调用本地 Qwen 模型 |
| **04** | 提示词工程 | 使用多种提示词模板和消息占位符，从 JSON、YAML 加载模板，配置部分变量，进行同步、异步、批量和流式调用 |
| **05** | 输出解析 | 使用字符串、JSON 和 Pydantic 解析器，通过 TypedDict 和 Pydantic 获取结构化输出 |
| **06** | LCEL | 使用 `RunnableSequence` 构建管道，实现并行执行、Lambda 转换和条件路由 |
| **07** | 对话记忆 | 管理内存消息历史，通过 `RunnableWithMessageHistory` 接入记忆，并使用 Redis 持久化 |
| **08** | 工具定义 | 使用 `@tool` 装饰器和 Pydantic 参数模型，完成工具绑定、结果解析及联网天气查询 |
| **09** | 文本嵌入 | 使用 DashScope `text-embedding-v4`，通过 NumPy 计算余弦相似度，生成查询与文档嵌入 |
| **10** | RAG | 加载常见格式文档，递归分割文本，使用 Redis 向量库完成相似度检索和 LLM 生成 |
| **11** | MCP | 使用 FastMCP 定义工具、资源和提示词，构建基于 SSE 的自定义 MCP Server，并通过 MCP Client 调用 |
| **12** | Agent | 实现 ReAct 模式，使用 LangChain v1.0 的 `create_agent()` 和 `AgentExecutor`，处理结构化输出并通过 A2A 编排多 Agent |

## 技术栈

- **LLM：** DeepSeek、阿里千问、Ollama 本地模型
- **嵌入：** 阿里云 DashScope
- **向量存储：** Redis
- **记忆：** Redis 和 InMemory
- **MCP：** FastMCP 和自定义 SSE Server
- **文档解析：** PyMuPDF、docx2txt、CSV、JSON 和 Markdown loaders
- **校验：** Pydantic v2 和 TypedDict

## 环境变量

在项目根目录创建 `.env` 文件：

```env
DASHSCOPE_API_KEY=你的阿里云DashScope密钥
deepseek-api=你的DeepSeek_API密钥
```

## 学习路线

```text
01 → 02 → 03   基础：环境、模型、本地部署
   ↓
04 → 05 → 06   核心：提示词 → 解析 → 链式编排
   ↓
07 → 08        进阶：记忆系统 + 工具调用
   ↓
09 → 10        实战：嵌入 → 向量库 → RAG 完整流水线
   ↓
11 → 12        前沿：MCP 协议 + Agent 智能体
```
