"""
SCOR Metric Observation Object Model

Stores time-series observations of SCOR metric values.
This is the ONLY Layer 2 table for SCOR - all other SCOR data is metadata.

This is a TimescaleDB hypertable optimized for time-series metric tracking.
Each observation records a metric value at a specific point in time with context.

Use Cases:
- Track Perfect Order Fulfillment % over time
- Monitor Order Fulfillment Cycle Time trends
- Analyze Total Supply Chain Cost changes
- Benchmark performance against industry standards
- Generate historical trend reports

Example Observations:
- RL.1.1 (Perfect Order Fulfillment): 98.5% on 2024-11-08
- RS.1.1 (Order Fulfillment Cycle Time): 2.3 days on 2024-11-08
- CO.1.1 (Total Supply Chain Cost): $2.5M on 2024-11-08
"""

SCOR_METRIC_OBSERVATION = {
    "code": "SCOR_METRIC_OBSERVATION",
    "name": "SCOR Metric Observation",
    "description": "Time-series observations of SCOR metric values with context and dimensions",
    "table_schema": {"table_name": "scor_metric_observations", "class_name": "SCORMetricObservation", "is_hypertable": True, "time_column": "timestamp", "partition_interval": "1 day", "columns": [{"name": "id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "timestamp", "type": "DateTime", "nullable": False, "index": True, "description": "When the metric was observed/calculated"}, {"name": "scor_metric_id", "type": "String", "length": 50, "nullable": False, "index": True, "description": "SCOR metric identifier (e.g., 'RL.1.1', 'RS.1.1')"}, {"name": "kpi_code", "type": "String", "length": 100, "index": True, "description": "Associated KPI code (e.g., 'PERFECT_ORDER_FULFILLMENT')"}, {"name": "value", "type": "Float", "nullable": False, "description": "Metric value"}, {"name": "unit", "type": "String", "length": 50, "description": "Unit of measurement (e.g., 'percentage', 'days', 'dollars')"}, {"name": "observation_period_start", "type": "DateTime", "description": "Start of the period this observation covers"}, {"name": "observation_period_end", "type": "DateTime", "description": "End of the period this observation covers"}, {"name": "organization_id", "type": "Integer", "index": True, "description": "Organization/client this observation belongs to"}, {"name": "process_id", "type": "String", "length": 50, "index": True, "description": "SCOR process this metric is associated with (e.g., 'P1', 'S1')"}, {"name": "context", "type": "JSON", "description": "Additional dimensions and context (region, product_line, facility, etc.)"}, {"name": "data_source", "type": "String", "length": 100, "description": "Source of the data (e.g., 'calculated', 'manual_entry', 'imported')"}, {"name": "confidence_level", "type": "Float", "description": "Confidence level in the observation (0.0 to 1.0)"}, {"name": "notes", "type": "Text", "description": "Additional notes or comments about this observation"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_scor_metric_observations_timestamp", "columns": ["timestamp"], "description": "Primary time-series index"}, {"name": "ix_scor_metric_observations_scor_metric_id", "columns": ["scor_metric_id"], "description": "Index for filtering by SCOR metric"}, {"name": "ix_scor_metric_observations_kpi_code", "columns": ["kpi_code"], "description": "Index for filtering by KPI"}, {"name": "ix_scor_metric_observations_organization_id", "columns": ["organization_id"], "description": "Index for multi-tenant filtering"}, {"name": "ix_scor_metric_observations_process_id", "columns": ["process_id"], "description": "Index for filtering by SCOR process"}, {"name": "ix_scor_metric_observations_composite", "columns": ["scor_metric_id", "timestamp", "organization_id"], "description": "Composite index for common query patterns"}], "constraints": [{"type": "check", "name": "chk_value_positive", "expression": "value >= 0", "description": "Ensure metric values are non-negative"}, {"type": "check", "name": "chk_confidence_range", "expression": "confidence_level IS NULL OR (confidence_level >= 0 AND confidence_level <= 1)", "description": "Ensure confidence level is between 0 and 1"}]},
    "schema_definition": """
    @startuml
    SCORMetricObservation "*" -- "1" Organization : belongs_to
    SCORMetricObservation "*" -- "1" SCORMetric : measures (via scor_metric_id)
    SCORMetricObservation "*" -- "1" KPI : calculated_from (via kpi_code)
    SCORMetricObservation "*" -- "0..1" SCORProcess : associated_with (via process_id)
    note right of SCORMetricObservation
        TimescaleDB Hypertable
        Partitioned by timestamp
        Optimized for time-series queries
        Stores actual metric values over time
    end note
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR"], "is_hypertable": True, "creates_layer_2_table": True, "time_series": True, "partition_by": "timestamp", "retention_policy": {"hot_data": "90 days", "warm_data": "1 year", "cold_data": "7 years (archived to Layer 2a)"}, "example_observations": [{"scor_metric_id": "RL.1.1", "kpi_code": "PERFECT_ORDER_FULFILLMENT", "value": 98.5, "unit": "percentage", "timestamp": "2024-11-08T13:00:00Z", "context": {"region": "North America", "product_line": "Electronics", "facility": "DC-001"}}, {"scor_metric_id": "RS.1.1", "kpi_code": "ORDER_FULFILLMENT_CYCLE_TIME", "value": 2.3, "unit": "days", "timestamp": "2024-11-08T13:00:00Z", "context": {"region": "Europe", "customer_segment": "Enterprise"}}, {"scor_metric_id": "CO.1.1", "kpi_code": "TOTAL_SUPPLY_CHAIN_COST", "value": 2500000, "unit": "dollars", "timestamp": "2024-11-08T13:00:00Z", "context": {"cost_center": "Logistics", "period": "Q4 2024"}}], "query_patterns": ["Time-series trend analysis", "Performance benchmarking", "Period-over-period comparison", "Multi-dimensional analysis (by region, product, etc.)", "Anomaly detection", "Forecasting and prediction"], "timescaledb_features": {"compression": "After 30 days", "continuous_aggregates": ["hourly_scor_metrics", "daily_scor_metrics", "weekly_scor_metrics", "monthly_scor_metrics"], "data_retention": "Automatic archival to Layer 2a after 1 year"}},
}
