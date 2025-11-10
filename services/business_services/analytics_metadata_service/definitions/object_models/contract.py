"""
Contract Object Model

Represents agreements and contracts with customers.
"""

CONTRACT = {
    "code": "CONTRACT",
    "name": "Contract",
    "description": "Legal agreements and contracts with customers",
    "table_schema": {"table_name": "contract", "class_name": "Contract", "columns": [{"name": "contract_number", "type": "Integer"}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "renewal_date", "type": "DateTime", "index": True}, {"name": "contract_value", "type": "Float"}, {"name": "terms", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "auto_renew", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_contract_start_date", "columns": ["start_date"]}, {"name": "ix_contract_end_date", "columns": ["end_date"]}, {"name": "ix_contract_renewal_date", "columns": ["renewal_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" Contract : has >
Contract "1" -- "0..*" Renewal : has >
Contract "0..*" -- "1..*" Product : covers >
' Related Objects
' Relationships to Related Objects
Contract "1" -- "*" Account : relates to
Contract "1" -- "*" ChannelPartner : relates to
Contract "1" -- "*" Customer : relates to
Contract "1" -- "*" Deal : relates to
Contract "1" -- "*" Lead : relates to
Contract "1" -- "*" Opportunity : relates to
Contract "1" -- "*" Product : relates to
Contract "1" -- "*" Sale : relates to
Contract "1" -- "*" SalesRepresentative : relates to
Contract "1" -- "*" SalesTeam : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["CONTRACT_RENEWAL_RATE"], "key_attributes": ["contract_number", "start_date", "end_date", "renewal_date", "contract_value", "terms", "status", "auto_renew"], "related_objects": ["Account", "Channel Partner", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale", "Sales Representative", "Sales Team"]},
}
