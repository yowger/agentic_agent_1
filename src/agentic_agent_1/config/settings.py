from pydantic_settings import BaseSettings, SettingsConfigDict

from agentic_agent_1.config.paths import ENV_DIR


class Settings(BaseSettings):
    OPENAI_API_KEY: str

    LLM_MODEL: str = "gpt-4o-mini"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    ROUTER_MODEL: str = "gpt-4o-mini"
    GENERATOR_MODEL: str = "gpt-4o-mini"

    COLLECTION_NAME: str = "nutrition_knowledge"

    model_config = SettingsConfigDict(
        env_file=ENV_DIR,
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
