from pydantic import BaseModel, Field


class PeopleExternalSchema(BaseModel):
    birth_year: str = Field(alias="birth_year")
    eye_color: str = Field(alias="eye_color")
    gender: str = Field(alias="gender")
    hair_color: str = Field(alias="hair_color")
    height: str = Field(alias="height")
    mass: str = Field(alias="mass")
    name: str = Field(alias="name")
    skin_color: str = Field(alias="skin_color")
    created_at: str = Field(alias="created")
    edited_at: str = Field(alias="edited")

    model_config = {"extra": "ignore"}


class PeopleSchema(BaseModel):
    birth_year: str
    eye_color: str
    gender: str
    hair_color: str
    height: str
    mass: str
    name: str
    skin_color: str
    created_at: str
    edited_at: str
    links: dict[str, dict[str, list[str]]]
