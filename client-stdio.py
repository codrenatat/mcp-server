import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # We define the server parameters
    server_params = StdioServerParameters(
        command = "python", # The command to run the server
        args = ["server.py"], # The arguments to pass to the server
    )

    # Connect to the server
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the session connection
            await session.initialize()

            # We list the tools available in the server
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            # We call the tool "add" with the arguments {"a": 1, "b": 2}
            result = await session.call_tool("add", arguments={"a": 1, "b": 2})

            # We print the result
            print(f"1 + 3 = {result.content[0].text}")
