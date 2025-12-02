import requests


def test_invoice_webhook():
    headers = {"Content-Type": "application/json"}
    data = {
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

    response = requests.post(
        "http://localhost:8000/invoice", headers=headers, json=data
    )

    assert response.status_code == 200
