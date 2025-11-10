"""
Emission Object Model

Represents carbon and greenhouse gas emissions.
Critical for environmental sustainability metrics.

Key SCOR Metrics Enabled:
- EV.1.1: Carbon Emissions per Unit
"""

EMISSION = {
    "code": "EMISSION",
    "name": "Emission",
    "description": "Carbon and greenhouse gas emissions tracking",
    "table_schema": {"table_name": "emissions", "class_name": "Emission", "is_hypertable": True, "time_column": "measurement_date", "partition_interval": "1 month", "columns": [{"name": "emission_id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "measurement_date", "type": "DateTime", "nullable": False, "index": True}, {"name": "facility_id", "type": "Integer", "index": True}, {"name": "emission_source", "type": "String", "length": 100, "index": True, "description": "production, transportation, warehousing"}, {"name": "emission_type", "type": "String", "length": 50, "description": "CO2, CH4, N2O, etc."}, {"name": "scope", "type": "Integer", "description": "Scope 1, 2, or 3"}, {"name": "amount_kg", "type": "Float", "nullable": False, "description": "Emissions in kg"}, {"name": "co2_equivalent_kg", "type": "Float", "description": "CO2 equivalent"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}]},
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "SUSTAINABILITY"], "related_kpis": ["CARBON_EMISSIONS_PER_UNIT"]},
}
