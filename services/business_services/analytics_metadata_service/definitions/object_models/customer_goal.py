"""
Customer Goal Object Model

Represents customer goals and their achievement tracking.
"""

CUSTOMER_GOAL = {
    "code": "CUSTOMER_GOAL",
    "name": "Customer Goal",
    "description": "Customer goals and achievement tracking",
    "table_schema": {"table_name": "customer_goal", "class_name": "Customer Goal", "columns": [{"name": "goal_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "goal_description", "type": "Text"}, {"name": "target_date", "type": "DateTime", "index": True}, {"name": "achievement_status", "type": "String", "length": 50, "index": True}, {"name": "progress_percentage", "type": "Float"}, {"name": "priority", "type": "String", "length": 255}, {"name": "business_impact", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_customer_goal_goal_id", "columns": ["goal_id"]}, {"name": "ix_customer_goal_customer_id", "columns": ["customer_id"]}, {"name": "ix_customer_goal_target_date", "columns": ["target_date"]}, {"name": "ix_customer_goal_achievement_status", "columns": ["achievement_status"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" CustomerGoal : has >
CustomerGoal "0..*" -- "0..*" QuarterlyBusinessReview : reviewed in >
CustomerGoal "1" -- "0..*" Milestone : has >
' Relationships to Related Objects
CustomerGoal "1" -- "*" Account : relates to
CustomerGoal "1" -- "*" AccountPenetration : relates to
CustomerGoal "1" -- "*" AccountPlan : relates to
CustomerGoal "1" -- "*" AccountRisk : relates to
CustomerGoal "1" -- "*" Call : relates to
CustomerGoal "1" -- "*" ChannelConflict : relates to
CustomerGoal "1" -- "*" ChannelDeal : relates to
CustomerGoal "1" -- "*" ChannelMarket : relates to
CustomerGoal "1" -- "*" ChannelPartner : relates to
CustomerGoal "1" -- "*" ChurnEvent : relates to
CustomerGoal "1" -- "*" CompetitiveAnalysis : relates to
CustomerGoal "1" -- "*" Contract : relates to
CustomerGoal "1" -- "*" Customer : relates to
CustomerGoal "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerGoal "1" -- "*" CustomerCohort : relates to
CustomerGoal "1" -- "*" CustomerCommunity : relates to
CustomerGoal "1" -- "*" CustomerEducation : relates to
CustomerGoal "1" -- "*" CustomerFeedback : relates to
CustomerGoal "1" -- "*" CustomerHealthRecord : relates to
CustomerGoal "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["CUSTOMER_GOAL_ACHIEVEMENT_RATE"], "key_attributes": ["goal_id", "customer_id", "goal_description", "target_date", "achievement_status", "progress_percentage", "priority", "business_impact"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Health Record", "Customer Journey"]},
}
