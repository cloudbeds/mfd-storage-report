import pytest

from app.modules.product.service import ProductService


class TestProductService:
    @pytest.mark.asyncio
    async def test_get_products(self, request_mock):
        request_mock({"foo": "bar"})
        response = await ProductService.get_products()
        assert response == {"foo": "bar"}
