from typing import Any

from schemas.people_schema import PeopleExternalSchema, PeopleSchema


class PeopleMapper:
    @staticmethod
    def to_external(api_response: dict[str, Any]) -> PeopleExternalSchema:
        return PeopleExternalSchema(**api_response)

    @staticmethod
    def to_domain(external_schema: PeopleExternalSchema) -> PeopleSchema:
        return PeopleSchema(
            birth_year=external_schema.birth_year,
            eye_color=external_schema.eye_color,
            gender=external_schema.gender,
            hair_color=external_schema.hair_color,
            height=external_schema.height,
            mass=external_schema.mass,
            created_at=external_schema.created_at,
            edited_at=external_schema.edited_at,
            skin_color=external_schema.skin_color,
            name=external_schema.name,
            links={},
        )
