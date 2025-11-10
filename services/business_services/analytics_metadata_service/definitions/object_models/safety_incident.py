"""
Safety Incident Object Model

Represents workplace safety incidents.
Critical for worker safety metrics and social responsibility.

Key SCOR Metrics Enabled:
- SC.1.1: Worker Safety Incident Rate
"""

from analytics_models import ObjectModel

SAFETY_INCIDENT = ObjectModel(
    name="Safety Incident",
    code="SAFETY_INCIDENT",
    description="Workplace safety incidents tracking",

    table_schema={
        "table_name": "safety_incidents",
        "class_name": "SafetyIncident",
        "columns": [
            {"name": "incident_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "incident_number", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True},
            {"name": "incident_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "employee_id", "type": "Integer", "foreign_key": "employees.employee_id", "index": True},
            {"name": "facility_id", "type": "Integer", "nullable": False, "index": True},
            {"name": "department", "type": "String", "length": 100, "index": True},
            {"name": "incident_type", "type": "String", "length": 50, "index": True, "description": "injury, near_miss, property_damage"},
            {"name": "severity", "type": "String", "length": 50, "index": True, "description": "minor, moderate, serious, fatal"},
            {"name": "is_recordable", "type": "Boolean", "default": True, "description": "OSHA recordable"},
            {"name": "is_lost_time", "type": "Boolean", "default": False, "description": "Lost time incident"},
            {"name": "days_away_from_work", "type": "Integer", "default": 0},
            {"name": "description", "type": "Text"},
            {"name": "root_cause", "type": "Text"},
            {"name": "corrective_action", "type": "Text"},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "HR", "SAFETY"],
        "related_kpis": ["WORKER_SAFETY_INCIDENT_RATE"],
        "scor_metrics": {
            "SC.1.1": {"name": "Worker Safety Incident Rate", "calculation": "(Recordable Incidents / Total Hours Worked) * 200,000"}
        }
    }
)
