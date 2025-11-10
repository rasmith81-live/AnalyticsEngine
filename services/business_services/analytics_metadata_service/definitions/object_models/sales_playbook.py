"""
Sales Playbook Object Model

Represents sales playbooks with best practices and processes.
"""

SALES_PLAYBOOK = {
    "code": "SALES_PLAYBOOK",
    "name": "Sales Playbook",
    "description": "Sales playbooks containing best practices and standardized processes",
    "table_schema": {"table_name": "sales_playbook", "class_name": "Sales Playbook", "columns": [{"name": "playbook_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "adoption_rate", "type": "Float"}, {"name": "compliance_rate", "type": "Float"}, {"name": "last_updated", "type": "String", "length": 255}, {"name": "version", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_playbook_playbook_id", "columns": ["playbook_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
EnablementTeam "1" -- "0..*" SalesPlaybook : creates >
SalesRepresentative "0..*" -- "0..*" SalesPlaybook : adopts >
SalesPlaybook "1" -- "0..*" BestPractice : contains >
SalesPlaybook "1" -- "1" SalesProcess : defines >
' Related Objects
' Relationships to Related Objects
SalesPlaybook "1" -- "*" Sale : relates to
SalesPlaybook "1" -- "*" SalesRepresentative : relates to
SalesPlaybook "1" -- "*" SalesTeam : relates to
@enduml
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "related_kpis": ["SALES_PLAYBOOK_ADOPTION_RATE", "SALES_PROCESS_COMPLIANCE_RATE", "SALES_BEST_PRACTICE_SHARING_RATE"], "key_attributes": ["playbook_id", "name", "adoption_rate", "compliance_rate", "last_updated", "version"], "related_objects": ["Sale", "Sales Representative", "Sales Team"]},
}
