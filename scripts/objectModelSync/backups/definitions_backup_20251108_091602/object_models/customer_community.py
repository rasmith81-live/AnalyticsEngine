"""
Customer Community Object Model

Represents customer communities and engagement platforms.
"""

from analytics_models import ObjectModel

CUSTOMER_COMMUNITY = ObjectModel(
    name="Customer Community",
    code="CUSTOMER_COMMUNITY",
    description="Customer communities and engagement platforms",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerCommunity {
}

class Customer {
}

class CommunityPost {
}

class CommunityEvent {
}

' Relationships
CustomerCommunity "0..*" -- "0..*" Customer : has members >
CustomerCommunity "1" -- "0..*" CommunityPost : contains >
CustomerCommunity "1" -- "0..*" CommunityEvent : hosts >

@enduml

' Relationships to Related Objects
CustomerCommunity "1" -- "*" Account : relates to
CustomerCommunity "1" -- "*" AccountPenetration : relates to
CustomerCommunity "1" -- "*" AccountPlan : relates to
CustomerCommunity "1" -- "*" AccountRisk : relates to
CustomerCommunity "1" -- "*" Call : relates to
CustomerCommunity "1" -- "*" ChannelConflict : relates to
CustomerCommunity "1" -- "*" ChannelDeal : relates to
CustomerCommunity "1" -- "*" ChannelMarket : relates to
CustomerCommunity "1" -- "*" ChannelPartner : relates to
CustomerCommunity "1" -- "*" ChurnEvent : relates to
CustomerCommunity "1" -- "*" CompetitiveAnalysis : relates to
CustomerCommunity "1" -- "*" Contract : relates to
CustomerCommunity "1" -- "*" Customer : relates to
CustomerCommunity "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerCommunity "1" -- "*" CustomerCohort : relates to
CustomerCommunity "1" -- "*" CustomerEducation : relates to
CustomerCommunity "1" -- "*" CustomerFeedback : relates to
CustomerCommunity "1" -- "*" CustomerGoal : relates to
CustomerCommunity "1" -- "*" CustomerHealthRecord : relates to
CustomerCommunity "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_COMMUNITY_ENGAGEMENT_RATE"
        ],
        "key_attributes": [
            "community_id",
            "name",
            "member_count",
            "active_members",
            "engagement_rate",
            "post_count",
            "event_count"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
