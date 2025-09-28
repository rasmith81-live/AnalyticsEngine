"""
Base Models - Consolidated database models from common directory.
"""

import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, TypeVar, Generic

from sqlalchemy import Column, DateTime, Integer, String, func, Text, Index, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

T = TypeVar('T')

class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Generate __tablename__ automatically from class name."""
        return cls.__name__.lower()

class TimestampMixin:
    """Mixin for created_at and updated_at columns."""
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

class IdMixin:
    """Mixin for id column."""
    
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

class UUIDMixin:
    """Mixin for UUID column."""
    
    uuid: Mapped[str] = mapped_column(
        String(36),
        default=lambda: str(uuid.uuid4()),
        nullable=False,
        unique=True
    )

class BaseModel(Base, IdMixin, TimestampMixin, UUIDMixin):
    """Base model with ID, UUID, and timestamps."""
    
    __abstract__ = True


class CommandBase:
    """Base class for CQRS commands."""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert command to dictionary."""
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }

class ReadBase(Generic[T]):
    """Base class for CQRS read models."""
    
    def __init__(self, entity: T):
        """Initialize read model from entity."""
        self._entity = entity
        
    @property
    def id(self) -> int:
        """Get entity ID."""
        return self._entity.id
    
    @property
    def uuid(self) -> str:
        """Get entity UUID."""
        return self._entity.uuid
    
    @property
    def created_at(self) -> datetime:
        """Get entity creation timestamp."""
        return self._entity.created_at
    
    @property
    def updated_at(self) -> datetime:
        """Get entity update timestamp."""
        return self._entity.updated_at
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert read model to dictionary."""
        result = {
            'id': self.id,
            'uuid': self.uuid,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
        
        # Add all public attributes
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                if isinstance(value, datetime):
                    result[key] = value.isoformat()
                else:
                    result[key] = value
                    
        return result
    
    @classmethod
    def from_entities(cls, entities: List[T]) -> List['ReadBase[T]']:
        """Create read models from entities."""
        return [cls(entity) for entity in entities]

class MarketData(BaseModel):
    __tablename__ = 'market_data'

    symbol: Mapped[str] = mapped_column(String(10), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    volume: Mapped[int] = mapped_column(Integer, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    __table_args__ = (Index('ix_market_data_timestamp', 'timestamp'),)


class NewsArticle(BaseModel):
    __tablename__ = 'news_articles'

    source: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    published_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    related_tickers: Mapped[List[str]] = mapped_column(ARRAY(String), nullable=True)
    article_type: Mapped[str] = mapped_column(String(255), nullable=True)
    sentiment: Mapped[float] = mapped_column(Float, nullable=True)

    __table_args__ = (Index('ix_news_articles_published_at', 'published_at'),)

