# LangChain RAG MCP — Learning Examples

**English** | [简体中文](README.zh-CN.md)

This repository contains the code examples I created while learning **LangChain**, **RAG**, **MCP**, and **AI Agents**. The content is organized into 12 chapters that progress from fundamentals to advanced topics.

> LLM providers: DeepSeek, Alibaba Cloud DashScope, and Ollama

## Project Structure

```text
├── 01_helloworld/    Getting started and environment setup
├── 02_models/        Model initialization and multiple providers
├── 03_ollama/        Local models
├── 04_prompt/        Prompt engineering
├── 05_parser/        Output parsers
├── 06_lcel/          LCEL chains
├── 07_memory/        Conversation memory
├── 08_tool/          Custom tools
├── 09_embedding/     Text embeddings
├── 10_rag/           Retrieval-augmented generation
├── 11_mcp/           Model Context Protocol
├── 12_agent/         AI Agents
```

## Chapter Overview

| Chapter | Topic | Key Topics |
|---------|-------|------------|
| **01** | Hello World | Checking the LangChain version, making a first call with `init_chat_model()`, and adding logging, streaming, and error handling through a standard wrapper |
| **02** | Model Initialization | `init_chat_model`, `ChatOpenAI` with DeepSeek compatibility, `ChatDeepSeek`, `ChatTongyi` for Qwen, and the native OpenAI SDK |
| **03** | Local Models with Ollama | Running a local Qwen model with `ChatOllama` |
| **04** | Prompt Engineering | Prompt templates, message placeholders, JSON and YAML loading, partial variables, and synchronous, asynchronous, batch, and streaming calls |
| **05** | Output Parsing | String, JSON, and Pydantic parsers, plus structured output with TypedDict and Pydantic |
| **06** | LCEL | Pipelines with `RunnableSequence`, parallel execution, lambda functions, and conditional routing with `RunnableBranch` |
| **07** | Conversation Memory | In-memory message history, `RunnableWithMessageHistory`, and persistent history with Redis |
| **08** | Tool Definition | The `@tool` decorator, Pydantic argument schemas, tool binding and result parsing, and online weather queries |
| **09** | Text Embeddings | DashScope `text-embedding-v4`, cosine similarity with NumPy, and query and document embeddings |
| **10** | RAG | Loading common document formats, recursive text splitting, Redis vector storage, similarity search, and LLM generation |
| **11** | MCP | FastMCP tools, resources, and prompts; a custom MCP server over SSE; and MCP client calls |
| **12** | Agents | The ReAct pattern, LangChain v1.0 `create_agent()`, `AgentExecutor`, structured output, and multi-agent orchestration with A2A |

## Tech Stack

- **LLMs:** DeepSeek, Alibaba Cloud Qwen, and local models through Ollama
- **Embeddings:** Alibaba Cloud DashScope
- **Vector store:** Redis
- **Memory:** Redis and in-memory storage
- **MCP:** FastMCP and a custom SSE server
- **Document parsing:** PyMuPDF, docx2txt, and CSV, JSON, and Markdown loaders
- **Validation:** Pydantic v2 and TypedDict

## Environment Variables

Create a `.env` file in the project root:

```env
DASHSCOPE_API_KEY=your_aliyun_dashscope_api_key
deepseek-api=your_deepseek_api_key
```

## Learning Path

```text
01 → 02 → 03   Fundamentals: environment, models, and local deployment
   ↓
04 → 05 → 06   Core concepts: prompts → parsing → chain composition
   ↓
07 → 08        Advanced topics: memory systems + tool calling
   ↓
09 → 10        Practice: embeddings → vector stores → complete RAG pipeline
   ↓
11 → 12        Emerging topics: MCP + AI Agents
```
