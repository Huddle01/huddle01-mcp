from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

huddle01_mcp = FastMCP(
    name="Huddle01_MCP",
    version="0.1.0",
)

@huddle01_mcp.custom_route("/healthz", methods=["GET"])
async def health_check(request: Request):
    """
    Health check endpoint to verify the service is running.
    """
    return JSONResponse({"status": "ok"}, status_code=200)