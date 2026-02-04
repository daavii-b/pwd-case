from typing import Any

from pydantic import BaseModel


class ListResponseModel(BaseModel):
    data: list[dict[str, Any]]

    model_config = {
        "json_schema_extra": {
            "examples": [{"data": [{"field_a": "value", "field_b": 123}]}]
        }
    }
