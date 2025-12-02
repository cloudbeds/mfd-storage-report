import pytest


class TestInvoiceRouter:
    @pytest.mark.asyncio
    def test_post_invoice(self, test_client, send_invoice_mock):
        json = {
            "success": True,
            "data": {
                "invoiceId": 12345,
                "prefix": "inv",
                "number": "234",
                "suffix": "-b",
                "documentIssueDate": "2017-12-03",
                "currency": "MXN",
                "items": [
                    {
                        "id": "340",
                        "description": "Reservation",
                        "type": "service",
                        "quantity": 2,
                        "netAmount": 10,
                        "taxes": [],
                        "fees": [],
                    }
                ],
                "taxes": [],
                "fees": [],
            },
        }
        response = test_client.post("/invoices", json=json)

        assert response.status_code == 200
