"""macOS Calendar MCP Server."""

import os

from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))
mcp = FastMCP("macoscal", json_response=True, host="0.0.0.0", port=port)


@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello — confirms the server is running."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
