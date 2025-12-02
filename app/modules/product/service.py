from app.common.http_client import HttpClient


class ProductService:
    @staticmethod
    async def get_products():
        http_client = HttpClient()
        return await http_client.get("/products")
