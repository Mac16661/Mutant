# Mutant

> **Mutant is a multi-model genetic evolution framework that iteratively refines LLM responses to minimize hallucinations and maximize accuracy while reducing inference cost.**

---

## Overview

Mutant is an evolutionary optimization framework for Large Language Models (LLMs).

Instead of relying on a single model, Mutant generates multiple candidate responses, evolves them through a genetic optimization process, and converges on a higher-quality final answer.

This approach enables:

- Reduced hallucinations
- Improved response accuracy
- Lower inference costs
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
- Compatible with OpenAI and Groq
- Parallel execution
- MCP server support

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Mac16661/Mutant.git
cd Mutant
```

---

## Configuration

Configure the following before running Mutant:

1. Installation path
2. Models to use
3. API keys


# MCP Integration

Mutant exposes an MCP server that can be connected to Claude Desktop.

Example configuration:

```json
{
  "mcpServers": {
    "mutant": {
      "command": "PATH\\dist\\server.exe",
      "args": [
        "--models",
        "[{\"openai\": \"gpt-5.4-mini\"}, {\"groq\": \"meta-llama/llama-4-scout-17b-16e-instruct\"}]"
      ],
      "env": {
        "OPENAI_API_KEY": "sk-proj-...",
        "ANTHROPIC_API_KEY": "sk-ant-...",
        "GROQ_API_KEY": "gsk_..."
      }
    }
  }
}
```

# Example

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

- [ ] Add support for more providers (Anthropic, Gemini, etc.)
- [ ] Local model support
- [ ] Benchmark
- [ ] Token usage dashboard

---

# Contributing

Contributions, issues, and feature requests are welcome.

Please open an issue before submitting a large pull request.

---

# License

MIT License
