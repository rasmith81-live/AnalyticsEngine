"""SQLAlchemy model for metadata_relationships table."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Index, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB

import sys
from pathlib import Path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.base_models import Base


class MetadataRelationship(Base):
    """Metadata relationships table (hypertable).
    
    Stores knowledge graph edges between entities.
    Optimized for graph traversal queries.
    """
    
    __tablename__ = "metadata_relationships"
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    from_entity_code = Column(String(255), nullable=False, index=True)
    to_entity_code = Column(String(255), nullable=False, index=True)
    relationship_type = Column(String(100), nullable=False, index=True)
    from_cardinality = Column(String(20))
    to_cardinality = Column(String(20))
    metadata_ = Column("metadata", JSONB)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    is_active = Column(Boolean, default=True, index=True)
    
    __table_args__ = (
        Index('idx_rel_from_active', 'from_entity_code', postgresql_where=(is_active == True)),
        Index('idx_rel_to_active', 'to_entity_code', postgresql_where=(is_active == True)),
        Index('idx_rel_type_active', 'relationship_type', postgresql_where=(is_active == True)),
    )
    
    def __repr__(self):
        return f"<MetadataRelationship({self.from_entity_code} --{self.relationship_type}--> {self.to_entity_code})>"
