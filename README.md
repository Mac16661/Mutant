# Mutant MCP server 
</a>
    <a href="https://discord.gg/NFqcw572Q">
        <img class="dark-light" style="padding-right: 4px; padding-bottom: 4px;" src="https://img.shields.io/discord/1220325004013604945?color=2f9d97&labelColor=0a1410&label=%20&logo=discord&logoColor=white">
</a>
 </a>
    <a href="https://mutantai.org/">
        <img class="dark-light" style="padding-right: 4px; padding-bottom: 4px;" src="https://img.shields.io/badge/WBSITE-MUTANTAI-ORG">
</a>

**Mutant is a multi-model genetic evolution engine that iteratively refines LLM responses to minimize hallucinations and maximize accuracy while reducing inference cost.**

---

## Overview

Mutant is an evolutionary optimization engine for Large Language Models (LLMs).

Instead of relying on a single model, Mutant generates multiple candidate responses, evolves them through a genetic optimization process, and converges on a higher-quality final answer.

This approach enables:

- Reduced hallucinations
- Improved response accuracy
- Lower inference costs
- Local Inference
- Better reasoning for complex engineering, programming, mathematics, and scientific problems

---

## How It Works

```
                User Query
                     │
                     ▼
          Generate Initial Population
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
    GPT            Claude         DeepSeek
     │               │               │
     └───────────────┼───────────────┘
                     ▼
          Evolutionary Optimization
     (Selection • Mutation • Crossover)
                     │
                     ▼
             Converged Final Answer
```

Mutant continuously evolves candidate responses until convergence or a stopping criterion is reached.

---

## Features

- Multi-model reasoning
- Genetic evolution of LLM responses
- Support Ollama for local inference
- Compatible with OpenAI and Groq
- Parallel execution
- MCP server support

---

# Installation

## Prerequisites

- Docker Desktop (or Docker Engine)
- OpenAI API key / A Groq API key / Ollama

## Pull the Docker image

```bash
docker pull mac16661/mutant-mcp:latest
```

The image is now available locally and can be used by any MCP client that supports Docker.


# MCP Integration

Examples:

```json
{
  "mcpServers": {
    "mutant": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "mutant-mcp",
        "-e", "OPENAI_API_KEY=sk-proj-...",
        "--models",
        "[{\"openai\":\"gpt-5.4-mini\"},{\"openai\":\"gpt-5.4-mini\"}]"
      ],
      "env": {}
    }
  }
}
```

Run docker inside wsl:

```bash
{
  "mcpServers": {
    "mutant": {
      "command": "wsl",
      "args": [
        "docker",
        "run",
        "--rm",
        "-i",
        "mutant-mcp",
        "-e", "OPENAI_API_KEY=sk-proj-",
        "-e", "GROQ_API_KEY=gsk_",
        "--models",
        "[{\"openai\":\"gpt-5.4-mini\"},{\"groq\":\"openai/gpt-oss-120b\"}]"
      ],
      "env": {}
    }
  }
}
```

# Configation

| Parameter           | Description                  | Default                                                  |
| ------------------- | ---------------------------- | -------------------------------------------------------- |
| `--models`          | Models used during evolution | [{\"openai\" : \"gpt-5.4\"}, {\"openai\": \"gpt-5.4\"}]  |
| `--max_iterations`  | Evolution rounds             | 10                                                        |

## Model Configuration

Mutant supports combining models from multiple providers in a single evolution pipeline. You can use any number of models from any supported provider.

### Ollama Only

```bash
"--models", "[{\"ollama\":\"qwen3:8b\"},{\"ollama\":\"deepseek-r1:8b\"}]"

"-e", "OLLAMA_URL=http://<HOST>:<PORT>/v1"
"-e", "OLLAMA_API_KEY=ollama"
```

```bash
"--models", "[{\"ollama\":\"qwen3:14b\"},{\"ollama\":\"qwen3:14b\"}]"

"-e", "OLLAMA_URL=http://<HOST>:<PORT>/v1"
"-e", "OLLAMA_API_KEY=ollama"
```

### Mixed Providers

```bash
"--models", "[{\"openai\":\"gpt-5.4-mini\"},{\"groq\":\"meta-llama/llama-4-scout-17b-16e-instruct\"},{\"ollama\":\"deepseek-r1:8b\"}]"

"-e", "OPENAI_API_KEY=sk-proj-..."
"-e", "GROQ_API_KEY=gsk_..."
"-e", "OLLAMA_URL=http://<HOST>:<PORT>/v1"
"-e", "OLLAMA_API_KEY=ollama"
```

### Configuration Notes

* You may specify **any number of models** in the `--models` array.
* Models can come from **one provider or a mix of supported providers** (OpenAI, Groq, Ollama).
* For **cloud-hosted providers** (such as OpenAI and Groq), configure the corresponding API key using environment variables.
* For **Ollama**, provide:

  * `OLLAMA_URL` — the OpenAI-compatible Ollama endpoint (for example, `http://localhost:11434/v1`).
  * `OLLAMA_API_KEY` — any non-empty value (the default `ollama` is commonly used).

> **Important:** Mutant relies on **structured outputs**. Only use models that support structured output (JSON schema/function calling). Models without structured output support are not compatible and may fail to work correctly. Small models may not reliably follow structured output requirements, which can cause response generation to fail.

# How to use

User:

```
Use Mutant to Design a lock-free B+ Tree.
```

Mutant:

```
1. Generates responses from multiple models
2. Evolves candidate solutions
3. Produces an optimized final answer

The final response is returned to the MCP client (e.g., Claude Desktop).
```

---

# Roadmap

- [X] OpenAI
- [X] Groq
- [X] Ollama
- [X] Gemini (via google ai studio)
- [ ] Anthropic
- [ ] Benchmark
- [ ] Token usage dashboard

---

# Contributing

Contributions, issues, and feature requests are welcome.

---

# License

MIT License
