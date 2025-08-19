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

## Installation

Clone the repository:
```bash
git clone https://github.com/ArjunKrish7356/MathMCP.git
cd MathMCP
```
## Connecting with Pydantic AI

Use the official Pydantic AI MCP client: https://ai.pydantic.dev/mcp/client/. This MCP server is compatible with the Stdio transport.

Key points:
- Run the server so it reads from stdin and writes to stdout (MCP messages on stdio).
- Configure the Pydantic AI client to use the Stdio protocol; the client will spawn or attach to the server process and exchange MCP JSON messages over stdin/stdout.
- Ensure the client and server agree on MCP framing and version (see official docs below) before integrating.

## More Resources
- Official MCP documentation: https://modelcontextprotocol.io/docs/getting-started/intro  
- Introductory video on MCP: https://www.youtube.com/watch?v=N3vHJcHBS-w

## Contributing

Thank you for your interest! Contributions are welcome—feel free to open issues or submit pull requests.



