# Functions from the mcp python sdk 
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")

# Creating our MCP server
# Similar to FastAPI 
# If http specify port and host if not standart io 
mcp = FastMCP(
    name = "Calculator",
    host = "0.0.0.0",   # Only used for SSE transport (localhost)
    port = 8050,    # Only used for SSE transport (set to any port)
)

#  Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# Run the server
if __name__ == "__main__":
    transport = "sse"
    if transport == "stdio":
        print("Running mcp server with stdio transport")
        mcp.run(transport = "stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport = "sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
