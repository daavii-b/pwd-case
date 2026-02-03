from typing import Any, ClassVar, TypeVar, cast

T = TypeVar("T")


class SingletonMeta(type):
    instances: ClassVar[dict[type, Any]] = {}

    def __call__(cls: type[T], *args: object, **kwargs: object) -> T:
        cls_meta = cast("SingletonMeta", cls)

        if cls not in cls_meta.instances:
            instance = super().__call__(*args, **kwargs)
            cls_meta.instances[cls] = instance

        return cls_meta.instances[cls]
