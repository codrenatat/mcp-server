import asyncio
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

nest_asyncio.apply() #entornos interactivos

async def main():
    #inicios el servidor con el stdio
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    #conecto al servidor
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            print("Herramientas disponibles:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            result = await session.call_tool("get_current_price_tool", {"symbol": "AAPL"})
            print(result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
