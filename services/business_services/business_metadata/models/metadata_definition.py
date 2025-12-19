"""SQLAlchemy model for metadata_definitions table."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Integer, Boolean, Index, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB

import sys
from pathlib import Path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.base_models import Base


class MetadataDefinition(Base):
    """Main metadata storage table (hypertable).
    
    Stores all ontology objects (entities, metrics, value chains, etc.)
    as JSONB with polymorphic discrimination via 'kind' field.
    """
    
    __tablename__ = "metadata_definitions"
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    kind = Column(String(100), nullable=False, index=True)
    code = Column(String(255), nullable=False, index=True)
    name = Column(String(500), nullable=False)
    version = Column(Integer, nullable=False, default=1)
    data = Column(JSONB, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(String(255))
    is_active = Column(Boolean, default=True, index=True)
    metadata_hash = Column(String(64))
    
    __table_args__ = (
        Index('idx_metadata_kind_active', 'kind', postgresql_where=(is_active == True)),
        Index('idx_metadata_code_active', 'code', postgresql_where=(is_active == True)),
        Index('idx_metadata_data_gin', 'data', postgresql_using='gin'),
    )
    
    def __repr__(self):
        return f"<MetadataDefinition(code='{self.code}', kind='{self.kind}', version={self.version})>"
