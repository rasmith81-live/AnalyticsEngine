"""Add simulation features tables for Predictive What-If and Process Scenario Modeler.

Revision ID: 20260201_113600
Revises: 20251229_153900_add_uuid_refs_to_relationships
Create Date: 2026-02-01 11:36:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20260201_113600'
down_revision = '20251229_153900_add_uuid_refs_to_relationships'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # KPI Correlations - hypertable for tracking statistical correlations between KPIs
    op.create_table(
        'kpi_correlations',
        sa.Column('time', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('kpi_a_code', sa.String(100), nullable=False),
        sa.Column('kpi_b_code', sa.String(100), nullable=False),
        sa.Column('correlation_coefficient', sa.Numeric(5, 4), nullable=True),
        sa.Column('correlation_method', sa.String(50), nullable=True),  # pearson, spearman, kendall
        sa.Column('lag_periods', sa.Integer, default=0),
        sa.Column('p_value', sa.Numeric(10, 8), nullable=True),
        sa.Column('sample_size', sa.Integer, nullable=True),
        sa.Column('confidence_level', sa.Numeric(4, 2), default=0.95),
        sa.Column('metadata', postgresql.JSONB, nullable=True),
        sa.PrimaryKeyConstraint('time', 'kpi_a_code', 'kpi_b_code')
    )
    # Convert to hypertable
    op.execute("SELECT create_hypertable('kpi_correlations', 'time', if_not_exists => TRUE);")
    
    # Create indexes for correlation queries
    op.create_index('idx_kpi_corr_a', 'kpi_correlations', ['kpi_a_code'])
    op.create_index('idx_kpi_corr_b', 'kpi_correlations', ['kpi_b_code'])
    op.create_index('idx_kpi_corr_method', 'kpi_correlations', ['correlation_method'])
    
    # What-If Predictions - store prediction results
    op.create_table(
        'what_if_predictions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('question_id', sa.String(100), nullable=False, index=True),
        sa.Column('question_text', sa.Text, nullable=False),
        sa.Column('change_type', sa.String(50), nullable=True),  # increase, decrease, add, remove
        sa.Column('change_subject', sa.String(255), nullable=True),  # price, capacity, etc.
        sa.Column('change_magnitude', sa.Numeric(18, 4), nullable=True),
        sa.Column('change_unit', sa.String(50), nullable=True),  # %, $, units
        sa.Column('primary_impacts', postgresql.JSONB, nullable=True),  # List of KPIImpactPrediction
        sa.Column('cascade_effects', postgresql.JSONB, nullable=True),  # List of CascadeEffect
        sa.Column('net_impact', postgresql.JSONB, nullable=True),
        sa.Column('sensitivity_analysis', postgresql.JSONB, nullable=True),
        sa.Column('optimal_value', postgresql.JSONB, nullable=True),
        sa.Column('recommendations', postgresql.JSONB, nullable=True),
        sa.Column('overall_confidence', sa.Numeric(4, 2), nullable=True),
        sa.Column('data_quality_score', sa.Numeric(4, 2), nullable=True),
        sa.Column('model_reliability', sa.Numeric(4, 2), nullable=True),
        sa.Column('methodology', postgresql.JSONB, nullable=True),
        sa.Column('session_id', sa.String(100), nullable=True, index=True),
        sa.Column('asked_by', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    
    # Process Definitions - BPMN-style process structures
    op.create_table(
        'process_definitions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('code', sa.String(100), unique=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('value_chain_module', sa.String(100), nullable=True, index=True),
        sa.Column('definition', postgresql.JSONB, nullable=False),  # Full process structure with steps, transitions
        sa.Column('linked_kpis', postgresql.JSONB, default='[]'),  # List of KPI codes affected
        sa.Column('default_parameters', postgresql.JSONB, default='{}'),
        sa.Column('resource_requirements', postgresql.JSONB, default='[]'),
        sa.Column('version', sa.Integer, default=1),
        sa.Column('is_active', sa.Boolean, default=True, index=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    
    # Process Scenarios - what-if configurations for processes
    op.create_table(
        'process_scenarios',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=True),
        sa.Column('process_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('process_definitions.id'), nullable=False, index=True),
        sa.Column('is_baseline', sa.Boolean, default=False),
        sa.Column('parameter_changes', postgresql.JSONB, nullable=False),  # List of ParameterChange
        sa.Column('simulation_config', postgresql.JSONB, nullable=False),  # Duration, replications, etc.
        sa.Column('arrival_distribution', postgresql.JSONB, nullable=True),
        sa.Column('created_by', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    
    # Simulation Runs - execution tracking
    op.create_table(
        'simulation_runs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('scenario_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('process_scenarios.id'), nullable=False, index=True),
        sa.Column('status', sa.String(50), nullable=False, index=True),  # pending, running, completed, failed
        sa.Column('progress', sa.Integer, default=0),  # 0-100
        sa.Column('started_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('completed_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('results', postgresql.JSONB, nullable=True),  # SimulationResult
        sa.Column('kpi_predictions', postgresql.JSONB, nullable=True),  # Dict[str, KPIPrediction]
        sa.Column('bottlenecks', postgresql.JSONB, nullable=True),  # List of BottleneckInfo
        sa.Column('error', sa.Text, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
    )
    
    # Simulation Events - detailed event log (hypertable)
    op.create_table(
        'simulation_events',
        sa.Column('time', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('simulation_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('event_type', sa.String(50), nullable=False),  # arrival, start, complete, queue, resource
        sa.Column('step_id', sa.String(100), nullable=True),
        sa.Column('entity_id', sa.String(100), nullable=True),
        sa.Column('resource_id', sa.String(100), nullable=True),
        sa.Column('event_data', postgresql.JSONB, nullable=True),
        sa.PrimaryKeyConstraint('time', 'simulation_id', 'event_type')
    )
    # Convert to hypertable
    op.execute("SELECT create_hypertable('simulation_events', 'time', if_not_exists => TRUE);")
    
    # Create indexes for simulation event queries
    op.create_index('idx_sim_events_sim_id', 'simulation_events', ['simulation_id'])
    op.create_index('idx_sim_events_type', 'simulation_events', ['event_type'])
    op.create_index('idx_sim_events_step', 'simulation_events', ['step_id'])
    
    # ML Model Registry - track trained models for predictions
    op.create_table(
        'ml_model_registry',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True, server_default=sa.text('gen_random_uuid()')),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('model_type', sa.String(100), nullable=False, index=True),  # price_elasticity, churn, forecaster, cascade
        sa.Column('version', sa.String(50), nullable=False),
        sa.Column('status', sa.String(50), default='staging', index=True),  # staging, production, archived
        sa.Column('target_kpi', sa.String(100), nullable=True, index=True),
        sa.Column('feature_kpis', postgresql.JSONB, default='[]'),
        sa.Column('hyperparameters', postgresql.JSONB, default='{}'),
        sa.Column('metrics', postgresql.JSONB, default='{}'),  # accuracy, r2, mape, etc.
        sa.Column('artifact_path', sa.String(500), nullable=True),
        sa.Column('trained_at', sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('training_data_range', postgresql.JSONB, nullable=True),  # {start, end, sample_size}
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()')),
        sa.UniqueConstraint('name', 'version', name='uq_ml_model_name_version')
    )


def downgrade() -> None:
    op.drop_table('ml_model_registry')
    op.drop_index('idx_sim_events_step', table_name='simulation_events')
    op.drop_index('idx_sim_events_type', table_name='simulation_events')
    op.drop_index('idx_sim_events_sim_id', table_name='simulation_events')
    op.drop_table('simulation_events')
    op.drop_table('simulation_runs')
    op.drop_table('process_scenarios')
    op.drop_table('process_definitions')
    op.drop_table('what_if_predictions')
    op.drop_index('idx_kpi_corr_method', table_name='kpi_correlations')
    op.drop_index('idx_kpi_corr_b', table_name='kpi_correlations')
    op.drop_index('idx_kpi_corr_a', table_name='kpi_correlations')
    op.drop_table('kpi_correlations')
