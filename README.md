# LangChain RAG MCP — 学习代码

本项目是我在学习 **LangChain**、**RAG**、**MCP** 和 **AI Agent** 过程中记录的代码，按照主题分 12 个章节循序渐进。

> LLM 供应商：DeepSeek（主力）、阿里云 DashScope（嵌入）、Ollama（本地模型）

## 目录结构

```
├── 01_helloworld/    入门与环境配置
├── 02_models/        模型初始化与多供应商
├── 03_ollama/        本地模型（Ollama）
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
| **01** | Hello World | LangChain 版本检查，`init_chat_model()` 首次调用，标准化封装（日志 / 流式 / 异常处理） |
| **02** | 模型初始化 | `init_chat_model`、`ChatOpenAI`（DeepSeek 兼容）、`ChatDeepSeek`、`ChatTongyi`（千问）、OpenAI 原生 SDK |
| **03** | Ollama 本地模型 | `ChatOllama` 调用本地 Qwen 模型 |
| **04** | 提示词工程 | `PromptTemplate` / `ChatPromptTemplate` / `FewShotPromptTemplate`、消息占位符、外部加载（JSON/YAML）、部分变量、同步/异步/批量/流式调用 |
| **05** | 输出解析 | `StrOutputParser`、`JsonOutputParser`、`PydanticOutputParser`、`with_structured_output()`（TypedDict / Pydantic） |
| **06** | LCEL | `RunnableSequence`（管道 `\|`）、`RunnableParallel`、`RunnableLambda`、`RunnableBranch` 条件路由 |
| **07** | 对话记忆 | `InMemoryChatMessageHistory`、`RunnableWithMessageHistory`、`RedisChatMessageHistory` 持久化 |
| **08** | 工具定义 | `@tool` 装饰器、Pydantic args_schema、`bind_tools()` + `JsonOutputKeyToolsParser`、联网天气查询 |
| **09** | 文本嵌入 | DashScope `text-embedding-v4`、余弦相似度（numpy）、`embed_query` / `embed_documents` |
| **10** | RAG | 文档加载（CSV/DOCX/JSON/MD/PDF/TXT）、文本分割（`RecursiveCharacterTextSplitter`）、Redis 向量库、相似度检索 → LLM 生成 |
| **11** | MCP | FastMCP Server（tool / resource / prompt）、自定义 MCP Server（SSE 传输）、MCP Client 调用 |
| **12** | Agent | ReAct 模式、`create_agent()`（LangChain v1.0）、`AgentExecutor`、结构化输出、多 Agent 编排（A2A） |

## 技术栈

- **LLM**: DeepSeek（`langchain-openai` 兼容接口）、阿里千问（`langchain-community` Tongyi）、Ollama 本地
- **嵌入**: 阿里云 DashScope `text-embedding-v4`
- **向量存储**: Redis（`langchain-redis`）
- **记忆**: Redis / InMemory
- **MCP**: `mcp[cli]` FastMCP + 自定义 SSE Server
- **文档解析**: PyMuPDF、docx2txt、CSV/JSON/Markdown loaders
- **校验**: Pydantic v2 + TypedDict

## 环境变量

在项目根目录创建 `.env` 文件：

```env
DASHSCOPE_API_KEY=你的阿里云DashScope密钥
deepseek-api=你的DeepSeek API密钥
```

## 学习路线

```
01 → 02 → 03      基础：环境、模型、本地部署
      ↓
   04 → 05 → 06   核心：提示词 → 解析 → 链式编排
      ↓
   07 → 08        进阶：记忆系统 + 工具调用
      ↓
   09 → 10        实战：嵌入 → 向量库 → RAG 完整流水线
      ↓
   11 → 12        前沿：MCP 协议 + Agent 智能体
```
