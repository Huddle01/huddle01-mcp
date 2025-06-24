import httpx
from app.config import settings

HUDDLE01_API_URL = "https://api.huddle01.com/api/v1"

headers = {
    "Content-Type": "application/json",
    "x-api-key": settings.huddle01_api_key,
}

client = httpx.AsyncClient(base_url=HUDDLE01_API_URL, headers=headers)