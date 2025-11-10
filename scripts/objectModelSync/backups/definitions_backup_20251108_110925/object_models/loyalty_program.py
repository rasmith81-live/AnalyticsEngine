"""
Loyalty Program Object Model

Represents customer loyalty and rewards programs.
"""

from analytics_models import ObjectModel

LOYALTY_PROGRAM = ObjectModel(
    name="Loyalty Program",
    code="LOYALTY_PROGRAM",
    description="Customer loyalty and rewards programs",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class LoyaltyProgram {
}

class Customer {
}

class Reward {
}

class LoyaltyMembership {
}

' Relationships
LoyaltyProgram "0..*" -- "0..*" Customer : has members >
LoyaltyProgram "1" -- "0..*" Reward : offers >
Customer "1" -- "0..1" LoyaltyMembership : has >
LoyaltyMembership "0..*" -- "1" LoyaltyProgram : in >

@enduml

' Relationships to Related Objects
LoyaltyProgram "1" -- "*" Account : relates to
LoyaltyProgram "1" -- "*" AccountPenetration : relates to
LoyaltyProgram "1" -- "*" AccountPlan : relates to
LoyaltyProgram "1" -- "*" AccountRisk : relates to
LoyaltyProgram "1" -- "*" Certification : relates to
LoyaltyProgram "1" -- "*" ChannelConflict : relates to
LoyaltyProgram "1" -- "*" ChannelDeal : relates to
LoyaltyProgram "1" -- "*" ChannelMarket : relates to
LoyaltyProgram "1" -- "*" ChannelPartner : relates to
LoyaltyProgram "1" -- "*" CompetitiveAnalysis : relates to
LoyaltyProgram "1" -- "*" Customer : relates to
LoyaltyProgram "1" -- "*" CustomerAdvocacyProgram : relates to
LoyaltyProgram "1" -- "*" CustomerCohort : relates to
LoyaltyProgram "1" -- "*" CustomerCommunity : relates to
LoyaltyProgram "1" -- "*" CustomerEducation : relates to
LoyaltyProgram "1" -- "*" CustomerFeedback : relates to
LoyaltyProgram "1" -- "*" CustomerGoal : relates to
LoyaltyProgram "1" -- "*" CustomerHealthRecord : relates to
LoyaltyProgram "1" -- "*" CustomerJourney : relates to
LoyaltyProgram "1" -- "*" CustomerOnboarding : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "LOYALTY_PROGRAM_EFFECTIVENESS",
            "LOYALTY_PROGRAM_PARTICIPATION_RATE"
        ],
        "key_attributes": [
            "program_id",
            "program_name",
            "program_type",
            "benefits",
            "participation_rate",
            "effectiveness_score",
            "member_count",
            "engagement_rate"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]}
)
