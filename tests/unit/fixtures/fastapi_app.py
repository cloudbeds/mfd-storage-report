from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient
from pytest_mock import MockerFixture

from app.main import app

client = TestClient(app)


@pytest.fixture(scope="class")
def test_client():
    return client


@pytest.fixture(scope="function")
def app_settings(mocker: MockerFixture):
    APP_SETTINGS = dict(
        FACT_API_URL="http://some.url", FACT_API_TOKEN="some-random-token", LOG_LEVEL=10
    )
    mocker.patch("app.utils.http_client.settings", SimpleNamespace(**APP_SETTINGS))
