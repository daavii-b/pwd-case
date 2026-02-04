from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict


class PaginationResponseSchema[T](BaseModel):
    data: Sequence[T]
    count: int

    model_config = ConfigDict(extra="ignore")
