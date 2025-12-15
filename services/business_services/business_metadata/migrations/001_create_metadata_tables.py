"""Create metadata tables for business_metadata service.

This migration will be executed by the database_service's migration_manager.

Revision ID: bm_001
Revises: 
Create Date: 2025-12-06 10:20:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB, TIMESTAMPTZ

# revision identifiers
revision = 'bm_001'
down_revision = None
branch_labels = ('business_metadata',)
depends_on = None


def upgrade() -> None:
    """Create metadata storage tables."""
    
    # Main metadata definitions table
    op.create_table(
        'metadata_definitions',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('kind', sa.String(100), nullable=False),
        sa.Column('code', sa.String(255), nullable=False),
        sa.Column('name', sa.String(500), nullable=False),
        sa.Column('version', sa.Integer, nullable=False, server_default='1'),
        sa.Column('data', JSONB, nullable=False),
        sa.Column('created_at', TIMESTAMPTZ, nullable=False, server_default=sa.text('NOW()')),
        sa.Column('updated_at', TIMESTAMPTZ, nullable=False, server_default=sa.text('NOW()')),
        sa.Column('created_by', sa.String(255)),
        sa.Column('is_active', sa.Boolean, server_default='true'),
        sa.Column('metadata_hash', sa.String(64)),
        sa.UniqueConstraint('code', 'kind', 'version', name='uq_metadata_code_kind_version'),
    )
    
    # Convert to hypertable (TimescaleDB)
    op.execute("""
        SELECT create_hypertable('metadata_definitions', 'created_at',
            chunk_time_interval => INTERVAL '1 month',
            if_not_exists => TRUE
        );
    """)
    
    # Indexes
    op.create_index(
        'idx_metadata_kind',
        'metadata_definitions',
        ['kind']
    )
    
    op.create_index(
        'idx_metadata_code',
        'metadata_definitions',
        ['code']
    )
    
    op.create_index(
        'idx_metadata_kind_active',
        'metadata_definitions',
        ['kind'],
        postgresql_where=sa.text('is_active = true')
    )
    
    op.create_index(
        'idx_metadata_code_active',
        'metadata_definitions',
        ['code'],
        postgresql_where=sa.text('is_active = true')
    )
    
    op.create_index(
        'idx_metadata_data_gin',
        'metadata_definitions',
        ['data'],
        postgresql_using='gin'
    )
    
    # Metadata relationships table
    op.create_table(
        'metadata_relationships',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('from_entity_code', sa.String(255), nullable=False),
        sa.Column('to_entity_code', sa.String(255), nullable=False),
        sa.Column('relationship_type', sa.String(100), nullable=False),
        sa.Column('from_cardinality', sa.String(20)),
        sa.Column('to_cardinality', sa.String(20)),
        sa.Column('metadata', JSONB),
        sa.Column('created_at', TIMESTAMPTZ, nullable=False, server_default=sa.text('NOW()')),
        sa.Column('is_active', sa.Boolean, server_default='true'),
        sa.UniqueConstraint('from_entity_code', 'to_entity_code', 'relationship_type', 
                          name='uq_relationship'),
    )
    
    # Convert to hypertable
    op.execute("""
        SELECT create_hypertable('metadata_relationships', 'created_at',
            chunk_time_interval => INTERVAL '1 month',
            if_not_exists => TRUE
        );
    """)
    
    # Relationship indexes
    op.create_index(
        'idx_rel_from',
        'metadata_relationships',
        ['from_entity_code']
    )
    
    op.create_index(
        'idx_rel_to',
        'metadata_relationships',
        ['to_entity_code']
    )
    
    op.create_index(
        'idx_rel_type',
        'metadata_relationships',
        ['relationship_type']
    )
    
    op.create_index(
        'idx_rel_from_active',
        'metadata_relationships',
        ['from_entity_code'],
        postgresql_where=sa.text('is_active = true')
    )
    
    op.create_index(
        'idx_rel_to_active',
        'metadata_relationships',
        ['to_entity_code'],
        postgresql_where=sa.text('is_active = true')
    )
    
    op.create_index(
        'idx_rel_type_active',
        'metadata_relationships',
        ['relationship_type'],
        postgresql_where=sa.text('is_active = true')
    )
    
    # Version history table
    op.create_table(
        'metadata_versions',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('definition_code', sa.String(255), nullable=False),
        sa.Column('definition_kind', sa.String(100), nullable=False),
        sa.Column('version', sa.Integer, nullable=False),
        sa.Column('data', JSONB, nullable=False),
        sa.Column('change_type', sa.String(50), nullable=False),
        sa.Column('changed_by', sa.String(255)),
        sa.Column('changed_at', TIMESTAMPTZ, nullable=False, server_default=sa.text('NOW()')),
        sa.Column('change_description', sa.Text),
    )
    
    # Convert to hypertable
    op.execute("""
        SELECT create_hypertable('metadata_versions', 'changed_at',
            chunk_time_interval => INTERVAL '1 month',
            if_not_exists => TRUE
        );
    """)
    
    # Version history indexes
    op.create_index(
        'idx_version_code_kind',
        'metadata_versions',
        ['definition_code', 'definition_kind']
    )


def downgrade() -> None:
    """Drop metadata tables."""
    op.drop_table('metadata_versions')
    op.drop_table('metadata_relationships')
    op.drop_table('metadata_definitions')
