from pydantic import BaseModel, ConfigDict, Field


class StarshipsExternalSchema(BaseModel):
    consumables: str = Field(alias="consumables")
    cost_in_credits: str = Field(alias="cost_in_credits")
    crew: str = Field(alias="crew")
    hyperdrive_rating: str = Field(alias="hyperdrive_rating")
    length: str = Field(alias="length")
    cargo_capacity: str = Field(alias="cargo_capacity")
    manufacturer: str = Field(alias="manufacturer")
    max_atmosphering_speed: str = Field(alias="max_atmosphering_speed")
    model: str = Field(alias="model")
    name: str = Field(alias="name")
    starship_class: str = Field(alias="starship_class")
    created_at: str = Field(alias="created")
    edited_at: str = Field(alias="edited")

    model_config = ConfigDict(extra="ignore")


class StarshipsSchema(BaseModel):
    consumables: str
    cost_in_credits: str
    crew: str
    hyperdrive_rating: str
    length: str
    cargo_capacity: str
    manufacturer: str
    max_atmosphering_speed: str
    model: str
    name: str
    starship_class: str
    created_at: str
    edited_at: str
    links: dict[str, dict[str, list[str]]]
