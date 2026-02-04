from typing import Any

from schemas.starships_schema import StarshipsExternalSchema, StarshipsSchema


class StarshipsMapper:
    @staticmethod
    def to_external(api_response: dict[str, Any]) -> StarshipsExternalSchema:
        return StarshipsExternalSchema(**api_response)

    @staticmethod
    def to_domain(external_schema: StarshipsExternalSchema) -> StarshipsSchema:
        return StarshipsSchema(
            consumables=external_schema.consumables,
            cost_in_credits=external_schema.cost_in_credits,
            crew=external_schema.crew,
            hyperdrive_rating=external_schema.hyperdrive_rating,
            length=external_schema.length,
            manufacturer=external_schema.manufacturer,
            name=external_schema.name,
            max_atmosphering_speed=external_schema.max_atmosphering_speed,
            model=external_schema.model,
            starship_class=external_schema.starship_class,
            cargo_capacity=external_schema.cargo_capacity,
            created_at=external_schema.created_at,
            edited_at=external_schema.edited_at,
            links={},
        )
