from app.common.http_client import HttpClient
from app.modules.invoice.schema import OutgoingInvoiceSchema


class InvoiceService:
    @staticmethod
    async def send_invoice(outgoing_invoice: OutgoingInvoiceSchema):
        http_client = HttpClient()
        return await http_client.post(
            "/documents/invoice", data=outgoing_invoice.model_dump()
        )
