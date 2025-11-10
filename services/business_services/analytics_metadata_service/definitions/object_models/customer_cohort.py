"""
Customer Cohort Object Model

Represents customer cohorts for retention and trend analysis.
"""

CUSTOMER_COHORT = {
    "code": "CUSTOMER_COHORT",
    "name": "Customer Cohort",
    "description": "Customer cohorts for retention and trend analysis",
    "table_schema": {"table_name": "customer_cohort", "class_name": "Customer Cohort", "columns": [{"name": "cohort_id", "type": "Integer", "index": True}, {"name": "cohort_name", "type": "String", "length": 255}, {"name": "acquisition_period", "type": "String", "length": 255}, {"name": "customer_count", "type": "Integer"}, {"name": "retention_rate", "type": "Float"}, {"name": "churn_rate", "type": "Float"}, {"name": "cohort_age", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_customer_cohort_cohort_id", "columns": ["cohort_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
CustomerCohort "0..*" -- "0..*" Customer : contains >
CustomerCohort "1" -- "0..*" RetentionMetric : tracked by >
' Relationships to Related Objects
CustomerCohort "1" -- "*" Account : relates to
CustomerCohort "1" -- "*" AccountPenetration : relates to
CustomerCohort "1" -- "*" AccountPlan : relates to
CustomerCohort "1" -- "*" AccountRisk : relates to
CustomerCohort "1" -- "*" Call : relates to
CustomerCohort "1" -- "*" ChannelConflict : relates to
CustomerCohort "1" -- "*" ChannelDeal : relates to
CustomerCohort "1" -- "*" ChannelMarket : relates to
CustomerCohort "1" -- "*" ChannelPartner : relates to
CustomerCohort "1" -- "*" ChurnEvent : relates to
CustomerCohort "1" -- "*" CompetitiveAnalysis : relates to
CustomerCohort "1" -- "*" Contract : relates to
CustomerCohort "1" -- "*" Customer : relates to
CustomerCohort "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerCohort "1" -- "*" CustomerCommunity : relates to
CustomerCohort "1" -- "*" CustomerEducation : relates to
CustomerCohort "1" -- "*" CustomerFeedback : relates to
CustomerCohort "1" -- "*" CustomerGoal : relates to
CustomerCohort "1" -- "*" CustomerHealthRecord : relates to
CustomerCohort "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["CUSTOMER_COHORT_RETENTION_RATE"], "key_attributes": ["cohort_id", "cohort_name", "acquisition_period", "customer_count", "retention_rate", "churn_rate", "cohort_age"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]},
}
