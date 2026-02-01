from typing import Any

from schemas.films_schema import FilmsExternalSchema, FilmsSchema


class FilmsMapper:
    @staticmethod
    def to_external(api_response: dict[str, Any]) -> FilmsExternalSchema:
        return FilmsExternalSchema(**api_response)

    @staticmethod
    def to_domain(external_schema: FilmsExternalSchema) -> FilmsSchema:
        return FilmsSchema(
            title=external_schema.title,
            episode_id=external_schema.episode_id,
            opening_crawl=external_schema.opening_crawl,
            director=external_schema.director,
            producer=external_schema.producer,
            release_date=external_schema.release_date,
            created_at=external_schema.created_at,
            edited_at=external_schema.edited_at,
            links={},
        )
