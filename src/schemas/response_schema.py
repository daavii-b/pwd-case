from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict


class PaginationMeta(BaseModel):
    total: int
    page: int = 1


class PaginationResponseSchema[T](BaseModel):
    data: Sequence[T]
    meta: PaginationMeta

    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "data": [{"field_a": "value", "field_b": 123}],
                    "meta": {"total": 0, "page": 1},
                }
            ]
        },
    )
