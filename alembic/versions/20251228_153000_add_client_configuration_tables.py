"""Add client configuration tables for conversation service

Revision ID: 20251228_153000
Revises: 20251221_062048
Create Date: 2025-12-28 15:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '20251228_153000'
down_revision: Union[str, None] = '20251221_062048'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create client_configurations table
    op.create_table(
        'client_configurations',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('client_id', sa.String(255), nullable=False),
        sa.Column('client_name', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('version', sa.String(50), nullable=False, server_default='1.0'),
        sa.Column('status', sa.String(50), nullable=False, server_default='draft'),
        sa.Column('source_session_id', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_client_config_client_id', 'client_configurations', ['client_id'])
    op.create_index('ix_client_config_status', 'client_configurations', ['status'])

    # Create client_recordings table
    op.create_table(
        'client_recordings',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('configuration_id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.String(255), nullable=False),
        sa.Column('transcript', sa.Text(), nullable=False),
        sa.Column('duration_seconds', sa.Float(), nullable=True),
        sa.Column('speaker_count', sa.Integer(), nullable=True),
        sa.Column('recorded_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('segments', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['configuration_id'], ['client_configurations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_client_recording_session', 'client_recordings', ['session_id'])
    op.create_index('ix_client_recording_config', 'client_recordings', ['configuration_id'])

    # Create client_intents table
    op.create_table(
        'client_intents',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('configuration_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('confidence', sa.Float(), nullable=False, server_default='1.0'),
        sa.Column('domain', sa.String(100), nullable=False, server_default='general'),
        sa.Column('category', sa.String(100), nullable=True),
        sa.Column('target_entities', postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column('requested_metrics', postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column('parameters', postgresql.JSONB(), nullable=True),
        sa.Column('source_utterance', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['configuration_id'], ['client_configurations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_client_intent_config', 'client_intents', ['configuration_id'])
    op.create_index('ix_client_intent_name', 'client_intents', ['name'])
    op.create_index('ix_client_intent_domain', 'client_intents', ['domain'])

    # Create client_entities table
    op.create_table(
        'client_entities',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('configuration_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('entity_type', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('properties', postgresql.JSONB(), nullable=True),
        sa.Column('related_entities', postgresql.JSONB(), nullable=True),
        sa.Column('extraction_confidence', sa.Float(), nullable=False, server_default='1.0'),
        sa.Column('source_context', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['configuration_id'], ['client_configurations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_client_entity_config', 'client_entities', ['configuration_id'])
    op.create_index('ix_client_entity_name', 'client_entities', ['name'])
    op.create_index('ix_client_entity_type', 'client_entities', ['entity_type'])

    # Create client_value_chain_models table
    op.create_table(
        'client_value_chain_models',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('uuid', sa.String(36), nullable=False),
        sa.Column('configuration_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('version', sa.String(50), nullable=False, server_default='1.0'),
        sa.Column('nodes', postgresql.JSONB(), nullable=False, server_default='[]'),
        sa.Column('links', postgresql.JSONB(), nullable=False, server_default='[]'),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('generated_from_session', sa.String(255), nullable=True),
        sa.Column('generation_method', sa.String(100), nullable=False, server_default='llm'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(['configuration_id'], ['client_configurations.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_client_vcm_config', 'client_value_chain_models', ['configuration_id'])
    op.create_index('ix_client_vcm_name', 'client_value_chain_models', ['name'])
    op.create_index('ix_client_vcm_active', 'client_value_chain_models', ['is_active'])


def downgrade() -> None:
    # Drop tables in reverse order (respecting foreign key constraints)
    op.drop_index('ix_client_vcm_active', table_name='client_value_chain_models')
    op.drop_index('ix_client_vcm_name', table_name='client_value_chain_models')
    op.drop_index('ix_client_vcm_config', table_name='client_value_chain_models')
    op.drop_table('client_value_chain_models')

    op.drop_index('ix_client_entity_type', table_name='client_entities')
    op.drop_index('ix_client_entity_name', table_name='client_entities')
    op.drop_index('ix_client_entity_config', table_name='client_entities')
    op.drop_table('client_entities')

    op.drop_index('ix_client_intent_domain', table_name='client_intents')
    op.drop_index('ix_client_intent_name', table_name='client_intents')
    op.drop_index('ix_client_intent_config', table_name='client_intents')
    op.drop_table('client_intents')

    op.drop_index('ix_client_recording_config', table_name='client_recordings')
    op.drop_index('ix_client_recording_session', table_name='client_recordings')
    op.drop_table('client_recordings')

    op.drop_index('ix_client_config_status', table_name='client_configurations')
    op.drop_index('ix_client_config_client_id', table_name='client_configurations')
    op.drop_table('client_configurations')
