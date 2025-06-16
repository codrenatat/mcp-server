from mcp.server.fastmcp import FastMCP
from tools import get_current_price  # Importar tu función desde tools.py

# Crear servidor
mcp = FastMCP(
    name="Stock Price Server",
    host="0.0.0.0",
    port=8050,
)

# funcion que se va a usar en el cliente
@mcp.tool()
def get_current_price_tool(symbol: str) -> str:
    """
    Wrapper MCP para la función externa.
    """
    return get_current_price(symbol)


# ejecuta el servidor
if __name__ == "__main__":
    print("Iniciando servidor MCP con stdio")
    mcp.run(transport="stdio")
