"""
Enablement Feedback Object Model

Represents feedback from sales teams on enablement programs.
"""

from analytics_models import ObjectModel

ENABLEMENT_FEEDBACK = ObjectModel(
    name="Enablement Feedback",
    code="ENABLEMENT_FEEDBACK",
    description="Feedback from sales teams on enablement programs and content",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class EnablementFeedback {
}

class SalesRepresentative {
}

class EnablementTeam {
}

class SalesContent {
}

class SalesTrainingProgram {
}

' Relationships
SalesRepresentative "1" -- "0..*" EnablementFeedback : provides >
EnablementTeam "1" -- "0..*" EnablementFeedback : receives >
EnablementFeedback "0..*" -- "0..1" SalesContent : influences >
EnablementFeedback "0..*" -- "0..1" SalesTrainingProgram : influences >

@enduml

' Relationships to Related Objects
EnablementFeedback "1" -- "*" Account : relates to
EnablementFeedback "1" -- "*" AccountPenetration : relates to
EnablementFeedback "1" -- "*" AccountPlan : relates to
EnablementFeedback "1" -- "*" AccountRisk : relates to
EnablementFeedback "1" -- "*" Assessment : relates to
EnablementFeedback "1" -- "*" Call : relates to
EnablementFeedback "1" -- "*" Certification : relates to
EnablementFeedback "1" -- "*" ChannelConflict : relates to
EnablementFeedback "1" -- "*" ChannelDeal : relates to
EnablementFeedback "1" -- "*" ChannelMarket : relates to
EnablementFeedback "1" -- "*" ChannelPartner : relates to
EnablementFeedback "1" -- "*" ChurnEvent : relates to
EnablementFeedback "1" -- "*" CoachingSession : relates to
EnablementFeedback "1" -- "*" CompetitiveAnalysis : relates to
EnablementFeedback "1" -- "*" Customer : relates to
EnablementFeedback "1" -- "*" CustomerAdvocacyProgram : relates to
EnablementFeedback "1" -- "*" CustomerCohort : relates to
EnablementFeedback "1" -- "*" CustomerCommunity : relates to
EnablementFeedback "1" -- "*" CustomerEducation : relates to
EnablementFeedback "1" -- "*" CustomerFeedback : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "SALES_ENABLEMENT", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_ENABLEMENT_SATISFACTION_SCORE",
            "SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME",
            "SALES_FEEDBACK_LOOP_EFFECTIVENESS"
        ],
        "key_attributes": [
            "feedback_id",
            "rep_id",
            "date",
            "type",
            "satisfaction_score",
            "response_time",
            "action_taken"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback"]}
)
