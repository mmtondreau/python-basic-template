from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from pythonproject.service import Service
from pythonproject.client import Client


@pytest.fixture()
def client_mock(mocker: MockerFixture) -> MagicMock:
    return mocker.patch("pythonproject.client.Client")


@pytest.fixture()
def service(client_mock: Client) -> Service:
    return Service(client_mock)


def test_hello(service: Service, client_mock: MagicMock) -> None:
    client_mock.do_post.return_value = "Hello"
    assert service.hello() == "Hello"
