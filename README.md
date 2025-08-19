# Math MCP Server

This repository contains an MCP (Model Context Protocol) server for mathematical calculations.

## Current Tools
- add
- subtract
- multiply
- divide
- power
- log

## Coming Soon
- modulus

## Connecting with Pydantic AI

Use the official Pydantic AI MCP client: https://ai.pydantic.dev/mcp/client/. This MCP server is compatible with the Stdio transport.

1. Clone the repo into the working directory where your agent runs:
```
git clone https://github.com/ArjunKrish7356/MathMCP.git
```

2. Create an MCP server wrapper in your agent code (the `name` can be any unique id; `args` are the command used to start the server process):
```python
from pydantic_ai.mcp import MCPServerStdio

mcp_server = MCPServerStdio(
    'uv'
    args=[
        "run",
        "MathAgent/main.py"
    ]
)
```

3. Register the MCP server with your Agent:
```python
from pydantic_ai import Agent

agent = Agent(model="openai:gpt-4o", toolsets=[mcp_server])
```

Notes:
- Ensure the `MathAgent/main.py` path is correct relative to where the agent runs and that the script is runnable.
- The Stdio transport will spawn the configured process using the provided `args`; verify any required environment or dependencies are installed before launching.
- Test the connection locally before deploying.

## More Resources
- Official MCP documentation: https://modelcontextprotocol.io/docs/getting-started/intro  
- Introductory video on MCP: https://www.youtube.com/watch?v=N3vHJcHBS-w

## Contributing

Thank you for your interest! Contributions are welcome—feel free to open issues or submit pull requests.



