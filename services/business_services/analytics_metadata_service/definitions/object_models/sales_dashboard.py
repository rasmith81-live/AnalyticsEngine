"""
Sales Dashboard Object Model

Represents sales performance dashboards and analytics views.
"""

SALES_DASHBOARD = {
    "code": "SALES_DASHBOARD",
    "name": "Sales Dashboard",
    "description": "Sales performance dashboards and analytics views",
    "table_schema": {"table_name": "sales_dashboard", "class_name": "Sales Dashboard", "columns": [{"name": "dashboard_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "metrics_tracked", "type": "String", "length": 255}, {"name": "refresh_frequency", "type": "String", "length": 255}, {"name": "user_access", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_dashboard_dashboard_id", "columns": ["dashboard_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesOperationsTeam "1" -- "0..*" SalesDashboard : creates >
SalesLeadership "0..*" -- "0..*" SalesDashboard : uses >
SalesDashboard "1" -- "1..*" Metric : displays >
SalesDashboard "0..*" -- "1" CRMSystem : integrates with >
' Relationships to Related Objects
SalesDashboard "1" -- "*" Account : relates to
SalesDashboard "1" -- "*" AccountPenetration : relates to
SalesDashboard "1" -- "*" AccountPlan : relates to
SalesDashboard "1" -- "*" AccountRisk : relates to
SalesDashboard "1" -- "*" Appointment : relates to
SalesDashboard "1" -- "*" Assessment : relates to
SalesDashboard "1" -- "*" Call : relates to
SalesDashboard "1" -- "*" Certification : relates to
SalesDashboard "1" -- "*" ChannelConflict : relates to
SalesDashboard "1" -- "*" ChannelDeal : relates to
SalesDashboard "1" -- "*" ChannelMarket : relates to
SalesDashboard "1" -- "*" ChannelPartner : relates to
SalesDashboard "1" -- "*" ChurnEvent : relates to
SalesDashboard "1" -- "*" Co-marketingCampaign : relates to
SalesDashboard "1" -- "*" CoachingSession : relates to
SalesDashboard "1" -- "*" CompetitiveAnalysis : relates to
SalesDashboard "1" -- "*" Contract : relates to
SalesDashboard "1" -- "*" Customer : relates to
SalesDashboard "1" -- "*" CustomerAdvocacyProgram : relates to
SalesDashboard "1" -- "*" CustomerCohort : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["SALES_OPERATIONAL_EFFICIENCY", "SALES_TEAM_PRODUCTIVITY"], "key_attributes": ["dashboard_id", "name", "metrics_tracked", "refresh_frequency", "user_access"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]},
}
