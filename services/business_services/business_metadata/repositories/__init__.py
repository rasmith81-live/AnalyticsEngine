"""Repository layer for metadata CRUD operations (CQRS pattern)."""

from .metadata_write_repository import MetadataWriteRepository
from .metadata_query_repository import MetadataQueryRepository

__all__ = [
    "MetadataWriteRepository",
    "MetadataQueryRepository",
]
