from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any, Literal

from fastapi import FastAPI
from httpx import AsyncClient, Limits

http_client_wrapper: dict[Literal["client"], AsyncClient] = {}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    client = AsyncClient(
        base_url="https://swapi.dev/api/",
        limits=Limits(max_keepalive_connections=20, max_connections=100),
    )

    http_client_wrapper["client"] = client

    yield

    await client.aclose()


def get_http_client() -> AsyncClient:
    return http_client_wrapper["client"]
