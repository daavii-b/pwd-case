from fastapi import HTTPException
from httpx import AsyncClient, HTTPStatusError, RequestError

from mappers import FilmsMapper, PeopleMapper, PlanetsMapper, StarshipsMapper
from schemas import (
    FilmsExternalSchema,
    PeopleExternalSchema,
    PlanetsExternalSchema,
    StarshipsExternalSchema,
)
from schemas.response_schema import PaginationMeta
from services.enums import ResourceEnum
from services.models import FetchInput, FetchOutput, ResourceOutput, ResourceQuery
from shared.patterns.singleton import SingletonMeta

DEFAULT_ERRORS = {
    "external_provider_error": HTTPException(
        status_code=502, detail="Error in the external provider"
    ),
    "external_provider_unavailable": HTTPException(
        status_code=504, detail="External provider unavailable"
    ),
    "invalid_resource": HTTPException(status_code=400, detail="Invalid resource"),
}


class StarWarsService(metaclass=SingletonMeta):
    _client: AsyncClient

    def __init__(self, client: AsyncClient) -> None:
        self._client = client

    async def fetch(self, filter_object: FetchInput) -> FetchOutput:
        resource_query = ResourceQuery(
            search=filter_object.search, page=filter_object.page
        )

        match filter_object.resource:
            case ResourceEnum.PEOPLE:
                result = await self.fetch_people(resource_query)
            case ResourceEnum.FILMS:
                result = await self.fetch_films(resource_query)
            case ResourceEnum.STARSHIPS:
                result = await self.fetch_starships(resource_query)
            case ResourceEnum.PLANETS:
                result = await self.fetch_planets(resource_query)
            case _:
                raise DEFAULT_ERRORS["invalid_resource"]

        return FetchOutput(
            data=result.output,
            meta=PaginationMeta(total=result.count, page=filter_object.page),
        )

    async def fetch_people(
        self, query: ResourceQuery
    ) -> ResourceOutput[PeopleExternalSchema]:
        try:
            response = await self._client.get("/people", params=query.model_dump())

            response.raise_for_status()

            json_response = response.json()

            return ResourceOutput(
                **json_response,
                output=[
                    PeopleMapper.to_external(item) for item in json_response["results"]
                ],
            )
        except HTTPStatusError as err:
            raise DEFAULT_ERRORS["external_provider_error"] from err
        except RequestError as err:
            raise DEFAULT_ERRORS["external_provider_unavailable"] from err

    async def fetch_films(
        self, query: ResourceQuery
    ) -> ResourceOutput[FilmsExternalSchema]:
        try:
            response = await self._client.get("/films", params=query.model_dump())

            response.raise_for_status()

            json_response = response.json()

            return ResourceOutput(
                **json_response,
                output=[
                    FilmsMapper.to_external(item) for item in json_response["results"]
                ],
            )
        except HTTPStatusError as err:
            raise DEFAULT_ERRORS["external_provider_error"] from err
        except RequestError as err:
            raise DEFAULT_ERRORS["external_provider_unavailable"] from err

    async def fetch_starships(
        self, query: ResourceQuery
    ) -> ResourceOutput[StarshipsExternalSchema]:
        try:
            response = await self._client.get("/starships", params=query.model_dump())

            response.raise_for_status()

            json_response = response.json()

            return ResourceOutput(
                **json_response,
                output=[
                    StarshipsMapper.to_external(item)
                    for item in json_response["results"]
                ],
            )
        except HTTPStatusError as err:
            raise DEFAULT_ERRORS["external_provider_error"] from err
        except RequestError as err:
            raise DEFAULT_ERRORS["external_provider_unavailable"] from err

    async def fetch_planets(
        self, query: ResourceQuery
    ) -> ResourceOutput[PlanetsExternalSchema]:
        try:
            response = await self._client.get("/planets", params=query.model_dump())

            response.raise_for_status()

            json_response = response.json()

            return ResourceOutput(
                **json_response,
                output=[
                    PlanetsMapper.to_external(item) for item in json_response["results"]
                ],
            )
        except HTTPStatusError as err:
            raise DEFAULT_ERRORS["external_provider_error"] from err
        except RequestError as err:
            raise DEFAULT_ERRORS["external_provider_unavailable"] from err
