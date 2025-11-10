"""
SCOR Metric Object Model - REFERENCE ONLY

This is a REFERENCE/CATALOG object that describes the SCOR metric framework.
It does NOT create a Layer 2 table. Instead:
- SCOR metrics are stored as metadata in Layer 1 (object_models table)
- Individual KPIs are created from SCOR metrics (kpis/ directory)
- Metric observations are stored in scor_metric_observations hypertable
- Business entities (orders, shipments, etc.) create Layer 2 tables

Performance Attributes:
- RL (Reliability): Perfect order fulfillment, delivery performance
- RS (Responsiveness): Order fulfillment cycle time, lead time
- AG (Agility): Supply chain flexibility, adaptability
- CO (Costs): Total supply chain management cost, COGS
- PR (Profit): Return on assets, profit margin
- AM (Asset Management): Cash-to-cash cycle, inventory turns
- EV (Environmental): Carbon emissions, waste reduction
- SC (Social): Worker safety, fair labor practices

Purpose: Framework reference and KPI enrichment metadata
"""

SCOR_METRIC = {
    "code": "SCOR_METRIC",
    "name": "SCOR Metric",
    "description": "SCOR framework metric catalog (reference only) - metrics are implemented as KPIs with SCOR metadata enrichment",
    "table_schema": {"table_name": "scor_metric", "class_name": "SCOR Metric", "columns": [{"name": "id", "type": "String", "length": 50, "primary_key": True, "autoincrement": True}, {"name": "name", "type": "String", "length": 200}, {"name": "description", "type": "String", "length": 1000}, {"name": "attribute", "type": "Enum"}, {"name": "level", "type": "Enum"}, {"name": "unit", "type": "String", "length": 50}, {"name": "calculation", "type": "String", "length": 1000}, {"name": "parent_metric_id", "type": "String", "length": 50}, {"name": "created_at", "type": "DateTime"}, {"name": "updated_at", "type": "DateTime"}, {"name": "parent_metric", "type": "SCORMetric"}, {"name": "child_metrics", "type": "List"}, {"name": "processes", "type": "List"}, {"name": "observations", "type": "List"}, {"name": "benchmarks", "type": "List"}, {"name": "id", "type": "String", "length": 50, "primary_key": True, "autoincrement": True}, {"name": "metric_id", "type": "String", "length": 50}, {"name": "process_id", "type": "String", "length": 50}, {"name": "value", "type": "Float"}, {"name": "unit", "type": "String", "length": 50}, {"name": "observation_date", "type": "DateTime"}, {"name": "observation_start", "type": "DateTime"}, {"name": "observation_end", "type": "DateTime"}, {"name": "id", "type": "String", "length": 50, "primary_key": True, "autoincrement": True}, {"name": "metric_id", "type": "String", "length": 50}, {"name": "group_name", "type": "String", "length": 200}, {"name": "min_value", "type": "Float"}, {"name": "max_value", "type": "Float"}, {"name": "target_value", "type": "Float"}, {"name": "unit", "type": "String", "length": 50}], "indexes": [{"name": "ix_scor_metric_created_at", "columns": ["created_at"]}]},
    "schema_definition": """
    @startuml
    SCORMetric "1" -- "0..*" SCORMetric : decomposes
    SCORMetric "1" -- "0..*" MetricObservation : measures
    SCORMetric "1" -- "0..*" Benchmark : benchmarks
    SCORMetric "0..*" -- "0..*" SCORProcess : measures
    note right of SCORMetric
@enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR"], "is_reference_only": True, "creates_layer_2_table": False, "stored_in_layer_1": True, "implementation_note": "SCOR metrics are implemented as KPIs, not as Layer 2 table rows", "is_hierarchical": True, "supports_parent_child": True, "supports_observations": True, "supports_benchmarks": True, "example_metrics": {"level_1": {"RL": ["RL.1.1 - Perfect Order Fulfillment"], "RS": ["RS.1.1 - Order Fulfillment Cycle Time"], "AG": ["AG.1.1 - Upside Supply Chain Flexibility"], "CO": ["CO.1.1 - Total Supply Chain Management Cost", "CO.1.2 - Cost of Goods Sold"], "PR": ["PR.1.1 - EBIT as % of Revenue"], "AM": ["AM.1.1 - Cash-to-Cash Cycle Time", "AM.1.2 - Return on Supply Chain Fixed Assets"], "EV": ["EV.1.1 - Carbon Emissions per Unit"], "SC": ["SC.1.1 - Worker Safety Incident Rate"]}}},
}
