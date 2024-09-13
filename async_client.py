from dataclasses import dataclass
from types import TracebackType
from typing import Any, AsyncIterator, Awaitable, Callable, List, Optional, Type, Dict

import asyncio
import aiohttp
from yarl import URL


@dataclass
class Response:
    status_code: int
    data: Optional[dict] = None


class AsyncClient:
    def __init__(self, base_url: str, *args, **kwargs) -> None:
        self._base_url = URL(base_url)
        self._client = aiohttp.ClientSession(*args, **kwargs)

    async def close(self) -> None:
        return await self._client.close()

    async def __aenter__(self) -> None:
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> Optional[bool]:
        await self.close()

        return None

    def _make_url(self, path: str) -> URL:
        return self._base_url / path

    async def post(self, path: str, params: Optional[dict] = {}) -> Response:
        async with self._client.post(self._make_url(path), params=params) as resp:
            status_code = resp.status
            data = await resp.json()
            return Response(status_code, data)

    async def get(self, path: str, params: Optional[dict] = {}) -> Response:
        async with self._client.get(self._make_url(path), params=params) as resp:
            status_code = resp.status
            data = await resp.json()
            return Response(status_code, data)

    async def delete(self, path: str, params: Optional[dict] = {}) -> Response:
        async with self._client.delete(self._make_url(path), params=params) as resp:
            status_code = resp.status
            data = await resp.json()
            return Response(status_code, data)

    async def update(self, path: str, params: Optional[dict] = {}) -> Response:
        async with self._client.patch(self._make_url(path), params=params) as resp:
            status_code = resp.status
            data = await resp.json()
            return Response(status_code, data)
