"""
Account Plan Object Model

Represents strategic account plans for key accounts.
"""

ACCOUNT_PLAN = {
    "code": "ACCOUNT_PLAN",
    "name": "Account Plan",
    "description": "Strategic plans for managing and growing key accounts",
    "table_schema": {"table_name": "account_plan", "class_name": "Account Plan", "columns": [{"name": "plan_id", "type": "Integer", "index": True}, {"name": "account_id", "type": "Integer", "index": True}, {"name": "kam_id", "type": "Integer", "index": True}, {"name": "objectives", "type": "String", "length": 255}, {"name": "strategies", "type": "String", "length": 255}, {"name": "growth_targets", "type": "String", "length": 255}, {"name": "roi_targets", "type": "String", "length": 255}, {"name": "review_frequency", "type": "String", "length": 255}, {"name": "created_date", "type": "DateTime", "index": True}, {"name": "last_updated", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_account_plan_plan_id", "columns": ["plan_id"]}, {"name": "ix_account_plan_account_id", "columns": ["account_id"]}, {"name": "ix_account_plan_kam_id", "columns": ["kam_id"]}, {"name": "ix_account_plan_created_date", "columns": ["created_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
KeyAccount "1" -- "1" AccountPlan : has >
KeyAccountManager "1" -- "0..*" AccountPlan : creates >
AccountPlan "1" -- "1..*" Objective : has >
AccountPlan "0..*" -- "0..*" StrategicReview : reviewed in >
' Relationships to Related Objects
AccountPlan "1" -- "*" Account : relates to
AccountPlan "1" -- "*" AccountPenetration : relates to
AccountPlan "1" -- "*" AccountRisk : relates to
AccountPlan "1" -- "*" Call : relates to
AccountPlan "1" -- "*" ChannelConflict : relates to
AccountPlan "1" -- "*" ChannelDeal : manages
AccountPlan "1" -- "*" ChannelMarket : relates to
AccountPlan "1" -- "*" ChannelPartner : relates to
AccountPlan "1" -- "*" CompetitiveAnalysis : relates to
AccountPlan "1" -- "*" Contract : relates to
AccountPlan "1" -- "*" Customer : relates to
AccountPlan "1" -- "*" CustomerAdvocacyProgram : relates to
AccountPlan "1" -- "*" CustomerCohort : relates to
AccountPlan "1" -- "*" CustomerCommunity : relates to
AccountPlan "1" -- "*" CustomerEducation : relates to
AccountPlan "1" -- "*" CustomerFeedback : relates to
AccountPlan "1" -- "*" CustomerGoal : relates to
AccountPlan "1" -- "*" CustomerHealthRecord : relates to
AccountPlan "1" -- "*" CustomerJourney : relates to
AccountPlan "1" -- "*" CustomerOnboarding : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["STRATEGIC_ACCOUNT_GROWTH", "STRATEGIC_ACCOUNT_ROI"], "key_attributes": ["plan_id", "account_id", "kam_id", "objectives", "strategies", "growth_targets", "roi_targets", "review_frequency", "created_date", "last_updated"], "related_objects": ["Account", "Account Penetration", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]},
}
