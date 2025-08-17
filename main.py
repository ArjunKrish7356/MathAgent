from fastmcp import FastMCP

mcp = FastMCP("MathsTools")

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """subtract two integer numbers together."""
    return a - b

mcp.run()