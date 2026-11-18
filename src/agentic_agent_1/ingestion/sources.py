from typing import TypedDict, NotRequired, Literal


class SourceMetaData(TypedDict):
    title: str
    organization: str
    document_type: Literal["guideline", "fact_sheet",  "joint_statement"]
    topic: str
    language: str
    publication_year: int


class ChunkingConfig(TypedDict, total=False):
    chunk_size: int
    chunk_overlap: int


class PDFSource(TypedDict):
    filename: str
    metadata: SourceMetaData
    chunking_config: NotRequired[ChunkingConfig]


DEFAULT_CHUNKING: ChunkingConfig = {
    "chunk_size": 1000,
    "chunk_overlap": 200
}


PDF_SOURCES: list[PDFSource] = [
    {
        "filename": "carb_intake_all_ages_eng.pdf",
        "metadata": {
            "title": "Carbohydrate intake for adults and children",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "Carbohydrates",
            "language": "en",
            "publication_year": 2023
        }
    },
    {
        "filename": "healthy_diet_fact_sheet_eng.pdf",
        "metadata": {
            "title": "Healthy diet",
            "organization": "WHO",
            "document_type": "fact_sheet",
            "topic": "Healthy_diet",
            "language": "en",
            "publication_year": 2018
        }
    },
    {
        "filename": "healthy_diet_fact_sheet_eng.pdf",
        "metadata": {
            "title": "What are healthy diets?",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "What are healthy diets?",
            "language": "en",
            "publication_year": 2024
        }
    },
    {
        "filename": "sat_trans_fat_all_ages_eng.pdf",
        "metadata": {
            "title": "Saturated fatty acid  and trans-fatty acid intake for adults and children",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "dietary_facts",
            "language": "en",
            "publication_year": 2023
        }
    },
    {
        "filename": "sodium_intake_all_ages_eng.pdf",
        "metadata": {
            "title": "Sodium intake for adults and children",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "sodium",
            "language": "en",
            "publication_year": 2012
        }
    },
    {
        "filename": "sugars_intake_all_ages_eng.pdf",
        "metadata": {
            "title": "Sugars intake for adults and children",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "Sugars",
            "language": "en",
            "publication_year": 2015
        }
    },
    {
        "filename": "total_fat_all_ages_eng.pdf",
        "metadata": {
            "title": "Total fat intake for the prevention of unhealthy weight gain in adults and children",
            "organization": "WHO",
            "document_type": "guideline",
            "topic": "dietary_facts",
            "language": "en",
            "publication_year": 2023
        }
    },

]
