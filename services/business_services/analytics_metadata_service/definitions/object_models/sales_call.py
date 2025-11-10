"""
Sales Call Object Model

Represents phone calls made by inside sales representatives.
"""

SALES_CALL = {
    "code": "SALES_CALL",
    "name": "Sales Call",
    "description": "Phone calls made by inside sales representatives",
    "table_schema": {"table_name": "sales_call", "class_name": "Sales Call", "columns": [{"name": "call_id", "type": "Integer", "index": True}, {"name": "rep_id", "type": "Integer", "index": True}, {"name": "lead_id", "type": "Integer", "index": True}, {"name": "date", "type": "String", "length": 255}, {"name": "duration", "type": "String", "length": 255}, {"name": "call_type", "type": "String", "length": 50, "index": True}, {"name": "outcome", "type": "String", "length": 255}, {"name": "success_flag", "type": "String", "length": 255}, {"name": "recording_url", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_sales_call_call_id", "columns": ["call_id"]}, {"name": "ix_sales_call_rep_id", "columns": ["rep_id"]}, {"name": "ix_sales_call_lead_id", "columns": ["lead_id"]}, {"name": "ix_sales_call_call_type", "columns": ["call_type"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" SalesCall : makes >
SalesCall "0..*" -- "1" Lead : to >
SalesCall "1" -- "0..1" Opportunity : may result in >
' Relationships to Related Objects
SalesCall "1" -- "*" Account : relates to
SalesCall "1" -- "*" AccountPenetration : relates to
SalesCall "1" -- "*" AccountPlan : relates to
SalesCall "1" -- "*" AccountRisk : relates to
SalesCall "1" -- "*" Appointment : relates to
SalesCall "1" -- "*" Assessment : relates to
SalesCall "1" -- "*" Call : relates to
SalesCall "1" -- "*" Certification : relates to
SalesCall "1" -- "*" ChannelConflict : relates to
SalesCall "1" -- "*" ChannelDeal : relates to
SalesCall "1" -- "*" ChannelMarket : relates to
SalesCall "1" -- "*" ChannelPartner : relates to
SalesCall "1" -- "*" ChurnEvent : relates to
SalesCall "1" -- "*" Co-marketingCampaign : relates to
SalesCall "1" -- "*" CoachingSession : relates to
SalesCall "1" -- "*" CompetitiveAnalysis : relates to
SalesCall "1" -- "*" Contract : relates to
SalesCall "1" -- "*" Customer : relates to
SalesCall "1" -- "*" CustomerAdvocacyProgram : relates to
SalesCall "1" -- "*" CustomerCohort : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["CALL_VOLUME", "AVERAGE_SALES_CALL_DURATION", "SALES_CALL_SUCCESS_RATE", "INBOUND_CALL_HANDLING_EFFICIENCY", "OUTBOUND_CALL_CONVERSION_RATE"], "key_attributes": ["call_id", "rep_id", "lead_id", "date", "duration", "call_type", "outcome", "success_flag", "recording_url"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]},
}
