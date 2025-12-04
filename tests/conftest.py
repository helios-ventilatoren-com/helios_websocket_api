from unittest.mock import AsyncMock, patch

import pytest
from websockets.client import WebSocketClientProtocol

from helios_websocket_api import Client, Helios


@pytest.fixture
async def client():
    client = Client("127.0.0.1")
    await client.load_bundled_data_model("2.0.16")

    return client


@pytest.fixture
async def helios():
    helios = Helios("127.0.0.1")
    await helios.load_bundled_data_model("2.0.16")

    return helios


@pytest.fixture
def ws():
    with patch("websockets.client.connect") as connect:
        protocol_mock = AsyncMock(spec=WebSocketClientProtocol)
        connect.return_value.__aenter__.side_effect = protocol_mock

        yield protocol_mock.return_value
