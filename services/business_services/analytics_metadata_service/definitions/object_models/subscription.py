"""
Subscription Object Model

Represents customer subscriptions or contracts for products/services.
"""

SUBSCRIPTION = {
    "code": "SUBSCRIPTION",
    "name": "Subscription",
    "description": "Customer subscriptions or contracts for recurring services",
    "table_schema": {"table_name": "subscription", "class_name": "Subscription", "columns": [{"name": "subscription_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "renewal_date", "type": "DateTime", "index": True}, {"name": "contract_value", "type": "Float"}, {"name": "utilization_rate", "type": "Float"}, {"name": "status", "type": "String", "length": 255}, {"name": "renewal_status", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_subscription_subscription_id", "columns": ["subscription_id"]}, {"name": "ix_subscription_customer_id", "columns": ["customer_id"]}, {"name": "ix_subscription_start_date", "columns": ["start_date"]}, {"name": "ix_subscription_end_date", "columns": ["end_date"]}, {"name": "ix_subscription_renewal_date", "columns": ["renewal_date"]}, {"name": "ix_subscription_renewal_status", "columns": ["renewal_status"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" Subscription : has >
Subscription "0..*" -- "1..*" Product : includes >
Subscription "1" -- "0..*" Renewal : has >
Subscription "1" -- "0..*" Revenue : generates >
' Related Objects
' Relationships to Related Objects
Subscription "1" -- "*" Account : relates to
Subscription "1" -- "*" ChannelPartner : relates to
Subscription "1" -- "*" Customer : relates to
Subscription "1" -- "*" Deal : relates to
Subscription "1" -- "*" Lead : relates to
Subscription "1" -- "*" Opportunity : relates to
Subscription "1" -- "*" Product : relates to
Subscription "1" -- "*" Sale : relates to
@enduml
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "related_kpis": ["CONTRACT_UTILIZATION_RATE", "RENEWAL_RATE", "RENEWAL_UPSELL_RATE", "REVENUE_RETENTION_RATE", "NET_REVENUE_RETENTION_NRR"], "key_attributes": ["subscription_id", "customer_id", "start_date", "end_date", "renewal_date", "contract_value", "utilization_rate", "status", "renewal_status"], "related_objects": ["Account", "Channel Partner", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale"]},
}
