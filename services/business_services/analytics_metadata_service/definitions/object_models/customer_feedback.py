"""
Customer Feedback Object Model

Represents feedback provided by customers through various channels.
"""

CUSTOMER_FEEDBACK = {
    "code": "CUSTOMER_FEEDBACK",
    "name": "Customer Feedback",
    "description": "Customer feedback collected through surveys, reviews, and other channels",
    "table_schema": {"table_name": "customer_feedback", "class_name": "Customer Feedback", "columns": [{"name": "feedback_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "date", "type": "String", "length": 255}, {"name": "type", "type": "String", "length": 255}, {"name": "channel", "type": "String", "length": 255}, {"name": "rating", "type": "String", "length": 255}, {"name": "sentiment", "type": "String", "length": 255}, {"name": "comments", "type": "String", "length": 255}, {"name": "response_provided", "type": "String", "length": 255}, {"name": "action_taken", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_customer_feedback_feedback_id", "columns": ["feedback_id"]}, {"name": "ix_customer_feedback_customer_id", "columns": ["customer_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" CustomerFeedback : provides >
CustomerFeedback "0..*" -- "0..1" Product : about >
CustomerFeedback "1" -- "0..*" FeedbackAction : triggers >
' Relationships to Related Objects
CustomerFeedback "1" -- "*" Account : relates to
CustomerFeedback "1" -- "*" AccountPenetration : relates to
CustomerFeedback "1" -- "*" AccountPlan : relates to
CustomerFeedback "1" -- "*" AccountRisk : relates to
CustomerFeedback "1" -- "*" Call : relates to
CustomerFeedback "1" -- "*" ChannelConflict : relates to
CustomerFeedback "1" -- "*" ChannelDeal : relates to
CustomerFeedback "1" -- "*" ChannelMarket : relates to
CustomerFeedback "1" -- "*" ChannelPartner : relates to
CustomerFeedback "1" -- "*" ChurnEvent : relates to
CustomerFeedback "1" -- "*" CoachingSession : relates to
CustomerFeedback "1" -- "*" CompetitiveAnalysis : relates to
CustomerFeedback "1" -- "*" Contract : relates to
CustomerFeedback "1" -- "*" Customer : relates to
CustomerFeedback "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerFeedback "1" -- "*" CustomerCohort : relates to
CustomerFeedback "1" -- "*" CustomerCommunity : relates to
CustomerFeedback "1" -- "*" CustomerEducation : relates to
CustomerFeedback "1" -- "*" CustomerGoal : relates to
CustomerFeedback "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["CUSTOMER_FEEDBACK_RESPONSE_RATE", "CUSTOMER_SATISFACTION_SCORE_CSAT", "VOICE_OF_THE_CUSTOMER_VOC_EFFECTIVENESS", "SOCIAL_MEDIA_SENTIMENT_ANALYSIS", "CUSTOMER_SERVICE_SATISFACTION_IMPROVEMENT_RATE"], "key_attributes": ["feedback_id", "customer_id", "date", "type", "channel", "rating", "sentiment", "comments", "response_provided", "action_taken"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Goal", "Customer Health Record"]},
}
