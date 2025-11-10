"""
Account Object Model

Represents target companies/organizations in the sales process.
"""

ACCOUNT = {
    "code": "ACCOUNT",
    "name": "Account",
    "description": "Target companies or organizations in the sales pipeline",
    "table_schema": {"table_name": "account", "class_name": "Account", "columns": [{"name": "account_name", "type": "String", "length": 255}, {"name": "account_type", "type": "String", "length": 50, "index": True}, {"name": "industry", "type": "String", "length": 255}, {"name": "size", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "assigned_team", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_account_account_type", "columns": ["account_type"]}]},
    "schema_definition": """
    @startuml
' Outside Sales Specific
' Key Account Management
' Relationships - Sales Management
SalesTeam "1..*" -- "0..*" Account : manages >
SalesRepresentative "1" -- "0..*" Account : manages >
' Relationships - Sales Process
Account "1" -- "0..*" Lead : generates >
Account "1" -- "0..1" Customer : becomes >
Account "1" -- "0..*" Opportunity : has >
' Relationships - Outside Sales
SalesTerritory "1" -- "0..*" Account : contains >
FieldVisit "0..*" -- "1" Account : to >
SalesAppointment "0..*" -- "1" Account : with >
' Relationships - Key Account Management
Account "0..1" -- "0..1" KeyAccount : may be >
' Related Objects
' Relationships to Related Objects
Account "1" -- "*" Call : relates to
Account "1" -- "*" Contract : relates to
Account "1" -- "*" Customer : relates to
Account "1" -- "*" Deal : manages
Account "1" -- "*" Lead : relates to
Account "1" -- "*" Opportunity : relates to
Account "1" -- "*" Product : relates to
Account "1" -- "*" Sale : relates to
Account "1" -- "*" SalesPipeline : relates to
Account "1" -- "*" SalesQuota : relates to
Account "1" -- "*" SalesRepresentative : relates to
Account "1" -- "*" SalesTeam : relates to
Account "1" -- "*" Subscription : relates to
Account "1" -- "*" SupportTicket : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "OUTSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT"], "related_kpis": ["ACCOUNT_COVERAGE_RATIO", "ACCOUNT_PENETRATION_RATE", "LAND_AND_EXPAND_SUCCESS_RATE"], "key_attributes": ["account_name", "account_type", "industry", "size", "status", "assigned_team"], "related_objects": ["Call", "Contract", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale", "Sales Pipeline", "Sales Quota", "Sales Representative", "Sales Team", "Subscription", "Support Ticket"]},
}
