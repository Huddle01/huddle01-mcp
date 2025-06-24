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

    # Room Management Methods
    async def create_room(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """Create a new room"""
        return await self.make_request("POST", "/create-room", data=room_data)

    async def get_room(self, room_id: str) -> dict[str, Any]:
        """Get room details"""
        return await self.make_request("GET", f"/rooms/{room_id}")

    async def list_rooms(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """List all rooms"""
        return await self.make_request("GET", "/rooms", params=params)

    async def update_room(self, room_id: str, update_data: dict[str, Any]) -> dict[str, Any]:
        """Update room settings"""
        return await self.make_request("PATCH", f"/rooms/{room_id}", data=update_data)

    async def delete_room(self, room_id: str) -> dict[str, Any]:
        """Delete a room"""
        return await self.make_request("DELETE", f"/rooms/{room_id}")

    # Meeting Session Methods
    async def start_meeting(self, room_id: str) -> dict[str, Any]:
        """Start a meeting session"""
        return await self.make_request("POST", f"/rooms/{room_id}/start")

    async def end_meeting(self, room_id: str) -> dict[str, Any]:
        """End a meeting session"""
        return await self.make_request("POST", f"/rooms/{room_id}/end")

    async def get_meeting(self, room_id: str) -> dict[str, Any]:
        """Get meeting session details"""
        return await self.make_request("GET", f"/rooms/{room_id}/meeting")

    # Participant Management Methods
    async def get_participants(self, room_id: str) -> dict[str, Any]:
        """Get room participants"""
        return await self.make_request("GET", f"/rooms/{room_id}/participants")

    async def remove_participant(self, room_id: str, participant_id: str) -> dict[str, Any]:
        """Remove a participant"""
        return await self.make_request("DELETE", f"/rooms/{room_id}/participants/{participant_id}")

    async def mute_participant(self, room_id: str, participant_id: str) -> dict[str, Any]:
        """Mute a participant"""
        return await self.make_request("POST", f"/rooms/{room_id}/participants/{participant_id}/mute")

    async def unmute_participant(self, room_id: str, participant_id: str) -> dict[str, Any]:
        """Unmute a participant"""
        return await self.make_request("POST", f"/rooms/{room_id}/participants/{participant_id}/unmute")

    # Access Token Methods
    async def generate_access_token(self, token_data: dict[str, Any]) -> dict[str, Any]:
        """Generate access token"""
        return await self.make_request("POST", "/access-token", data=token_data)

    # Recording Methods
    async def start_recording(self, recording_data: dict[str, Any]) -> dict[str, Any]:
        """Start recording"""
        return await self.make_request("POST", "/recordings/start", data=recording_data)

    async def stop_recording(self, recording_id: str) -> dict[str, Any]:
        """Stop recording"""
        return await self.make_request("POST", f"/recordings/{recording_id}/stop")

    async def list_recordings(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """List recordings"""
        return await self.make_request("GET", "/recordings", params=params)

    async def get_recording(self, recording_id: str) -> dict[str, Any]:
        """Get recording details"""
        return await self.make_request("GET", f"/recordings/{recording_id}")

    # Analytics Methods
    async def get_room_analytics(self, room_id: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get room analytics"""
        return await self.make_request("GET", f"/analytics/rooms/{room_id}", params=params)

    async def get_project_analytics(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Get project analytics"""
        return await self.make_request("GET", "/analytics/project", params=params)

# Global client instance
huddle_client = Huddle01Client()
