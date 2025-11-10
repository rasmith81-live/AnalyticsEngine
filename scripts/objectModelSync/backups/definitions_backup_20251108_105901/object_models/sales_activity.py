"""
Sales Activity Object Model

Represents individual sales activities (calls, emails, meetings) performed by inside sales reps.
"""

from analytics_models import ObjectModel

SALES_ACTIVITY = ObjectModel(
    name="Sales Activity",
    code="SALES_ACTIVITY",
    description="Individual sales activities performed by inside sales representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesActivity {
}

class SalesRepresentative {
}

class Lead {
}

class Opportunity {
}

class ActivityScorecard {
}

' Relationships
SalesRepresentative "1" -- "0..*" SalesActivity : performs >
SalesActivity "0..*" -- "0..1" Lead : related to >
SalesActivity "0..*" -- "0..1" Opportunity : related to >
ActivityScorecard "1" -- "0..*" SalesActivity : aggregates >

@enduml

' Relationships to Related Objects
SalesActivity "1" -- "*" Account : relates to
SalesActivity "1" -- "*" AccountPenetration : relates to
SalesActivity "1" -- "*" AccountPlan : relates to
SalesActivity "1" -- "*" AccountRisk : relates to
SalesActivity "1" -- "*" Appointment : relates to
SalesActivity "1" -- "*" Assessment : relates to
SalesActivity "1" -- "*" Call : relates to
SalesActivity "1" -- "*" Certification : relates to
SalesActivity "1" -- "*" ChannelConflict : relates to
SalesActivity "1" -- "*" ChannelDeal : relates to
SalesActivity "1" -- "*" ChannelMarket : relates to
SalesActivity "1" -- "*" ChannelPartner : relates to
SalesActivity "1" -- "*" ChurnEvent : relates to
SalesActivity "1" -- "*" Co-marketingCampaign : relates to
SalesActivity "1" -- "*" CoachingSession : relates to
SalesActivity "1" -- "*" CompetitiveAnalysis : relates to
SalesActivity "1" -- "*" Contract : relates to
SalesActivity "1" -- "*" Customer : relates to
SalesActivity "1" -- "*" CustomerAdvocacyProgram : relates to
SalesActivity "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "ACTIVITY_SCORECARD",
            "FOLLOW_UP_CONTACT_RATE",
            "NEW_CONTACT_RATE"
        ],
        "key_attributes": [
            "activity_id",
            "rep_id",
            "activity_type",
            "date",
            "duration",
            "outcome",
            "lead_id",
            "opportunity_id",
            "notes"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
