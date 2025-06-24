from typing import Any

import httpx

from app.config import settings

# Huddle01 API Base URLs
HUDDLE01_API_V2 = "https://api.huddle01.com/api/v2"

class Huddle01Client:
    """
    HTTP client for interacting with Huddle01 APIs
    """

    def __init__(self) -> None:
        self.api_key = settings.huddle01_api_key
        self.project_id = settings.huddle01_project_id
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "x-project-id": self.project_id
        }
    async def make_request(
        self,
        method: str,
        endpoint: str,
        base_url: str = HUDDLE01_API_V2,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        Make an HTTP request to Huddle01 API
        This method handles the HTTP request and returns the response data.
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, PATCH)
            endpoint: API endpoint path
            base_url: Base URL for the API (v1 or v2)
            data: JSON payload for the request
            params: Query parameters

        Returns:
            Response data as dictionary
        """
        url = f"{base_url}{endpoint}"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=self.headers,
                    json=data,
                    params=params,
                    timeout=30.0
                )
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}", "status_code": e.response.status_code}
        except httpx.HTTPError as e:
            return {"error": f"HTTP error: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

# Global client instance
huddle_client = Huddle01Client()
