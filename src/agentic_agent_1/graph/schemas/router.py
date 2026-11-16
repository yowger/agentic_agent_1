from typing import Literal
from pydantic import BaseModel, Field

Routes = list[Literal["retrieve", "nutrition_api"]]


class RouteDecision(BaseModel):
    routes: Routes = Field(
        min_length=1,
        description=(
            "The sources needed to answer the user's question. "
            "Choose retrieve, nutrition_api, or both."
        )
    )
