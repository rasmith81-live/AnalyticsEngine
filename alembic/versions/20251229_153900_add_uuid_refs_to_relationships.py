"""Add UUID references to metadata_relationships table.

Revision ID: 20251229_153900
Revises: 20251228_153000
Create Date: 2025-12-29 15:39:00

This migration adds from_entity_id and to_entity_id UUID columns to the
metadata_relationships table to enable proper foreign key references to
metadata_definitions. The existing code-based columns are retained for
backward compatibility.
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '20251229_153900'
down_revision = '20251228_153000'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add UUID reference columns to metadata_relationships
    op.add_column(
        'metadata_relationships',
        sa.Column('from_entity_id', UUID(as_uuid=True), nullable=True)
    )
    op.add_column(
        'metadata_relationships',
        sa.Column('to_entity_id', UUID(as_uuid=True), nullable=True)
    )
    
    # Add foreign key constraints
    op.create_foreign_key(
        'fk_rel_from_entity',
        'metadata_relationships',
        'metadata_definitions',
        ['from_entity_id'],
        ['id'],
        ondelete='SET NULL'
    )
    op.create_foreign_key(
        'fk_rel_to_entity',
        'metadata_relationships',
        'metadata_definitions',
        ['to_entity_id'],
        ['id'],
        ondelete='SET NULL'
    )
    
    # Add indexes for the new UUID columns
    op.create_index(
        'idx_rel_from_entity_id',
        'metadata_relationships',
        ['from_entity_id']
    )
    op.create_index(
        'idx_rel_to_entity_id',
        'metadata_relationships',
        ['to_entity_id']
    )
    
    # Populate the UUID columns from existing code-based relationships
    # This updates existing rows to link to the correct metadata_definitions
    op.execute("""
        UPDATE metadata_relationships r
        SET from_entity_id = d.id
        FROM metadata_definitions d
        WHERE LOWER(r.from_entity_code) = LOWER(d.code)
        AND d.is_active = true
    """)
    
    op.execute("""
        UPDATE metadata_relationships r
        SET to_entity_id = d.id
        FROM metadata_definitions d
        WHERE LOWER(r.to_entity_code) = LOWER(d.code)
        AND d.is_active = true
    """)


def downgrade() -> None:
    # Drop indexes
    op.drop_index('idx_rel_to_entity_id', table_name='metadata_relationships')
    op.drop_index('idx_rel_from_entity_id', table_name='metadata_relationships')
    
    # Drop foreign key constraints
    op.drop_constraint('fk_rel_to_entity', 'metadata_relationships', type_='foreignkey')
    op.drop_constraint('fk_rel_from_entity', 'metadata_relationships', type_='foreignkey')
    
    # Drop columns
    op.drop_column('metadata_relationships', 'to_entity_id')
    op.drop_column('metadata_relationships', 'from_entity_id')
