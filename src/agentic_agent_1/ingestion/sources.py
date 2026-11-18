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
    source_id: str
    filename: str
    metadata: SourceMetaData
    chunking_config: NotRequired[ChunkingConfig]


DEFAULT_CHUNKING: ChunkingConfig = {
    "chunk_size": 1500,
    "chunk_overlap": 200
}


PDF_SOURCES: list[PDFSource] = [
    {
        "source_id": "who_carbohydrate_intake_adults_children_2023",
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
        "source_id": "who_healthy_diet_fact_sheet_2018",
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
        "source_id": "who_healthy_diets_2024",
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
        "source_id": "who_saturated_trans_fat_intake_2023",
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
        "source_id": "who_sodium_intake_adults_children_2012",
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
        "source_id": "who_sugars_intake_adults_children_2015",
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
        "source_id": "who_total_fat_intake_unhealthy_weight_gain_2023",
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
