
"""SQLAlchemy engine, sessions, and schema initialization."""

from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    """Base class for all persistent application models."""


engine = create_engine(settings.resolved_database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator[Session, None, None]:
    """Provide a database session to FastAPI request handlers."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def initialize_database() -> None:
    """Enable pgvector and create the initial application tables."""
    # Import here so every model has registered itself with Base.metadata.
    from app.storage import models  # noqa: F401

    with engine.begin() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        Base.metadata.create_all(connection)
