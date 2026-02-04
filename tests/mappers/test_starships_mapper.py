from typing import Any

import pytest

from mappers.starships_mapper import StarshipsMapper


class TestStarshipMapper:
    sut = StarshipsMapper
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

        assert result.cargo_capacity == self.api_response["cargo_capacity"]
        assert result.cost_in_credits == self.api_response["cost_in_credits"]
        assert result.crew == self.api_response["crew"]
        assert result.consumables == self.api_response["consumables"]
        assert result.hyperdrive_rating == self.api_response["hyperdrive_rating"]
        assert result.manufacturer == self.api_response["manufacturer"]
        assert result.length == self.api_response["length"]
        assert result.name == self.api_response["name"]
        assert result.starship_class == self.api_response["starship_class"]
        assert result.model == self.api_response["model"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_convert_api_response_to_people_external_schema(self):
        result = self.sut.to_external(self.api_response)

        assert result.cargo_capacity == self.api_response["cargo_capacity"]
        assert result.cost_in_credits == self.api_response["cost_in_credits"]
        assert result.crew == self.api_response["crew"]
        assert result.consumables == self.api_response["consumables"]
        assert result.hyperdrive_rating == self.api_response["hyperdrive_rating"]
        assert result.manufacturer == self.api_response["manufacturer"]
        assert result.length == self.api_response["length"]
        assert result.name == self.api_response["name"]
        assert result.starship_class == self.api_response["starship_class"]
        assert result.model == self.api_response["model"]
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
        "cargo_capacity": "1000000000000",
        "consumables": "3 years",
        "cost_in_credits": "1000000000000",
        "crew": "342953",
        "edited": "2014-12-10T16:36:50.509000Z",
        "created": "2014-12-10T16:36:50.509000Z",
        "hyperdrive_rating": "4.0",
        "length": "120000",
        "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
        "max_atmosphering_speed": "n/a",
        "model": "DS-1 Orbital Battle Station",
        "name": "Death Star",
        "starship_class": "Deep Space Mobile Battlestation",
    }
