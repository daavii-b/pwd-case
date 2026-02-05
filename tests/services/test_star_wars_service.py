from typing import Any

import httpx
import pytest
from fastapi import HTTPException
from pytest_httpx import HTTPXMock

from schemas.films_schema import FilmsExternalSchema
from schemas.people_schema import PeopleExternalSchema
from schemas.planets_schema import PlanetsExternalSchema
from schemas.response_schema import PaginationMeta
from schemas.starships_schema import StarshipsExternalSchema
from services.enums import ResourceEnum
from services.models import FetchInput, FetchOutput
from services.star_wars_service import StarWarsService


class TestStarWarsServiceIntegration:
    """Integration tests for StarWarsService."""

    sut: StarWarsService

    @pytest.fixture(autouse=True)
    def setup(self, star_wars_service: StarWarsService) -> None:
        self.sut = star_wars_service

    @pytest.mark.asyncio
    async def test_fetch_people_successfully(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test successful fetch of people resource."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=1",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=1)
        )

        assert isinstance(result, FetchOutput)
        assert result.meta.total == 1
        assert result.meta.page == 1
        assert len(result.data) == 1

        person = result.data[0]

        assert isinstance(person, PeopleExternalSchema)
        assert person.name == "Luke Skywalker"
        assert person.height == "172"

    @pytest.mark.asyncio
    async def test_fetch_films_successfully(
        self,
        httpx_mock: HTTPXMock,
        films_api_response: dict[str, Any],
    ) -> None:
        """Test successful fetch of films resource."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/films?page=1",
            json=films_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.FILMS, search=None, page=1)
        )

        assert isinstance(result, FetchOutput)
        assert len(result.data) == 1
        assert result.meta.total == 1
        assert result.meta.page == 1

        film = result.data[0]

        assert isinstance(film, FilmsExternalSchema)
        assert film.title == "A New Hope"
        assert film.episode_id == 4

    @pytest.mark.asyncio
    async def test_fetch_starships_successfully(
        self,
        httpx_mock: HTTPXMock,
        starships_api_response: dict[str, Any],
    ) -> None:
        """Test successful fetch of starships resource."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/starships?page=1",
            json=starships_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.STARSHIPS, search=None, page=1)
        )

        assert isinstance(result, FetchOutput)
        assert len(result.data) == 1
        assert result.meta.total == 1
        assert result.meta.page == 1

        starship = result.data[0]

        assert isinstance(starship, StarshipsExternalSchema)
        assert starship.name == "Millennium Falcon"
        assert starship.model == "YT-1300 light freighter"

    @pytest.mark.asyncio
    async def test_fetch_planets_successfully(
        self,
        httpx_mock: HTTPXMock,
        planets_api_response: dict[str, Any],
    ) -> None:
        """Test successful fetch of planets resource."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/planets?page=1",
            json=planets_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PLANETS, search=None, page=1)
        )

        assert isinstance(result, FetchOutput)
        assert len(result.data) == 1
        assert result.meta.total == 1
        assert result.meta.page == 1

        planet = result.data[0]

        assert isinstance(planet, PlanetsExternalSchema)
        assert planet.name == "Tatooine"
        assert planet.climate == "arid"

    @pytest.mark.asyncio
    async def test_fetch_with_pagination(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test that pagination parameter is correctly passed to the API."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=3",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=3)
        )

        assert result.meta.page == 3
        assert isinstance(result.meta, PaginationMeta)

    @pytest.mark.asyncio
    async def test_pagination_metadata(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test pagination metadata in response."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=2",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=2)
        )

        assert result.meta.total == 1
        assert result.meta.page == 2

    @pytest.mark.asyncio
    async def test_fetch_with_search_parameter(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test that search parameter is correctly passed to the API."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?search=skywalker&page=1",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search="skywalker", page=1)
        )

        assert isinstance(result, FetchOutput)
        assert len(result.data) > 0

    @pytest.mark.asyncio
    async def test_fetch_with_search_and_pagination(
        self,
        httpx_mock: HTTPXMock,
        films_api_response: dict[str, Any],
    ) -> None:
        """Test combination of search and pagination parameters."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/films?search=hope&page=1",
            json=films_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.FILMS, search="hope", page=1)
        )

        assert isinstance(result, FetchOutput)
        assert result.meta.page == 1

    @pytest.mark.asyncio
    async def test_fetch_with_http_status_error(
        self,
        httpx_mock: HTTPXMock,
    ) -> None:
        """Test handling of HTTP status errors (500)."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=1",
            status_code=500,
            json={"detail": "Internal Server Error"},
        )

        with pytest.raises(HTTPException) as exc_info:
            await self.sut.fetch(
                FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=1)
            )

        assert exc_info.value.status_code == 502
        assert exc_info.value.detail == "Error in the external provider"

    @pytest.mark.asyncio
    async def test_fetch_with_request_error(
        self,
        httpx_mock: HTTPXMock,
    ) -> None:
        """Test handling of request errors (timeout/network issues)."""
        httpx_mock.add_exception(
            httpx.RequestError("Connection timeout"),
            url="https://swapi.dev/api/people?page=1",
        )

        with pytest.raises(HTTPException) as exc_info:
            await self.sut.fetch(
                FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=1)
            )

        assert exc_info.value.status_code == 504
        assert exc_info.value.detail == "External provider unavailable"

    @pytest.mark.asyncio
    async def test_fetch_with_invalid_resource(
        self,
    ) -> None:
        """Test handling of invalid resource enum."""
        from pydantic import ValidationError

        with pytest.raises(ValidationError) as exc_info:
            FetchInput(
                resource="invalid_resource",  # type: ignore
                search=None,
                page=1,
            )

        assert "resource" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_response_data_mapping(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test that API response data is correctly mapped using mappers."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=1",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=1)
        )

        person = result.data[0]
        assert hasattr(person, "name")
        assert hasattr(person, "height")
        assert hasattr(person, "mass")
        assert hasattr(person, "created_at")
        assert hasattr(person, "edited_at")

    @pytest.mark.asyncio
    async def test_response_structure(
        self,
        httpx_mock: HTTPXMock,
        people_api_response: dict[str, Any],
    ) -> None:
        """Test the structure of the response with data and metadata."""
        httpx_mock.add_response(
            method="GET",
            url="https://swapi.dev/api/people?page=1",
            json=people_api_response,
            status_code=200,
        )

        result = await self.sut.fetch(
            FetchInput(resource=ResourceEnum.PEOPLE, search=None, page=1)
        )

        assert hasattr(result, "data")
        assert hasattr(result, "meta")
        assert isinstance(result.data, list)
        assert isinstance(result.meta, PaginationMeta)
        assert hasattr(result.meta, "total")
        assert hasattr(result.meta, "page")


@pytest.fixture
def star_wars_service() -> StarWarsService:
    """Create a StarWarsService instance with mocked HTTP client."""
    client = httpx.AsyncClient(base_url="https://swapi.dev/api")
    return StarWarsService(client=client)


@pytest.fixture
def people_api_response() -> dict[str, Any]:
    """Mock API response for people resource."""
    return {
        "count": 1,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                "homeworld": "https://swapi.dev/api/planets/1/",
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                    "https://swapi.dev/api/films/3/",
                    "https://swapi.dev/api/films/6/",
                ],
                "species": [],
                "vehicles": [
                    "https://swapi.dev/api/vehicles/14/",
                    "https://swapi.dev/api/vehicles/30/",
                ],
                "starships": [
                    "https://swapi.dev/api/starships/12/",
                    "https://swapi.dev/api/starships/22/",
                ],
                "created": "2014-12-09T13:50:51.644000Z",
                "edited": "2014-12-20T21:17:56.891000Z",
                "url": "https://swapi.dev/api/people/1/",
            }
        ],
    }


@pytest.fixture
def films_api_response() -> dict[str, Any]:
    """Mock API response for films resource."""
    return {
        "count": 1,
        "results": [
            {
                "title": "A New Hope",
                "episode_id": 4,
                "opening_crawl": "It is a period of civil war...",
                "director": "George Lucas",
                "producer": "Gary Kurtz, Rick McCallum",
                "release_date": "1977-05-25",
                "characters": [
                    "https://swapi.dev/api/people/1/",
                ],
                "planets": [
                    "https://swapi.dev/api/planets/1/",
                ],
                "starships": [
                    "https://swapi.dev/api/starships/2/",
                ],
                "vehicles": [
                    "https://swapi.dev/api/vehicles/4/",
                ],
                "species": [
                    "https://swapi.dev/api/species/1/",
                ],
                "created": "2014-12-10T14:23:31.880000Z",
                "edited": "2014-12-20T19:49:45.256000Z",
                "url": "https://swapi.dev/api/films/1/",
            }
        ],
    }


@pytest.fixture
def starships_api_response() -> dict[str, Any]:
    """Mock API response for starships resource."""
    return {
        "count": 1,
        "results": [
            {
                "name": "Millennium Falcon",
                "model": "YT-1300 light freighter",
                "manufacturer": "Corellian Engineering Corporation",
                "cost_in_credits": "100000",
                "length": "34.37",
                "max_atmosphering_speed": "1050",
                "crew": "4",
                "passengers": "6",
                "cargo_capacity": "100000",
                "consumables": "2 months",
                "hyperdrive_rating": "0.5",
                "MGLT": "75",
                "starship_class": "Light freighter",
                "pilots": [
                    "https://swapi.dev/api/people/13/",
                    "https://swapi.dev/api/people/14/",
                ],
                "films": [
                    "https://swapi.dev/api/films/1/",
                ],
                "created": "2014-12-10T16:59:45.094000Z",
                "edited": "2014-12-20T21:23:49.880000Z",
                "url": "https://swapi.dev/api/starships/10/",
            }
        ],
    }


@pytest.fixture
def planets_api_response() -> dict[str, Any]:
    """Mock API response for planets resource."""
    return {
        "count": 1,
        "results": [
            {
                "name": "Tatooine",
                "rotation_period": "23",
                "orbital_period": "304",
                "diameter": "10465",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "surface_water": "1",
                "population": "200000",
                "residents": [
                    "https://swapi.dev/api/people/1/",
                ],
                "films": [
                    "https://swapi.dev/api/films/1/",
                ],
                "created": "2014-12-09T13:50:49.641000Z",
                "edited": "2014-12-20T20:58:18.411000Z",
                "url": "https://swapi.dev/api/planets/1/",
            }
        ],
    }
