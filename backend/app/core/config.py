from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    app_name: str = "AI Document Intelligence Assistant"
    api_v1_prefix: str = "/api/v1"
    database_url: str = (
        "postgresql+psycopg://document_intelligence:change-me@postgres:5432/"
        "document_intelligence"
    )
    postgres_host: str | None = None
    postgres_port: int = 5432
    postgres_db: str | None = None
    postgres_user: str | None = None
    postgres_password: str | None = None
    embedding_dimensions: int = 1536

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def resolved_database_url(self) -> str:
        """Create a safe SQLAlchemy URL when discrete PostgreSQL settings are set."""
        if all((self.postgres_db, self.postgres_user, self.postgres_password)):
            return URL.create(
                "postgresql+psycopg",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host or "localhost",
                port=self.postgres_port,
                database=self.postgres_db,
            ).render_as_string(hide_password=False)
        return self.database_url


settings = Settings()
