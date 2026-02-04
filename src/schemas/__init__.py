from .films_schema import FilmsExternalSchema
from .people_schema import PeopleExternalSchema
from .planets_schema import PlanetsExternalSchema
from .response_schema import PaginationResponseSchema
from .starships_schema import StarshipsExternalSchema

__all__ = [
    "FilmsExternalSchema",
    "PaginationResponseSchema",
    "PeopleExternalSchema",
    "PlanetsExternalSchema",
    "StarshipsExternalSchema",
]
