"""SQLAlchemy model for metadata_versions table."""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Integer, Text, Index, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB

import sys
from pathlib import Path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.base_models import Base


class MetadataVersion(Base):
    """Metadata version history table (hypertable).
    
    Tracks all changes to metadata definitions for audit trail
    and time-travel queries.
    """
    
    __tablename__ = "metadata_versions"
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    definition_code = Column(String(255), nullable=False, index=True)
    definition_kind = Column(String(100), nullable=False, index=True)
    version = Column(Integer, nullable=False)
    data = Column(JSONB, nullable=False)
    change_type = Column(String(50), nullable=False)  # "created", "updated", "deleted"
    changed_by = Column(String(255))
    changed_at = Column(TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)
    change_description = Column(Text)
    
    __table_args__ = (
        Index('idx_version_code_kind', 'definition_code', 'definition_kind'),
    )
    
    def __repr__(self):
        return f"<MetadataVersion(code='{self.definition_code}', kind='{self.definition_kind}', v{self.version}, {self.change_type})>"
