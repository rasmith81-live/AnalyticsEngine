"""
Sales Content Object Model

Represents sales content, collateral, and materials.
"""

SALES_CONTENT = {
    "code": "SALES_CONTENT",
    "name": "Sales Content",
    "description": "Sales content, collateral, and materials for sales effectiveness",
    "table_schema": {"table_name": "sales_content", "class_name": "Sales Content", "columns": [{"name": "content_id", "type": "Integer", "index": True}, {"name": "type", "type": "String", "length": 255}, {"name": "title", "type": "String", "length": 255}, {"name": "usage_rate", "type": "Float"}, {"name": "effectiveness_score", "type": "Float"}, {"name": "last_updated", "type": "String", "length": 255}, {"name": "personalization_level", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_content_content_id", "columns": ["content_id"]}, {"name": "ix_sales_content_personalization_level", "columns": ["personalization_level"]}]},
    "schema_definition": """
    @startuml
' Relationships
EnablementTeam "1" -- "0..*" SalesContent : creates >
SalesRepresentative "0..*" -- "0..*" SalesContent : uses >
EnablementPlatform "1" -- "0..*" SalesContent : hosts >
SalesContent "0..*" -- "0..*" Product : for >
' Related Objects
' Relationships to Related Objects
SalesContent "1" -- "*" Assessment : relates to
SalesContent "1" -- "*" Customer : relates to
SalesContent "1" -- "*" Deal : relates to
SalesContent "1" -- "*" Lead : relates to
SalesContent "1" -- "*" Opportunity : relates to
SalesContent "1" -- "*" Product : relates to
SalesContent "1" -- "*" Proposal : relates to
SalesContent "1" -- "*" Sale : relates to
SalesContent "1" -- "*" SalesQuota : relates to
SalesContent "1" -- "*" SalesRepresentative : relates to
SalesContent "1" -- "*" SalesTeam : relates to
SalesContent "1" -- "*" SalesTerritory : relates to
SalesContent "1" -- "*" TrainingProgram : relates to
@enduml
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "related_kpis": ["CONTENT_UTILIZATION_RATE", "SALES_CONTENT_USAGE_RATE", "SALES_CONTENT_EFFECTIVENESS_RATE", "SALES_CONTENT_PERSONALIZATION_RATE"], "key_attributes": ["content_id", "type", "title", "usage_rate", "effectiveness_score", "last_updated", "personalization_level"], "related_objects": ["Assessment", "Customer", "Deal", "Lead", "Opportunity", "Product", "Proposal", "Sale", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Training Program"]},
}
