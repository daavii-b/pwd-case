from typing import Any, ClassVar, TypeVar, cast

from httpx import AsyncClient

T = TypeVar("T")


class SingletonMeta(type):
    instances: ClassVar[dict[type, Any]] = {}

    def __call__(cls: type[T], *args: object, **kwargs: object) -> T:
        cls_meta = cast("SingletonMeta", cls)

        if cls not in cls_meta.instances:
            instance = super().__call__(*args, **kwargs)
            cls_meta.instances[cls] = instance

        return cls_meta.instances[cls]


class HTTPClient(metaclass=SingletonMeta):
    def get_client(self, base_url: str) -> AsyncClient:
        return AsyncClient(base_url=base_url)
