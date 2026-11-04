from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Document Intelligence Assistant"
    api_v1_prefix: str = "/api/v1"
    database_url: str = (
        "postgresql+psycopg://document_intelligence:change-me@postgres:5432/"
        "document_intelligence"
    )
    embedding_dimensions: int = 1536

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
