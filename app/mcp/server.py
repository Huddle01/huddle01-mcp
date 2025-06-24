from typing import Any

import httpx
from fastmcp import FastMCP
from app.mcp.client import huddle_client
from starlette.requests import Request
from starlette.responses import JSONResponse

huddle01_mcp = FastMCP(
    name="Huddle01_MCP",
    version="0.1.0",
)

@huddle01_mcp.custom_route("/healthz", methods=["GET"])
async def health_check(_request: Request) -> JSONResponse:
    """
    Health check endpoint to verify the service is running.
    """
    return JSONResponse({"status": "ok"}, status_code=200)

@huddle01_mcp.tool
async def create_room(
    room_locked: bool = False,
    metadata: dict[str, Any] = {},
) -> dict[str, Any]:
    """
    Create a new Huddle01 room for video conferencing.
    
    Args:
        roomLocked (bool): Whether the room is locked for entry.
        metadata (dict): Additional metadata for the room.
    
    Returns:
        Room creation response with room details
        - message (str): Status message, e.g., "Room created successfully"
        - roomId (str): Unique identifier for the created room
    """
    try:
        payload = {
            "roomLocked": room_locked,
            "metadata": metadata
        }
        
        response = await huddle_client.make_request(
            method="POST",
            endpoint="/create-room",
            data=payload,
        )
        
        return response
    except httpx.HTTPError as e:
        return {"error": f"HTTP error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}
