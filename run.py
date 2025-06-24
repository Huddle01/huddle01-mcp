"""
Huddle01 MCP Server - Main Entry Point
======================================

This file serves as the main entry point for the Huddle01 MCP Server.
It initializes and runs the FastMCP application with proper configuration.
"""
import asyncio
import logging
import sys

from app.config import settings
from app.mcp import huddle01_mcp

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Main function to run the FastMCP application
async def main() -> None:
    try:
        logger.info("Starting Huddle01 MCP Server...")

        if not settings.huddle01_api_key:
            logger.error("HUDDLE01_API_KEY environment variable is required")
            sys.exit(1)

        if not settings.huddle01_project_id:
            logger.error("HUDDLE01_PROJECT_ID environment variable is required")
            sys.exit(1)

        logger.info("Configuration validated successfully")

        await huddle01_mcp.run_async(transport="http")

    except KeyboardInterrupt:
        logger.info("Received shutdown signal, stopping server...")
    except Exception as e:
        logger.exception("Failed to start server:", exc_info=e)
        sys.exit(1)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
