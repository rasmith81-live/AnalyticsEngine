"""
Sales Territory Object Model

Represents geographic sales territories assigned to field sales representatives.
"""

SALES_TERRITORY = {
    "code": "SALES_TERRITORY",
    "name": "Sales Territory",
    "description": "Geographic sales territories for field sales management",
    "table_schema": {"table_name": "sales_territory", "class_name": "Sales Territory", "columns": [{"name": "territory_id", "type": "Integer", "index": True}, {"name": "territory_name", "type": "String", "length": 255}, {"name": "geographic_area", "type": "String", "length": 255}, {"name": "account_count", "type": "Integer"}, {"name": "potential_value", "type": "Float"}, {"name": "penetration_rate", "type": "Float"}, {"name": "assigned_rep_id", "type": "Integer", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_territory_territory_id", "columns": ["territory_id"]}, {"name": "ix_sales_territory_assigned_rep_id", "columns": ["assigned_rep_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" SalesTerritory : assigned to >
SalesTerritory "1" -- "0..*" Account : contains >
SalesTerritory "1" -- "1" MarketPotential : has >
' Related Objects
' Relationships to Related Objects
SalesTerritory "1" -- "*" Customer : relates to
SalesTerritory "1" -- "*" Product : relates to
SalesTerritory "1" -- "*" Sale : relates to
SalesTerritory "1" -- "*" SalesContent : relates to
SalesTerritory "1" -- "*" SalesRepresentative : relates to
SalesTerritory "1" -- "*" SalesTeam : relates to
@enduml
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "related_kpis": ["TERRITORY_PENETRATION_RATE", "MARKET_PENETRATION_RATE"], "key_attributes": ["territory_id", "territory_name", "geographic_area", "account_count", "potential_value", "penetration_rate", "assigned_rep_id"], "related_objects": ["Customer", "Product", "Sale", "Sales Content", "Sales Representative", "Sales Team"]},
}
