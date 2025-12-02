import pytest
from pytest_mock import MockerFixture


@pytest.fixture(scope="function")
def request_mock(mocker: MockerFixture):
    def mock_httpx(response: dict):
        request_mock = mocker.Mock()
        request_mock.json.return_value = response
        request_mock.raise_for_status.return_value = False
        mocker.patch(
            "httpx.AsyncClient.get", mocker.AsyncMock(return_value=request_mock)
        )
        mocker.patch(
            "httpx.AsyncClient.post", mocker.AsyncMock(return_value=request_mock)
        )

    yield mock_httpx
