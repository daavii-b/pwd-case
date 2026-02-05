from typing import Annotated, Literal

from fastapi import Depends, FastAPI, Query, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from httpx import AsyncClient
from pydantic import BaseModel

from config.http import lifespan
from config.http.http import get_http_client
from schemas import PaginationResponseSchema
from services.enums import ResourceEnum
from services.models import FetchInput
from services.star_wars_service import StarWarsService

app = FastAPI(lifespan=lifespan)


def get_star_wars_service(
    client: AsyncClient = Depends(get_http_client),
) -> StarWarsService:
    return StarWarsService(client)


class DashboardQueryParams(BaseModel):
    resource: ResourceEnum = ResourceEnum.PEOPLE
    page: int = Query(default=1, description="Current results page")
    search: str | None = Query(
        default=None, description="Search term to filter results"
    )
    sort_by: Literal["name", "title", "created_at", "edited_at"] = Query(
        default="created_at", description="Field to sort results by"
    )
    sort_dir: Literal["asc", "desc"] = Query(
        default="asc", description="Direction to sort results"
    )

    model_config = {"extra": "ignore"}


@app.get(
    "/health",
    response_class=Response,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={204: {"description": "Service is healthy"}},
)
def health_check() -> Response:
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.get(
    "/dashboard", response_class=JSONResponse, response_model=PaginationResponseSchema
)
async def dashboard(
    query: Annotated[DashboardQueryParams, Query()],
    star_wars_service: StarWarsService = Depends(get_star_wars_service),
) -> JSONResponse:
    output = await star_wars_service.fetch(
        filter_object=FetchInput(**query.model_dump())
    )

    encoded_output = sorted(
        [jsonable_encoder(item, by_alias=False) for item in output.data],
        key=lambda x: x.get(query.sort_by, "created_at"),
        reverse=query.sort_dir == "desc",
    )

    return JSONResponse(
        content={"data": encoded_output, "meta": jsonable_encoder(output.meta)},
        status_code=status.HTTP_200_OK,
    )
