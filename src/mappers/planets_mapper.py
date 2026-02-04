from typing import Any

from schemas.planets_schema import PlanetsExternalSchema, PlanetsSchema


class PlanetsMapper:
    @staticmethod
    def to_external(api_response: dict[str, Any]) -> PlanetsExternalSchema:
        return PlanetsExternalSchema(**api_response)

    @staticmethod
    def to_domain(external_schema: PlanetsExternalSchema) -> PlanetsSchema:
        return PlanetsSchema(
            climate=external_schema.climate,
            name=external_schema.name,
            terrain=external_schema.terrain,
            created_at=external_schema.created_at,
            edited_at=external_schema.edited_at,
            diameter=external_schema.edited_at,
            gravity=external_schema.gravity,
            population=external_schema.population,
            orbital_period=external_schema.orbital_period,
            rotation_period=external_schema.rotation_period,
            surface_water=external_schema.surface_water,
        )
