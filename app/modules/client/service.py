from app.common.http_client import HttpClient


class ClientService:
    @staticmethod
    async def get_clients():
        http_client = HttpClient()
        return await http_client.get("/clients")
