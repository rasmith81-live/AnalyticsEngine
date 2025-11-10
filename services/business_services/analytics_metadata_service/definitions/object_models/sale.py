"""
Sale Object Model

Represents completed transactions with customers.
"""

SALE = {
    "code": "SALE",
    "name": "Sale",
    "description": "Completed transaction where a deal has been won and closed",
    "table_schema": {"table_name": "sale", "class_name": "Sale", "columns": [{"name": "sale_amount", "type": "Float"}, {"name": "sale_date", "type": "DateTime", "index": True}, {"name": "cost", "type": "String", "length": 255}, {"name": "profit_margin", "type": "String", "length": 255}, {"name": "payment_terms", "type": "String", "length": 255}, {"name": "follow_up_completed", "type": "String", "length": 255}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "sales_rep_id", "type": "Integer", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sale_sale_date", "columns": ["sale_date"]}, {"name": "ix_sale_customer_id", "columns": ["customer_id"]}, {"name": "ix_sale_sales_rep_id", "columns": ["sales_rep_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
Deal "1" -- "0..1" Sale : results in >
Sale "1" -- "1" Customer : creates >
Sale "0..*" -- "1..*" Product : contains >
Sale "1" -- "1" Revenue : generates >
Sale "1" -- "0..*" FollowUp : requires >
' Related Objects
' Relationships to Related Objects
Sale "1" -- "*" Account : relates to
Sale "1" -- "*" Appointment : relates to
Sale "1" -- "*" Assessment : relates to
Sale "1" -- "*" Benchmark : relates to
Sale "1" -- "*" Call : relates to
Sale "1" -- "*" Certification : relates to
Sale "1" -- "*" ChannelPartner : relates to
Sale "1" -- "*" CoachingSession : relates to
Sale "1" -- "*" Contract : relates to
Sale "1" -- "*" Customer : relates to
Sale "1" -- "*" Deal : relates to
Sale "1" -- "*" Demo : relates to
Sale "1" -- "*" Email : relates to
Sale "1" -- "*" Goal : relates to
Sale "1" -- "*" Lead : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["PROFIT_MARGIN_PER_SALE", "POST_SALE_FOLLOW_UP_RATE", "RETURN_ON_SALES_INVESTMENT_ROSI", "SALES_GROWTH", "AVERAGE_REVENUE_PER_UNIT_ARPU"], "key_attributes": ["sale_amount", "sale_date", "cost", "profit_margin", "payment_terms", "follow_up_completed", "customer_id", "sales_rep_id"], "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Certification", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Email", "Goal", "Lead"]},
}
