from pydantic import BaseModel, Field


class PlanetsExternalSchema(BaseModel):
    name: str = Field(alias="name")
    climate: str = Field(alias="climate")
    terrain: str = Field(alias="terrain")
    diameter: str = Field(alias="diameter")
    gravity: str = Field(alias="gravity")
    surface_water: str = Field(alias="surface_water")
    rotation_period: str = Field(alias="rotation_period")
    orbital_period: str = Field(alias="orbital_period")
    population: str = Field(alias="population")
    created_at: str = Field(alias="created")
    edited_at: str = Field(alias="edited")

    model_config = {"extra": "ignore"}


class PlanetsSchema(BaseModel):
    name: str
    climate: str
    terrain: str
    diameter: str
    gravity: str
    surface_water: str
    rotation_period: str
    orbital_period: str
    population: str
    created_at: str
    edited_at: str
