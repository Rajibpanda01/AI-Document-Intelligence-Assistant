
"""pgvector similarity-search helpers."""

from collections.abc import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.storage.models import DocumentChunk


def search_similar_chunks(
    session: Session,
    query_embedding: Sequence[float],
    *,
    limit: int = 5,
    document_ids: Sequence[UUID] | None = None,
) -> list[DocumentChunk]:
    """Return chunks ranked by cosine distance (lower is more similar)."""
    if len(query_embedding) != settings.embedding_dimensions:
        raise ValueError(
            f"Expected {settings.embedding_dimensions} embedding dimensions, "
            f"received {len(query_embedding)}."
        )
    if limit < 1:
        raise ValueError("limit must be at least 1")

    distance = DocumentChunk.embedding.cosine_distance(list(query_embedding))
    statement = select(DocumentChunk).order_by(distance).limit(limit)
    if document_ids:
        statement = statement.where(DocumentChunk.document_id.in_(document_ids))

    return list(session.scalars(statement))
