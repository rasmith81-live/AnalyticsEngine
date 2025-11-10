"""
Sales Quota Object Model

Represents sales targets and quotas for teams and individuals.
"""

SALES_QUOTA = {
    "code": "SALES_QUOTA",
    "name": "Sales Quota",
    "description": "Sales targets and quotas assigned to teams and representatives",
    "table_schema": {"table_name": "sales_quota", "class_name": "Sales Quota", "columns": [{"name": "quota_amount", "type": "Float"}, {"name": "period", "type": "String", "length": 255}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "actual_amount", "type": "Float"}, {"name": "attainment_percentage", "type": "Float"}, {"name": "assignee_type", "type": "String", "length": 50, "index": True}, {"name": "assignee_id", "type": "Integer", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_quota_start_date", "columns": ["start_date"]}, {"name": "ix_sales_quota_end_date", "columns": ["end_date"]}, {"name": "ix_sales_quota_assignee_type", "columns": ["assignee_type"]}, {"name": "ix_sales_quota_assignee_id", "columns": ["assignee_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesRepresentative "1" -- "1" SalesQuota : has >
SalesTeam "1" -- "1" SalesQuota : assigned >
SalesQuota "0..*" -- "1" Period : for >
' Related Objects
' Relationships to Related Objects
SalesQuota "1" -- "*" Account : relates to
SalesQuota "1" -- "*" ChannelPartner : relates to
SalesQuota "1" -- "*" CoachingSession : relates to
SalesQuota "1" -- "*" Customer : relates to
SalesQuota "1" -- "*" Deal : relates to
SalesQuota "1" -- "*" Lead : relates to
SalesQuota "1" -- "*" Meeting : relates to
SalesQuota "1" -- "*" Opportunity : relates to
SalesQuota "1" -- "*" Product : relates to
SalesQuota "1" -- "*" Sale : relates to
SalesQuota "1" -- "*" SalesContent : relates to
SalesQuota "1" -- "*" SalesPipeline : relates to
SalesQuota "1" -- "*" SalesRepresentative : relates to
SalesQuota "1" -- "*" SalesTeam : relates to
SalesQuota "1" -- "*" SupportTicket : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["QUOTA_ATTAINMENT_RATE"], "key_attributes": ["quota_amount", "period", "start_date", "end_date", "actual_amount", "attainment_percentage", "assignee_type", "assignee_id"], "related_objects": ["Account", "Channel Partner", "Coaching Session", "Customer", "Deal", "Lead", "Meeting", "Opportunity", "Product", "Sale", "Sales Content", "Sales Pipeline", "Sales Representative", "Sales Team", "Support Ticket"]},
}
