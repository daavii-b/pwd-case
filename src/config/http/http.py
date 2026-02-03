from typing import Any, Literal

from httpx import AsyncClient, Limits

from shared.patterns.singleton import SingletonMeta


class HTTPClient(metaclass=SingletonMeta):
    def get_client(self, base_url: str | None = None) -> AsyncClient:
        client_config: dict[Literal["limits", "base_url"], Any] = {
            "limits": Limits(max_keepalive_connections=20, max_connections=100)
        }

        if base_url is not None:
            client_config["base_url"] = base_url

        return AsyncClient(**client_config)
