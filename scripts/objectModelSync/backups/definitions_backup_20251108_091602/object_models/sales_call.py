"""
Sales Call Object Model

Represents phone calls made by inside sales representatives.
"""

from analytics_models import ObjectModel

SALES_CALL = ObjectModel(
    name="Sales Call",
    code="SALES_CALL",
    description="Phone calls made by inside sales representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesCall {
}

class SalesRepresentative {
}

class Lead {
}

class Opportunity {
}

' Relationships
SalesRepresentative "1" -- "0..*" SalesCall : makes >
SalesCall "0..*" -- "1" Lead : to >
SalesCall "1" -- "0..1" Opportunity : may result in >

@enduml

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
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CALL_VOLUME",
            "AVERAGE_SALES_CALL_DURATION",
            "SALES_CALL_SUCCESS_RATE",
            "INBOUND_CALL_HANDLING_EFFICIENCY",
            "OUTBOUND_CALL_CONVERSION_RATE"
        ],
        "key_attributes": [
            "call_id",
            "rep_id",
            "lead_id",
            "date",
            "duration",
            "call_type",
            "outcome",
            "success_flag",
            "recording_url"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
