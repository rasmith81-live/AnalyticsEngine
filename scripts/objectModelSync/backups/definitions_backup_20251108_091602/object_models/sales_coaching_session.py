"""
Sales Coaching Session Object Model

Represents coaching sessions for sales skill development.
"""

from analytics_models import ObjectModel

SALES_COACHING_SESSION = ObjectModel(
    name="Sales Coaching Session",
    code="SALES_COACHING_SESSION",
    description="Coaching sessions for sales representative skill development",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesCoachingSession {
}

class SalesRepresentative {
}

class SalesManager {
}

class TrainingMaterial {
}

class RolePlay {
}

' Relationships
SalesManager "1" -- "0..*" SalesCoachingSession : conducts >
SalesRepresentative "1" -- "0..*" SalesCoachingSession : receives >
SalesCoachingSession "0..*" -- "0..*" TrainingMaterial : uses >
SalesCoachingSession "1" -- "0..*" RolePlay : includes >

@enduml

' Relationships to Related Objects
SalesCoachingSession "1" -- "*" Account : relates to
SalesCoachingSession "1" -- "*" AccountPenetration : relates to
SalesCoachingSession "1" -- "*" AccountPlan : relates to
SalesCoachingSession "1" -- "*" AccountRisk : relates to
SalesCoachingSession "1" -- "*" Appointment : relates to
SalesCoachingSession "1" -- "*" Assessment : relates to
SalesCoachingSession "1" -- "*" Call : relates to
SalesCoachingSession "1" -- "*" Certification : relates to
SalesCoachingSession "1" -- "*" ChannelConflict : relates to
SalesCoachingSession "1" -- "*" ChannelDeal : relates to
SalesCoachingSession "1" -- "*" ChannelMarket : relates to
SalesCoachingSession "1" -- "*" ChannelPartner : relates to
SalesCoachingSession "1" -- "*" ChurnEvent : relates to
SalesCoachingSession "1" -- "*" Co-marketingCampaign : relates to
SalesCoachingSession "1" -- "*" CoachingSession : relates to
SalesCoachingSession "1" -- "*" CompetitiveAnalysis : relates to
SalesCoachingSession "1" -- "*" Contract : relates to
SalesCoachingSession "1" -- "*" Customer : relates to
SalesCoachingSession "1" -- "*" CustomerAdvocacyProgram : relates to
SalesCoachingSession "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_COACHING_EFFECTIVENESS_RATE",
            "PEER_TO_PEER_COACHING_PARTICIPATION_RATE",
            "SALES_ROLE_PLAY_EFFECTIVENESS_SCORE"
        ],
        "key_attributes": [
            "session_id",
            "coach_id",
            "rep_id",
            "date",
            "type",
            "effectiveness_score",
            "topics_covered"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
