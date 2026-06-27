import asyncio
from mcp.server.fastmcp import FastMCP

server = FastMCP("Calculator MCP Server", instructions="MCP сервер с калькулятором")


@server.tool(description="Сложение двух чисел")
def add(первое_число: float, второе_число: float) -> float:
    return первое_число + второе_число


@server.tool(description="Вычитание второго числа из первого")
def subtract(первое_число: float, второе_число: float) -> float:
    return первое_число - второе_число


@server.tool(description="Умножение двух чисел")
def multiply(первое_число: float, второе_число: float) -> float:
    return первое_число * второе_число


@server.tool(description="Деление первого числа на второе")
def divide(первое_число: float, второе_число: float) -> float:
    if второе_число == 0:
        raise ValueError("Деление на ноль невозможно")
    return первое_число / второе_число


if __name__ == "__main__":
    asyncio.run(server.run_sse_async(host="127.0.0.1", port=8000))
