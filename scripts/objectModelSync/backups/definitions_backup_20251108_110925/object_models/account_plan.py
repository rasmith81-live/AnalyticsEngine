"""
Account Plan Object Model

Represents strategic account plans for key accounts.
"""

from analytics_models import ObjectModel

ACCOUNT_PLAN = ObjectModel(
    name="Account Plan",
    code="ACCOUNT_PLAN",
    description="Strategic plans for managing and growing key accounts",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class AccountPlan {
}

class KeyAccount {
}

class KeyAccountManager {
}

class Objective {
}

class StrategicReview {
}

' Relationships
KeyAccount "1" -- "1" AccountPlan : has >
KeyAccountManager "1" -- "0..*" AccountPlan : creates >
AccountPlan "1" -- "1..*" Objective : has >
AccountPlan "0..*" -- "0..*" StrategicReview : reviewed in >

@enduml

' Relationships to Related Objects
AccountPlan "1" -- "*" Account : relates to
AccountPlan "1" -- "*" AccountPenetration : relates to
AccountPlan "1" -- "*" AccountRisk : relates to
AccountPlan "1" -- "*" Call : relates to
AccountPlan "1" -- "*" ChannelConflict : relates to
AccountPlan "1" -- "*" ChannelDeal : manages
AccountPlan "1" -- "*" ChannelMarket : relates to
AccountPlan "1" -- "*" ChannelPartner : relates to
AccountPlan "1" -- "*" CompetitiveAnalysis : relates to
AccountPlan "1" -- "*" Contract : relates to
AccountPlan "1" -- "*" Customer : relates to
AccountPlan "1" -- "*" CustomerAdvocacyProgram : relates to
AccountPlan "1" -- "*" CustomerCohort : relates to
AccountPlan "1" -- "*" CustomerCommunity : relates to
AccountPlan "1" -- "*" CustomerEducation : relates to
AccountPlan "1" -- "*" CustomerFeedback : relates to
AccountPlan "1" -- "*" CustomerGoal : relates to
AccountPlan "1" -- "*" CustomerHealthRecord : relates to
AccountPlan "1" -- "*" CustomerJourney : relates to
AccountPlan "1" -- "*" CustomerOnboarding : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "STRATEGIC_ACCOUNT_GROWTH",
            "STRATEGIC_ACCOUNT_ROI"
        ],
        "key_attributes": [
            "plan_id",
            "account_id",
            "kam_id",
            "objectives",
            "strategies",
            "growth_targets",
            "roi_targets",
            "review_frequency",
            "created_date",
            "last_updated"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]}
)
