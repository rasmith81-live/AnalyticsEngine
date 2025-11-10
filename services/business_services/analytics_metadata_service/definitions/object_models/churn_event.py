"""
Churn Event Object Model

Represents customer churn events and related interventions.
"""

CHURN_EVENT = {
    "code": "CHURN_EVENT",
    "name": "Churn Event",
    "description": "Customer churn events with reasons and save attempts",
    "table_schema": {"table_name": "churn_event", "class_name": "Churn Event", "columns": [{"name": "churn_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "churn_date", "type": "DateTime", "index": True}, {"name": "churn_reason", "type": "String", "length": 255}, {"name": "save_attempted", "type": "DateTime", "index": True}, {"name": "save_successful", "type": "String", "length": 255}, {"name": "winback_attempted", "type": "DateTime", "index": True}, {"name": "winback_successful", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_churn_event_churn_id", "columns": ["churn_id"]}, {"name": "ix_churn_event_customer_id", "columns": ["customer_id"]}, {"name": "ix_churn_event_churn_date", "columns": ["churn_date"]}, {"name": "ix_churn_event_save_attempted", "columns": ["save_attempted"]}, {"name": "ix_churn_event_winback_attempted", "columns": ["winback_attempted"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" ChurnEvent : may experience >
ChurnEvent "1" -- "1..*" ChurnReason : has >
ChurnEvent "1" -- "0..1" SaveAttempt : may have >
ChurnEvent "1" -- "0..1" WinbackCampaign : may trigger >
' Relationships to Related Objects
ChurnEvent "1" -- "*" AccountRisk : relates to
ChurnEvent "1" -- "*" ChannelConflict : relates to
ChurnEvent "1" -- "*" ChannelDeal : relates to
ChurnEvent "1" -- "*" ChannelMarket : relates to
ChurnEvent "1" -- "*" ChannelPartner : relates to
ChurnEvent "1" -- "*" Contract : relates to
ChurnEvent "1" -- "*" Customer : relates to
ChurnEvent "1" -- "*" CustomerAdvocacyProgram : relates to
ChurnEvent "1" -- "*" CustomerCohort : relates to
ChurnEvent "1" -- "*" CustomerCommunity : relates to
ChurnEvent "1" -- "*" CustomerEducation : relates to
ChurnEvent "1" -- "*" CustomerFeedback : relates to
ChurnEvent "1" -- "*" CustomerGoal : relates to
ChurnEvent "1" -- "*" CustomerHealthRecord : relates to
ChurnEvent "1" -- "*" CustomerJourney : relates to
ChurnEvent "1" -- "*" CustomerOnboarding : relates to
ChurnEvent "1" -- "*" CustomerSegment : relates to
ChurnEvent "1" -- "*" CustomerSuccessManager : relates to
ChurnEvent "1" -- "*" Deal : relates to
ChurnEvent "1" -- "*" EnablementFeedback : relates to
@enduml
    """,
    "metadata_": {"modules": ["CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"], "related_kpis": ["CHURN_RATE", "CUSTOMER_EXIT_RATE", "CUSTOMER_SAVE_RATE", "CUSTOMER_WINBACK_RATE"], "key_attributes": ["churn_id", "customer_id", "churn_date", "churn_reason", "save_attempted", "save_successful", "winback_attempted", "winback_successful"], "related_objects": ["Account Risk", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback"]},
}
