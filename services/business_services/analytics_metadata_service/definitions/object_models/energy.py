"""
Energy Object Model

Represents energy consumption in supply chain operations.
Critical for carbon emissions calculation.

Key SCOR Metrics Enabled:
- EV.1.1: Carbon Emissions per Unit (energy-based emissions)
"""

ENERGY = {
    "code": "ENERGY",
    "name": "Energy",
    "description": "Energy consumption in supply chain operations",
    "table_schema": {"table_name": "energy", "class_name": "Energy", "is_hypertable": True, "time_column": "measurement_date", "partition_interval": "1 month", "columns": [{"name": "energy_id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "measurement_date", "type": "DateTime", "nullable": False, "index": True}, {"name": "facility_id", "type": "Integer", "nullable": False, "index": True}, {"name": "energy_type", "type": "String", "length": 50, "index": True, "description": "electricity, natural_gas, diesel, etc."}, {"name": "consumption_amount", "type": "Float", "nullable": False}, {"name": "unit_of_measure", "type": "String", "length": 20, "description": "kWh, therms, gallons"}, {"name": "cost", "type": "Float"}, {"name": "carbon_factor", "type": "Float", "description": "kg CO2 per unit"}, {"name": "carbon_emissions_kg", "type": "Float"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}]},
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "SUSTAINABILITY"], "related_kpis": ["CARBON_EMISSIONS_PER_UNIT"]},
}
