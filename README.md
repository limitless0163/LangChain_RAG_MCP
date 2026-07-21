<div align="center">

# LangChain

</div>

<div align="center">

**English** | [简体中文](README.zh-CN.md)

</div>

**LangChain** is a framework for building applications powered by large language models (LLMs). It provides a standardized set of interfaces for model invocation, prompt management, output parsing, chaining, memory, tool integration, and more, helping developers quickly assemble LLM-driven workflows.

This repository contains the code I wrote while learning **LangChain**. It is organized into 12 chapters, progressing from basic concepts to advanced topics.

## Project Structure

```
.
├── 01_helloworld/         # Basic setup: model invocation, environment validation
├── 02_models/             # Using different LLMs: DeepSeek, Qwen (Tongyi), OpenAI-compatible
├── 03_ollama/             # Running local models via Ollama
├── 04_prompt/             # Prompt templates: construction, parameterization, external loading
├── 05_parser/             # Output parsers: string, JSON, Pydantic, TypedDict
├── 06_lcel/               # LangChain Expression Language: chains, parallelism, branching
├── 07_memory/             # Conversation memory: in-memory storage, Redis-backed history
├── 08_tool/               # Tool definitions and LLM tool calling
├── 09_embedding/          # Text embeddings: DashScope, OpenAI, Redis vector storage
├── 10_rag/                # Retrieval-Augmented Generation: document loading, text splitting, vector retrieval
├── 11_mcp/                # Model Context Protocol: custom server/client implementation
└── 12_agent/              # Agent patterns: ReAct, tool selection strategies
```

