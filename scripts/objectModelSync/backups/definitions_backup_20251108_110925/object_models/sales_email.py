"""
Sales Email Object Model

Represents emails sent by inside sales representatives.
"""

from analytics_models import ObjectModel

SALES_EMAIL = ObjectModel(
    name="Sales Email",
    code="SALES_EMAIL",
    description="Emails sent by inside sales representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesEmail {
}

class SalesRepresentative {
}

class Lead {
}

class EmailEngagement {
}

' Relationships
SalesRepresentative "1" -- "0..*" SalesEmail : sends >
SalesEmail "0..*" -- "1" Lead : to >
SalesEmail "1" -- "0..1" EmailEngagement : tracked by >

@enduml

' Relationships to Related Objects
SalesEmail "1" -- "*" Account : relates to
SalesEmail "1" -- "*" AccountPenetration : relates to
SalesEmail "1" -- "*" AccountPlan : relates to
SalesEmail "1" -- "*" AccountRisk : relates to
SalesEmail "1" -- "*" Appointment : relates to
SalesEmail "1" -- "*" Assessment : relates to
SalesEmail "1" -- "*" Call : relates to
SalesEmail "1" -- "*" Certification : relates to
SalesEmail "1" -- "*" ChannelConflict : relates to
SalesEmail "1" -- "*" ChannelDeal : relates to
SalesEmail "1" -- "*" ChannelMarket : relates to
SalesEmail "1" -- "*" ChannelPartner : relates to
SalesEmail "1" -- "*" ChurnEvent : relates to
SalesEmail "1" -- "*" Co-marketingCampaign : relates to
SalesEmail "1" -- "*" CoachingSession : relates to
SalesEmail "1" -- "*" CompetitiveAnalysis : relates to
SalesEmail "1" -- "*" Contract : relates to
SalesEmail "1" -- "*" Customer : relates to
SalesEmail "1" -- "*" CustomerAdvocacyProgram : relates to
SalesEmail "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "EMAIL_OPEN_RATE",
            "EMAIL_CLICK_THROUGH_RATE_CTR"
        ],
        "key_attributes": [
            "email_id",
            "rep_id",
            "lead_id",
            "date",
            "subject",
            "opened",
            "clicked",
            "replied",
            "bounce_flag"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
