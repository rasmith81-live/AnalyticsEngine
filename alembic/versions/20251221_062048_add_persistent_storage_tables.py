"""add persistent storage tables

Revision ID: 20251221_062048
Revises: 
Create Date: 2025-12-21 06:20:48.000000

Description:
    Adds three tables for persistent storage of service data:
    - connector_profiles: Store connection profiles for Connector Service
    - client_configs: Store client configurations for Demo Config Service
    - service_proposals: Store service proposals for Demo Config Service
    
    These tables enable services to persist data across container restarts
    using JSONB for flexible schema storage.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20251221_062048'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Create persistent storage tables for business services.
    
    Tables created:
    1. connector_profiles - Connection profiles with credentials and config
    2. client_configs - Client-specific configuration data
    3. service_proposals - Generated service proposals and SOWs
    """
    
    # Create connector_profiles table
    op.create_table(
        'connector_profiles',
        sa.Column('id', sa.String(length=255), nullable=False, comment='Unique profile identifier'),
        sa.Column('profile_data', postgresql.JSONB(astext_type=sa.Text()), nullable=False, comment='Profile configuration and credentials'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Profile creation timestamp'),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Last update timestamp'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_connector_profiles')),
        comment='Connection profiles for external data sources (SQL, API, Excel)'
    )
    
    # Create index on created_at for time-based queries
    op.create_index(
        op.f('ix_connector_profiles_created_at'),
        'connector_profiles',
        ['created_at'],
        unique=False
    )
    
    # Create client_configs table
    op.create_table(
        'client_configs',
        sa.Column('client_id', sa.String(length=255), nullable=False, comment='Unique client identifier'),
        sa.Column('config_data', postgresql.JSONB(astext_type=sa.Text()), nullable=False, comment='Client configuration data'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Config creation timestamp'),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Last update timestamp'),
        sa.PrimaryKeyConstraint('client_id', name=op.f('pk_client_configs')),
        comment='Client-specific configuration and preferences'
    )
    
    # Create index on created_at for time-based queries
    op.create_index(
        op.f('ix_client_configs_created_at'),
        'client_configs',
        ['created_at'],
        unique=False
    )
    
    # Create service_proposals table
    op.create_table(
        'service_proposals',
        sa.Column('proposal_id', sa.String(length=255), nullable=False, comment='Unique proposal identifier'),
        sa.Column('proposal_data', postgresql.JSONB(astext_type=sa.Text()), nullable=False, comment='Proposal details, pricing, timeline'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False, comment='Proposal creation timestamp'),
        sa.PrimaryKeyConstraint('proposal_id', name=op.f('pk_service_proposals')),
        comment='Generated service proposals and statements of work'
    )
    
    # Create index on created_at for time-based queries
    op.create_index(
        op.f('ix_service_proposals_created_at'),
        'service_proposals',
        ['created_at'],
        unique=False
    )
    
    # Add comments explaining JSONB structure expectations
    op.execute("""
        COMMENT ON COLUMN connector_profiles.profile_data IS 
        'JSONB structure: {
            "name": "string",
            "type": "sql|api|excel",
            "connection_string": "string (encrypted)",
            "credentials": {"username": "string", "password": "string"},
            "schema_info": {"tables": [...], "columns": {...}},
            "test_status": "success|failed",
            "last_tested": "timestamp"
        }'
    """)
    
    op.execute("""
        COMMENT ON COLUMN client_configs.config_data IS 
        'JSONB structure: {
            "client_name": "string",
            "license_type": "basic|professional|enterprise",
            "modules": ["string"],
            "preferences": {...},
            "custom_kpis": [...],
            "data_sources": [...]
        }'
    """)
    
    op.execute("""
        COMMENT ON COLUMN service_proposals.proposal_data IS 
        'JSONB structure: {
            "client_id": "string",
            "proposal_type": "implementation|consulting",
            "pricing": {"total": number, "breakdown": {...}},
            "timeline": {"start_date": "date", "end_date": "date", "phases": [...]},
            "resources": {"consultants": [...], "hours": number},
            "status": "draft|sent|accepted|rejected"
        }'
    """)


def downgrade() -> None:
    """
    Drop persistent storage tables.
    
    WARNING: This will delete all stored connection profiles, 
    client configurations, and service proposals.
    """
    
    # Drop indexes first
    op.drop_index(op.f('ix_service_proposals_created_at'), table_name='service_proposals')
    op.drop_index(op.f('ix_client_configs_created_at'), table_name='client_configs')
    op.drop_index(op.f('ix_connector_profiles_created_at'), table_name='connector_profiles')
    
    # Drop tables
    op.drop_table('service_proposals')
    op.drop_table('client_configs')
    op.drop_table('connector_profiles')
