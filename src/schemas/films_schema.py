from pydantic import BaseModel, Field


class FilmsExternalSchema(BaseModel):
    title: str = Field(alias="title")
    episode_id: int = Field(alias="episode_id")
    opening_crawl: str = Field(alias="opening_crawl")
    director: str = Field(alias="director")
    producer: str = Field(alias="producer")
    release_date: str = Field(alias="release_date")
    created_at: str = Field(alias="created")
    edited_at: str = Field(alias="edited")

    model_config = {"extra": "ignore"}


class FilmsSchema(BaseModel):
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date: str
    created_at: str
    edited_at: str
    links: dict[str, dict[str, list[str]]]
