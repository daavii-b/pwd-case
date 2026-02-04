from typing import Any

import pytest

from mappers.planets_mapper import PlanetsMapper


class TestPlanetsMapper:
    sut = PlanetsMapper
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

        assert result.climate == self.api_response["climate"]
        assert result.diameter == self.api_response["diameter"]
        assert result.gravity == self.api_response["gravity"]
        assert result.orbital_period == self.api_response["orbital_period"]
        assert result.population == self.api_response["population"]
        assert result.rotation_period == self.api_response["rotation_period"]
        assert result.surface_water == self.api_response["surface_water"]
        assert result.terrain == self.api_response["terrain"]
        assert result.created_at == self.api_response["created"]
        assert result.edited_at == self.api_response["edited"]

    def test_should_convert_api_response_to_people_external_schema(self):
        result = self.sut.to_external(self.api_response)

        assert result.climate == self.api_response["climate"]
        assert result.diameter == self.api_response["diameter"]
        assert result.gravity == self.api_response["gravity"]
        assert result.orbital_period == self.api_response["orbital_period"]
        assert result.population == self.api_response["population"]
        assert result.rotation_period == self.api_response["rotation_period"]
        assert result.surface_water == self.api_response["surface_water"]
        assert result.terrain == self.api_response["terrain"]
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
        "climate": "Arid",
        "created": "2014-12-09T13:50:49.641000Z",
        "diameter": "10465",
        "edited": "2014-12-15T13:48:16.167217Z",
        "gravity": "1",
        "name": "Tatooine",
        "orbital_period": "304",
        "population": "120000",
        "rotation_period": "23",
        "surface_water": "1",
        "terrain": "Dessert",
    }
