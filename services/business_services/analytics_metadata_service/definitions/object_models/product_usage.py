"""
Product Usage Object Model

Represents customer product usage patterns and engagement.
"""

PRODUCT_USAGE = {
    "code": "PRODUCT_USAGE",
    "name": "Product Usage",
    "description": "Customer product usage patterns and engagement tracking",
    "table_schema": {"table_name": "product_usage", "class_name": "Product Usage", "columns": [{"name": "usage_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "product_id", "type": "Integer", "index": True}, {"name": "date", "type": "String", "length": 255}, {"name": "frequency", "type": "String", "length": 255}, {"name": "duration", "type": "String", "length": 255}, {"name": "features_used", "type": "String", "length": 255}, {"name": "engagement_level", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_product_usage_usage_id", "columns": ["usage_id"]}, {"name": "ix_product_usage_customer_id", "columns": ["customer_id"]}, {"name": "ix_product_usage_product_id", "columns": ["product_id"]}, {"name": "ix_product_usage_engagement_level", "columns": ["engagement_level"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" ProductUsage : has >
Product "1" -- "0..*" ProductUsage : tracked by >
ProductUsage "1" -- "1..*" UsageMetric : includes >
' Relationships to Related Objects
ProductUsage "1" -- "*" Account : relates to
ProductUsage "1" -- "*" AccountPenetration : relates to
ProductUsage "1" -- "*" AccountPlan : relates to
ProductUsage "1" -- "*" AccountRisk : relates to
ProductUsage "1" -- "*" Appointment : relates to
ProductUsage "1" -- "*" Certification : relates to
ProductUsage "1" -- "*" ChannelConflict : relates to
ProductUsage "1" -- "*" ChannelDeal : relates to
ProductUsage "1" -- "*" ChannelMarket : relates to
ProductUsage "1" -- "*" ChannelPartner : relates to
ProductUsage "1" -- "*" CompetitiveAnalysis : relates to
ProductUsage "1" -- "*" Customer : relates to
ProductUsage "1" -- "*" CustomerAdvocacyProgram : relates to
ProductUsage "1" -- "*" CustomerCohort : relates to
ProductUsage "1" -- "*" CustomerCommunity : relates to
ProductUsage "1" -- "*" CustomerEducation : relates to
ProductUsage "1" -- "*" CustomerFeedback : relates to
ProductUsage "1" -- "*" CustomerGoal : relates to
ProductUsage "1" -- "*" CustomerHealthRecord : relates to
ProductUsage "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["PRODUCT_USAGE_FREQUENCY", "CONTRACT_UTILIZATION_RATE", "MONTHLY_ACTIVE_USERS_MAU"], "key_attributes": ["usage_id", "customer_id", "product_id", "date", "frequency", "duration", "features_used", "engagement_level"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]},
}
