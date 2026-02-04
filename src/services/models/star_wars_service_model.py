from pydantic import BaseModel, ConfigDict, Field

from schemas import (
    FilmsExternalSchema,
    PeopleExternalSchema,
    PlanetsExternalSchema,
    StarshipsExternalSchema,
)
from schemas.response_schema import PaginationResponseSchema
from services.enums import ResourceEnum


class FetchInput(BaseModel):
    resource: ResourceEnum
    search: str | None
    page: int

    model_config = ConfigDict(extra="ignore")


class FetchOutput(
    PaginationResponseSchema[
        FilmsExternalSchema
        | PeopleExternalSchema
        | PlanetsExternalSchema
        | StarshipsExternalSchema
    ]
):
    pass


class ResourceQuery(BaseModel):
    search: str | None
    page: int

    model_config = ConfigDict(extra="ignore")


class ResourceOutput[T](BaseModel):
    count: int = Field(alias="count")
    output: list[T]
