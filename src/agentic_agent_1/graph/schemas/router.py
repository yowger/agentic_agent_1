from typing import Literal
from pydantic import BaseModel, Field

from agentic_agent_1.graph.schemas.metadata_filter import MetadataFilter

Routes = list[Literal["retrieve", "nutrition_api", "out_of_scope"]]


class RouteQuery(BaseModel):
    routes: Routes = Field(
        min_length=1,
        description=(
            "The sources needed to answer the user's question. "
            "Choose retrieve, nutrition_api, or both."
        ),
    )
    metadata_filter: MetadataFilter
