from typing import Dict

from httpx import AsyncClient, HTTPStatusError

from app.common.logger import logger
from app.config import settings


class HttpClient:
    BASE_URL = settings.FACT_API_URL
    HEADERS = {
        # TODO: Pull API KEY per customer for FACT.PT
        "x-auth-token": settings.FACT_API_TOKEN,
        "Content-type": "application/json",
        "api-version": "1.0.0",
    }

    def __init__(self):
        self.client = AsyncClient(base_url=self.BASE_URL, headers=self.HEADERS)

    async def get(self, url: str) -> Dict:
        try:
            response = await self.client.get(url)
            response.raise_for_status()
        except HTTPStatusError as error:
            logger.error("Error doing a GET request", extra={"error": str(error)})
            return {}
        return response.json()

    async def post(self, url: str, data: dict) -> Dict:
        try:
            response = await self.client.post(url, json=data)
            response.raise_for_status()
        except HTTPStatusError as error:
            logger.error("Error doing a POST request", extra={"error": str(error)})
            return None
        return response.json()
