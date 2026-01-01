"""
Client Configuration Database Models for Conversation Service.

These models store client-specific value chains, intents, entities, and models
that are separate from the metadata service's ontology entities.
"""

import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any

from sqlalchemy import (
    Column, DateTime, Integer, String, Text, Float, Boolean,
    ForeignKey, Index, JSON, func
)
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    """Base class for all SQLAlchemy models."""
    pass


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


class ClientConfiguration(Base, TimestampMixin):
    """
    Client Configuration - Top-level container for a client's conversation-derived configuration.
    
    This stores the complete configuration extracted from conversation sessions,
    including value chains, intents, entities, and models.
    """
    __tablename__ = 'client_configurations'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # Client identification
    client_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    client_name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    # Configuration metadata
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0", nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="draft", nullable=False)  # draft, active, archived
    
    # Source session info
    source_session_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    
    # Relationships
    recordings: Mapped[List["ClientRecording"]] = relationship(back_populates="configuration", cascade="all, delete-orphan")
    intents: Mapped[List["ClientIntent"]] = relationship(back_populates="configuration", cascade="all, delete-orphan")
    entities: Mapped[List["ClientEntity"]] = relationship(back_populates="configuration", cascade="all, delete-orphan")
    value_chain_models: Mapped[List["ClientValueChainModel"]] = relationship(back_populates="configuration", cascade="all, delete-orphan")
    
    __table_args__ = (
        Index('ix_client_config_client_id', 'client_id'),
        Index('ix_client_config_status', 'status'),
    )


class ClientRecording(Base, TimestampMixin):
    """
    Client Recording - Stores conversation recordings/transcripts.
    """
    __tablename__ = 'client_recordings'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # Foreign key to configuration
    configuration_id: Mapped[int] = mapped_column(Integer, ForeignKey('client_configurations.id'), nullable=False)
    configuration: Mapped["ClientConfiguration"] = relationship(back_populates="recordings")
    
    # Recording data
    session_id: Mapped[str] = mapped_column(String(255), nullable=False)
    transcript: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Metadata
    duration_seconds: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    speaker_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    
    # Segments as JSON array
    segments: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True)
    
    __table_args__ = (
        Index('ix_client_recording_session', 'session_id'),
        Index('ix_client_recording_config', 'configuration_id'),
    )


class ClientIntent(Base, TimestampMixin):
    """
    Client Intent - Business intents extracted from conversations.
    
    These are client-specific intents, separate from the metadata ontology.
    """
    __tablename__ = 'client_intents'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # Foreign key to configuration
    configuration_id: Mapped[int] = mapped_column(Integer, ForeignKey('client_configurations.id'), nullable=False)
    configuration: Mapped["ClientConfiguration"] = relationship(back_populates="intents")
    
    # Intent data
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confidence: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    
    # Domain and categorization
    domain: Mapped[str] = mapped_column(String(100), default="general", nullable=False)
    category: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    # Related entities and metrics (stored as arrays)
    target_entities: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), nullable=True)
    requested_metrics: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String), nullable=True)
    
    # Parameters as JSON
    parameters: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True)
    
    # Source tracking
    source_utterance: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    __table_args__ = (
        Index('ix_client_intent_config', 'configuration_id'),
        Index('ix_client_intent_name', 'name'),
        Index('ix_client_intent_domain', 'domain'),
    )


class ClientEntity(Base, TimestampMixin):
    """
    Client Entity - Business entities extracted from conversations.
    
    These are client-specific entities (e.g., "Customer", "Order", "Product")
    that form the client's value chain vocabulary.
    """
    __tablename__ = 'client_entities'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # Foreign key to configuration
    configuration_id: Mapped[int] = mapped_column(Integer, ForeignKey('client_configurations.id'), nullable=False)
    configuration: Mapped["ClientConfiguration"] = relationship(back_populates="entities")
    
    # Entity data
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    entity_type: Mapped[str] = mapped_column(String(100), nullable=False)  # e.g., "Process", "Activity", "Metric", "Object"
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    # Properties as JSON
    properties: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True)
    
    # Relationships to other entities (stored as JSON array of entity UUIDs)
    related_entities: Mapped[Optional[Dict]] = mapped_column(JSONB, nullable=True)
    
    # Extraction metadata
    extraction_confidence: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    source_context: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    __table_args__ = (
        Index('ix_client_entity_config', 'configuration_id'),
        Index('ix_client_entity_name', 'name'),
        Index('ix_client_entity_type', 'entity_type'),
    )


class ClientValueChainModel(Base, TimestampMixin):
    """
    Client Value Chain Model - Complete value chain model derived from conversations.
    
    This stores the full value chain structure with nodes and links,
    separate from the metadata service's value chains.
    """
    __tablename__ = 'client_value_chain_models'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    
    # Foreign key to configuration
    configuration_id: Mapped[int] = mapped_column(Integer, ForeignKey('client_configurations.id'), nullable=False)
    configuration: Mapped["ClientConfiguration"] = relationship(back_populates="value_chain_models")
    
    # Model metadata
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    version: Mapped[str] = mapped_column(String(50), default="1.0", nullable=False)
    
    # Model structure stored as JSON
    # nodes: [{id, name, type, description, properties}]
    nodes: Mapped[Dict] = mapped_column(JSONB, nullable=False, default=list)
    
    # links: [{source_id, target_id, type}]
    links: Mapped[Dict] = mapped_column(JSONB, nullable=False, default=list)
    
    # Model status
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    # Generation metadata
    generated_from_session: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    generation_method: Mapped[str] = mapped_column(String(100), default="llm", nullable=False)
    
    __table_args__ = (
        Index('ix_client_vcm_config', 'configuration_id'),
        Index('ix_client_vcm_name', 'name'),
        Index('ix_client_vcm_active', 'is_active'),
    )
