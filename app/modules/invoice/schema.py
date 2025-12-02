from typing import List

from pydantic import BaseModel

from app.modules.client.schema import ClientSchema


class ItemSchema(BaseModel):
    id: int


class IncomingInvoiceItemSchema(BaseModel):
    id: str
    description: str
    type: str
    quantity: float
    netAmount: float
    taxes: List[dict] = []
    fees: List[dict] = []


class DocumentSchema(BaseModel):
    date: str
    paymentTerm: int


class IncomingInvoiceDataSchema(BaseModel):
    invoiceId: int
    prefix: str
    number: str
    suffix: str
    documentIssueDate: str
    currency: str
    items: List[IncomingInvoiceItemSchema]
    taxes: List[dict]
    fees: List[dict]


class IncomingInvoiceSchema(BaseModel):
    success: bool
    data: IncomingInvoiceDataSchema


class OutgoingInvoiceSchema(BaseModel):
    client: ClientSchema
    document: DocumentSchema
    items: List[ItemSchema]
