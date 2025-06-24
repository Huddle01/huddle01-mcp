from app.mcp import huddle01_mcp

# Main function to run the FastMCP application
async def main():
    await huddle01_mcp.run_async(transport="http")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())