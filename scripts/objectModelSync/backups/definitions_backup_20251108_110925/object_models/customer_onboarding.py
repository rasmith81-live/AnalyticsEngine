"""
Customer Onboarding Object Model

Represents the customer onboarding process and milestones.
"""

from analytics_models import ObjectModel

CUSTOMER_ONBOARDING = ObjectModel(
    name="Customer Onboarding",
    code="CUSTOMER_ONBOARDING",
    description="Customer onboarding process and success tracking",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerOnboarding {
}

class Customer {
}

class OnboardingMilestone {
}

class Training {
}

' Relationships
Customer "1" -- "1" CustomerOnboarding : completes >
CustomerOnboarding "1" -- "0..*" OnboardingMilestone : has >
CustomerOnboarding "1" -- "0..*" Training : includes >

@enduml

' Relationships to Related Objects
CustomerOnboarding "1" -- "*" Account : relates to
CustomerOnboarding "1" -- "*" AccountPenetration : relates to
CustomerOnboarding "1" -- "*" AccountPlan : relates to
CustomerOnboarding "1" -- "*" AccountRisk : relates to
CustomerOnboarding "1" -- "*" Call : relates to
CustomerOnboarding "1" -- "*" ChannelConflict : relates to
CustomerOnboarding "1" -- "*" ChannelDeal : relates to
CustomerOnboarding "1" -- "*" ChannelMarket : relates to
CustomerOnboarding "1" -- "*" ChannelPartner : relates to
CustomerOnboarding "1" -- "*" ChurnEvent : relates to
CustomerOnboarding "1" -- "*" CoachingSession : relates to
CustomerOnboarding "1" -- "*" CompetitiveAnalysis : relates to
CustomerOnboarding "1" -- "*" Contract : relates to
CustomerOnboarding "1" -- "*" Customer : relates to
CustomerOnboarding "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerOnboarding "1" -- "*" CustomerCohort : relates to
CustomerOnboarding "1" -- "*" CustomerCommunity : relates to
CustomerOnboarding "1" -- "*" CustomerEducation : relates to
CustomerOnboarding "1" -- "*" CustomerFeedback : relates to
CustomerOnboarding "1" -- "*" CustomerGoal : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_ONBOARDING_EFFECTIVENESS"
        ],
        "key_attributes": [
            "onboarding_id",
            "customer_id",
            "start_date",
            "completion_date",
            "success_status",
            "satisfaction_score",
            "milestones_completed",
            "time_to_value"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}
)
