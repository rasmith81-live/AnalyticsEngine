"""
Churn Event Object Model

Represents customer churn events and related interventions.
"""

from analytics_models import ObjectModel

CHURN_EVENT = ObjectModel(
    name="Churn Event",
    code="CHURN_EVENT",
    description="Customer churn events with reasons and save attempts",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ChurnEvent {
}

class Customer {
}

class ChurnReason {
}

class SaveAttempt {
}

class WinbackCampaign {
}

' Relationships
Customer "1" -- "0..*" ChurnEvent : may experience >
ChurnEvent "1" -- "1..*" ChurnReason : has >
ChurnEvent "1" -- "0..1" SaveAttempt : may have >
ChurnEvent "1" -- "0..1" WinbackCampaign : may trigger >

@enduml

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
""",
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "CHURN_RATE",
            "CUSTOMER_EXIT_RATE",
            "CUSTOMER_SAVE_RATE",
            "CUSTOMER_WINBACK_RATE"
        ],
        "key_attributes": [
            "churn_id",
            "customer_id",
            "churn_date",
            "churn_reason",
            "save_attempted",
            "save_successful",
            "winback_attempted",
            "winback_successful"
        ],
        "related_objects": ["Account Risk", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback"]}
)
