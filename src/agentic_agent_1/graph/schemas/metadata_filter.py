from pydantic import BaseModel, Field


class MetadataFilter(BaseModel):
    organization: str | None = Field(
        default=None,
        description="Organization explicitly mentioned in the question, such as WHO."
    )
    publication_year: int | None = Field(
        default=None,
        description="Publication year explicitly mentioned in the question."
    )
