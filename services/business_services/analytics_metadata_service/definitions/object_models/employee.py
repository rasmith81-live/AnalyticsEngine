"""
Employee Object Model

Represents employees in supply chain operations.
Critical for worker safety and social responsibility metrics.

Key SCOR Metrics Enabled:
- SC.1.1: Worker Safety Incident Rate
"""

from analytics_models import ObjectModel

EMPLOYEE = ObjectModel(
    name="Employee",
    code="EMPLOYEE",
    description="Employees in supply chain operations",

    table_schema={
        "table_name": "employees",
        "class_name": "Employee",
        "columns": [
            {"name": "employee_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "employee_number", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True},
            {"name": "first_name", "type": "String", "length": 100},
            {"name": "last_name", "type": "String", "length": 100},
            {"name": "department", "type": "String", "length": 100, "index": True},
            {"name": "job_title", "type": "String", "length": 100},
            {"name": "facility_id", "type": "Integer", "index": True},
            {"name": "hire_date", "type": "DateTime"},
            {"name": "employment_status", "type": "String", "length": 50, "index": True},
            {"name": "is_supply_chain_role", "type": "Boolean", "default": True},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "HR"],
        "related_kpis": ["WORKER_SAFETY_INCIDENT_RATE"]
    }
)
