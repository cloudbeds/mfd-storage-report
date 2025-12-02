import pytest
from pytest_mock import MockerFixture


@pytest.fixture(scope="function")
def send_invoice_mock(mocker: MockerFixture):
    mocker.patch(
        "app.modules.invoice.service.InvoiceService.send_invoice",
        mocker.AsyncMock(return_value=dict(invoice="invoice")),
    )
