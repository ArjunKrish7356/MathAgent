# MathAgent

A minimal math agent that delegates all calculations to an MCP (Model Context Protocol) server. The agent uses MCP tools for every operation—no mental math—so you get consistent, inspectable results.

## What’s inside
- Agent: built with pydantic-ai, connected via MCP stdio
- MCP Server: powered by fastmcp, exposing math tools

### Available MCP tools
- add
- subtract
- multiply
- divide
- power
- log

Coming soon:
- modulus

## Requirements
- Python 3.13+
- uv (Python package/dependency manager)
- A Groq API key (for the LLM model)
- A Logfire token (for instrumentation)

## Setup
1) Clone the repository
2) Create your environment file
	 - Copy the example file and fill in your secrets
	 ```bash
	 cp .env.example .env
	 ```
	 - Set these keys:
		 - `groq_key` — your Groq API key
		 - `logfire_key` — your Logfire token

## Run the agent
Run with uv so dependencies are resolved and the MCP server is launched as a toolset:

```bash
uv run agent.py
```

Notes:
- The agent is configured to use the Groq model `qwen/qwen3-32b` (see `agent.py`). You can swap models as needed.
- The agent will reject non-math questions by design.
- All calculations route through the MCP tools defined in `mcp-server.py`.

## Contributing
Contributions are welcome—feel free to open issues or submit pull requests.



