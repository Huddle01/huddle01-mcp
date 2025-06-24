"""
Huddle01 MCP Server - Main Entry Point
======================================

This file serves as the main entry point for the Huddle01 MCP Server.
It initializes and runs the FastMCP application with proper configuration.
"""
import logging
import sys

from fastmcp import FastMCP
from contextlib import asynccontextmanager
from app.config import settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastMCP):
    """
    Lifespan event handler for the FastAPI application.
    """
    logger.info("Starting Huddle01 MCP Server...")
    try:
        if not settings.huddle01_api_key:
            logger.error("HUDDLE01_API_KEY environment variable is required")
            sys.exit(1)

        if not settings.huddle01_project_id:
            logger.error("HUDDLE01_PROJECT_ID environment variable is required")
            sys.exit(1)

        logger.info("Configuration validated successfully")
        
    except Exception as e:
        logger.critical(f"Fatal Error during API Startup: {e}")

    yield

    logger.info("Stopping Huddle01 MCP Server...")


# MCP Server Configuration
huddle01_mcp = FastMCP(
    name="Huddle01_MCP",
    version="0.1.0",
    lifespan=lifespan
)

# ASGI application instance for the Huddle01 MCP server
app = huddle01_mcp.http_app(path="/mcp", transport='streamable-http')
