"""
Strategic Review Object Model

Represents strategic business reviews with key accounts.
"""

from analytics_models import ObjectModel

STRATEGIC_REVIEW = ObjectModel(
    name="Strategic Review",
    code="STRATEGIC_REVIEW",
    description="Strategic business reviews with key accounts",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class StrategicReview {
}

class KeyAccount {
}

class KeyAccountManager {
}

class Stakeholder {
}

class AccountPlan {
}

class ActionItem {
}

' Relationships
KeyAccount "1" -- "0..*" StrategicReview : reviewed in >
KeyAccountManager "1" -- "0..*" StrategicReview : conducts >
StrategicReview "0..*" -- "1..*" Stakeholder : includes >
StrategicReview "0..*" -- "1" AccountPlan : reviews >
StrategicReview "1" -- "0..*" ActionItem : produces >

@enduml

' Relationships to Related Objects
StrategicReview "1" -- "*" Account : relates to
StrategicReview "1" -- "*" AccountPenetration : relates to
StrategicReview "1" -- "*" AccountPlan : relates to
StrategicReview "1" -- "*" AccountRisk : relates to
StrategicReview "1" -- "*" Assessment : relates to
StrategicReview "1" -- "*" Call : relates to
StrategicReview "1" -- "*" ChannelConflict : relates to
StrategicReview "1" -- "*" ChannelDeal : relates to
StrategicReview "1" -- "*" ChannelMarket : relates to
StrategicReview "1" -- "*" ChannelPartner : relates to
StrategicReview "1" -- "*" CompetitiveAnalysis : relates to
StrategicReview "1" -- "*" EnablementFeedback : relates to
StrategicReview "1" -- "*" EnablementPlatform : relates to
StrategicReview "1" -- "*" Goal : relates to
StrategicReview "1" -- "*" KeyAccount : relates to
StrategicReview "1" -- "*" KeyAccountManager : relates to
StrategicReview "1" -- "*" LostSale : relates to
StrategicReview "1" -- "*" PartnerAgreement : relates to
StrategicReview "1" -- "*" PartnerIncentive : relates to
StrategicReview "1" -- "*" PartnerPerformanceScorecard : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_ENABLEMENT"],
        "related_kpis": [
            "STRATEGIC_ACCOUNT_CONTACT_FREQUENCY"
        ],
        "key_attributes": [
            "review_id",
            "account_id",
            "kam_id",
            "date",
            "attendees",
            "topics_covered",
            "action_items",
            "outcomes",
            "next_review_date"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Enablement Feedback", "Enablement Platform", "Goal", "Key Account", "Key Account Manager", "Lost Sale", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard"]}
)
