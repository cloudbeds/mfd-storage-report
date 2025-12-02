import pytest

from tests.unit.mocks.access_token import SUPER_ADMIN_TOKEN


class TestInvoiceRouter:
    @pytest.mark.asyncio
    def test_get_products(self, test_client, request_mock):
        request_mock({"products": [{"id": "1123", "name": "coke"}]})
        response = test_client.get(
            "/products",
            headers={
                "Authorization": f"Bearer {SUPER_ADMIN_TOKEN}",
                "X-PROPERTY-ID": "79",
            },
        )
        assert response.status_code == 200
        assert len(response.json()["products"]) == 1
