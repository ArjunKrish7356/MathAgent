from fastmcp import FastMCP

mcp = FastMCP("MathsTools")

@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two integer numbers together."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """subtract two integer numbers together."""
    return a - b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide two numbers. Raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool
def power(a: float, b: float) -> float:
    """Raise a number to the power of another number (a^b)."""
    return a ** b

@mcp.tool
def log(a: float, base: float = 10.0) -> float:
    """Calculate the logarithm of a number with the specified base (default base 10).
    
    Args:
        a: The number to calculate logarithm for (must be positive)
        base: The base of the logarithm (must be positive and not equal to 1, default is 10)
    """
    import math
    
    
    if a <= 0:
        raise ValueError("Logarithm input must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    
    return math.log(a) / math.log(base)

mcp.run()