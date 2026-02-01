from typing import Any

import pytest

from mappers.people_mapper import PeopleMapper


class TestPeopleMapper:
    sut = PeopleMapper
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

        assert result.birth_year == self.api_response["birth_year"]
        assert result.eye_color == self.api_response["eye_color"]
        assert result.gender == self.api_response["gender"]
        assert result.hair_color == self.api_response["hair_color"]
        assert result.height == self.api_response["height"]
        assert result.mass == self.api_response["mass"]
        assert result.name == self.api_response["name"]
        assert result.skin_color == self.api_response["skin_color"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_convert_api_response_to_people_external_schema(self):
        result = self.sut.to_external(self.api_response)

        assert result.birth_year == self.api_response["birth_year"]
        assert result.eye_color == self.api_response["eye_color"]
        assert result.gender == self.api_response["gender"]
        assert result.hair_color == self.api_response["hair_color"]
        assert result.height == self.api_response["height"]
        assert result.mass == self.api_response["mass"]
        assert result.name == self.api_response["name"]
        assert result.skin_color == self.api_response["skin_color"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_ignore_extra_fields_in_api_response(self):
        result = self.sut.to_external(self.api_response)

        assert not hasattr(result, "films")
        assert not hasattr(result, "homeworld")
        assert not hasattr(result, "unknown_field")


@pytest.fixture
def api_response() -> dict[str, Any]:
    return {
        "birth_year": "19 BBY",
        "eye_color": "Blue",
        "films": ["https://swapi.dev/api/films/1/"],
        "gender": "Male",
        "hair_color": "Blond",
        "height": "172",
        "homeworld": "https://swapi.dev/api/planets/1/",
        "mass": "77",
        "name": "Luke Skywalker",
        "skin_color": "Fair",
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-10T13:52:43.172000Z",
    }
