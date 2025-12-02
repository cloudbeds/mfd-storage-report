from typing import Dict

from fastapi import APIRouter, HTTPException

from app.modules.invoice.schema import (
    ClientSchema,
    DocumentSchema,
    IncomingInvoiceSchema,
    ItemSchema,
    OutgoingInvoiceSchema,
)
from app.modules.invoice.service import InvoiceService

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"],
)


@router.post("")
async def create_invoice(incoming_invoice: IncomingInvoiceSchema) -> Dict:
    # TODO:
    # Client id most like can be achieved with https://hotels.cloudbeds.com/api/v1.1/docs/#api-Guest-getGuest
    # Document info can be achieved with all the webhook payload
    # Items needs to be constructed with https://hotels.cloudbeds.com/api/v1.1/docs/#api-Payment-getPayments
    # Consider use getInvoice method

    client = ClientSchema(id=530)
    document = DocumentSchema(
        date=incoming_invoice.data.documentIssueDate, paymentTerm=0
    )
    items = [ItemSchema(id=item.id) for item in incoming_invoice.data.items]

    outgoing_invoice = OutgoingInvoiceSchema(
        client=client, document=document, items=items
    )

    print(outgoing_invoice)
    invoice = await InvoiceService.send_invoice(outgoing_invoice)

    if invoice:
        # TODO: send it back to MFD
        return {"success": True, "data": invoice}

    raise HTTPException(status_code=404, detail="Couldn't create an invoice")
