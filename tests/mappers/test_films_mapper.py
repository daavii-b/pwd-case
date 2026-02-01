from typing import Any

import pytest

from mappers.films_mapper import FilmsMapper


class TestFilmsMapper:
    sut = FilmsMapper
    api_response: dict[str, Any]

    @pytest.fixture(autouse=True)
    def setup(self, api_response: dict[str, Any]) -> None:
        self.api_response = api_response

    def test_should_raise_type_error_when_call_to_domain_method_with_a_not_dict_value(
        self,
    ):
        with pytest.raises(TypeError):
            self.sut.to_external(["not", "a", "dict"])  # type: ignore

    def test_should_raise_type_error_when_call_to_external_method_with_a_not_dict_value(
        self,
    ):
        with pytest.raises(TypeError):
            self.sut.to_external(["not", "a", "dict"])  # type: ignore

    def test_should_have_to_external_static_method(self):
        assert hasattr(self.sut, "to_external")
        assert callable(self.sut.to_external)

    def test_should_have_to_domain_static_method(self):
        assert hasattr(self.sut, "to_domain")
        assert callable(self.sut.to_domain)

    def test_should_covert_people_external_schema_to_people_schema(self):
        external_schema = self.sut.to_external(self.api_response)

        result = self.sut.to_domain(external_schema)

        assert result.title == self.api_response["title"]
        assert result.episode_id == self.api_response["episode_id"]
        assert result.opening_crawl == self.api_response["opening_crawl"]
        assert result.director == self.api_response["director"]
        assert result.producer == self.api_response["producer"]
        assert result.release_date == self.api_response["release_date"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_convert_api_response_to_people_external_schema(self):
        result = self.sut.to_external(self.api_response)

        assert result.title == self.api_response["title"]
        assert result.episode_id == self.api_response["episode_id"]
        assert result.opening_crawl == self.api_response["opening_crawl"]
        assert result.director == self.api_response["director"]
        assert result.producer == self.api_response["producer"]
        assert result.release_date == self.api_response["release_date"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_ignore_extra_fields_in_api_response(self):
        result = self.sut.to_external(self.api_response)

        assert not hasattr(result, "films")
        assert not hasattr(result, "homeworld")
        assert not hasattr(result, "unknown_field")


@pytest.fixture()
def api_response() -> dict[str, Any]:
    return {
        "title": "A New Hope",
        "episode_id": 4,
        "opening_crawl": "It is a period of civil war....",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25",
        "created": "2014-12-10T14:23:31.880000Z",
        "edited": "2014-12-20T19:49:45.256000Z",
    }
