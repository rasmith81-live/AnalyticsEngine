"""SQLAlchemy model for metadata_relationships table."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Index, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from sqlalchemy.orm import relationship

import sys
from pathlib import Path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.base_models import Base


class MetadataRelationship(Base):
    """Metadata relationships table (hypertable).
    
    Stores knowledge graph edges between entities.
    Optimized for graph traversal queries.
    
    Uses both UUID references (from_entity_id, to_entity_id) and 
    code-based references (from_entity_code, to_entity_code) for flexibility.
    UUID references are preferred for integrity; codes are kept for backward compatibility.
    """
    
    __tablename__ = "metadata_relationships"
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    # UUID-based references (preferred)
    from_entity_id = Column(PG_UUID(as_uuid=True), ForeignKey('metadata_definitions.id'), nullable=True, index=True)
    to_entity_id = Column(PG_UUID(as_uuid=True), ForeignKey('metadata_definitions.id'), nullable=True, index=True)
    # Code-based references (backward compatibility)
    from_entity_code = Column(String(255), nullable=False, index=True)
    to_entity_code = Column(String(255), nullable=False, index=True)
    relationship_type = Column(String(100), nullable=False, index=True)
    from_cardinality = Column(String(20))
    to_cardinality = Column(String(20))
    metadata_ = Column("metadata", JSONB)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    is_active = Column(Boolean, default=True, index=True)
    
    # Relationships to MetadataDefinition
    from_entity = relationship("MetadataDefinition", foreign_keys=[from_entity_id], lazy="joined")
    to_entity = relationship("MetadataDefinition", foreign_keys=[to_entity_id], lazy="joined")
    
    __table_args__ = (
        Index('idx_rel_from_active', 'from_entity_code', postgresql_where=(is_active == True)),
        Index('idx_rel_to_active', 'to_entity_code', postgresql_where=(is_active == True)),
        Index('idx_rel_type_active', 'relationship_type', postgresql_where=(is_active == True)),
    )
    
    def __repr__(self):
        return f"<MetadataRelationship({self.from_entity_code} --{self.relationship_type}--> {self.to_entity_code})>"
