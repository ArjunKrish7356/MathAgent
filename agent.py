from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
import logfire
from dotenv import load_dotenv
import os

load_dotenv()
logfire_token = os.getenv("logfire_key")
groq_key = os.getenv("groq_key")

logfire.configure(token=logfire_token)
logfire.instrument_pydantic_ai()

server = MCPServerStdio(  
    'uv',
    args=[
        'run',
        'mcp-server.py'
    ]
)

prompt = """
/no_think
Math Agent using MCP tools. RULES:
1. NEVER calculate mentally - always use MCP math tools
2. ONLY math questions - else respond: "This question is outside my math context. Please ask a mathematical question."
3. Convert string numbers to numeric types before calling tools

CRITICAL: Tools expect numeric types (int/float), NOT strings
- "9" → 9, "6.5" → 6.5 before passing to tools

WORKFLOW:
1. Extract numbers from input
2. Convert strings to int/float  
3. Use tools for each operation with numeric inputs
4. Show step-by-step results
"""

model = GroqModel(
    'qwen/qwen3-32b', provider=GroqProvider(api_key=groq_key)
)

agent = Agent(
    system_prompt=prompt,
    model=model,
    toolsets=[server]
)

output = agent.run_sync(
    'what is 456 * 324 / 23 + 998 - 240?'
)

print(output.output)