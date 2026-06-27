import asyncio
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession

async def main():
    async with stdio_client(StdioServerParameters(
        command="python",
        args=[r"C:\Users\A\Desktop\test_mcp\server.py"]
    )) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = (await session.list_tools()).tools
            for t in tools:
                print(f"  {t.name}: {t.description}")

asyncio.run(main())
