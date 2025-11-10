"""
Work Hours Object Model

Represents employee work hours in supply chain operations.
Critical for calculating worker safety incident rates.

Key SCOR Metrics Enabled:
- SC.1.1: Worker Safety Incident Rate (hours worked denominator)
"""

from analytics_models import ObjectModel

WORK_HOURS = ObjectModel(
    name="Work Hours",
    code="WORK_HOURS",
    description="Employee work hours in supply chain operations",

    table_schema={
        "table_name": "work_hours",
        "class_name": "WorkHours",
        "is_hypertable": True,
        "time_column": "work_date",
        "partition_interval": "1 month",
        "columns": [
            {"name": "work_hours_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "employee_id", "type": "Integer", "foreign_key": "employees.employee_id", "nullable": False, "index": True},
            {"name": "work_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "facility_id", "type": "Integer", "index": True},
            {"name": "department", "type": "String", "length": 100, "index": True},
            {"name": "regular_hours", "type": "Float", "default": 0},
            {"name": "overtime_hours", "type": "Float", "default": 0},
            {"name": "total_hours", "type": "Float"},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}
        ]
    },

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "HR"],
        "related_kpis": ["WORKER_SAFETY_INCIDENT_RATE"],
        "scor_metrics": {
            "SC.1.1": {"name": "Worker Safety Incident Rate", "calculation": "(Incidents / Total Hours Worked) * 200,000"}
        }
    }
)
