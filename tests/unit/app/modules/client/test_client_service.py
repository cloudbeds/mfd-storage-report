import pytest

from app.modules.client.service import ClientService


class TestClientService:
    @pytest.mark.asyncio
    async def test_get_clients(self, request_mock):
        request_mock({"foo": "bar"})
        response = await ClientService.get_clients()
        assert response == {"foo": "bar"}
