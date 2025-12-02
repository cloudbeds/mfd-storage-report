import pytest

from app.common.http_client import HttpClient


class TestHttpClient:
    @pytest.mark.asyncio
    async def test_http_client_get(self, request_mock):
        http_client = HttpClient()
        request_mock({"foo": "bar"})
        response = await http_client.get("/clients")
        assert response == {"foo": "bar"}

    @pytest.mark.asyncio
    async def test_http_client_post(self, request_mock):
        request_mock({"success": True})
        http_client = HttpClient()
        response = await http_client.post("/documents/invoice", data={"id": 123})
        assert response == {"success": True}
