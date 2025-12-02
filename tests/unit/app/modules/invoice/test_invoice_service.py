import pytest

from app.modules.invoice.schema import (
    ClientSchema,
    DocumentSchema,
    OutgoingInvoiceSchema,
)
from app.modules.invoice.service import InvoiceService


class TestInvoiceService:
    @pytest.mark.asyncio
    async def test_send_invoice(self, request_mock):
        request_mock({"success": True})
        response = await InvoiceService.send_invoice(
            OutgoingInvoiceSchema(
                client=ClientSchema(id=1),
                document=DocumentSchema(date="2023-01-01", paymentTerm=1),
                items=[],
            )
        )
        assert response == {"success": True}
