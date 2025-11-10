"""
Partnership Object Model

Represents strategic business partnerships and alliances.
"""

from analytics_models import ObjectModel

PARTNERSHIP = ObjectModel(
    name="Partnership",
    code="PARTNERSHIP",
    description="Strategic partnerships and business alliances",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Partnership {
}

class Account {
}

class Opportunity {
}

class Revenue {
}

' Relationships
Partnership "0..*" -- "1" Account : with >
Partnership "1" -- "0..*" Opportunity : generates >
Partnership "1" -- "0..*" Revenue : produces >

@enduml

' Relationships to Related Objects
Partnership "1" -- "*" Account : relates to
Partnership "1" -- "*" AccountPenetration : relates to
Partnership "1" -- "*" AccountPlan : relates to
Partnership "1" -- "*" AccountRisk : relates to
Partnership "1" -- "*" Assessment : relates to
Partnership "1" -- "*" ChannelConflict : relates to
Partnership "1" -- "*" ChannelDeal : relates to
Partnership "1" -- "*" ChannelMarket : relates to
Partnership "1" -- "*" ChannelPartner : relates to
Partnership "1" -- "*" EnablementFeedback : relates to
Partnership "1" -- "*" KeyAccount : relates to
Partnership "1" -- "*" KeyAccountManager : relates to
Partnership "1" -- "*" PartnerAgreement : relates to
Partnership "1" -- "*" PartnerIncentive : relates to
Partnership "1" -- "*" PartnerPerformanceScorecard : relates to
Partnership "1" -- "*" PartnerPortal : relates to
Partnership "1" -- "*" PartnerTraining : relates to
Partnership "1" -- "*" RevenueForecast : relates to
Partnership "1" -- "*" StrategicInitiative : relates to
Partnership "1" -- "*" StrategicReview : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES"],
        "related_kpis": [
            "STRATEGIC_PARTNER_DEVELOPMENT_INDEX"
        ],
        "key_attributes": [
            "partner_name",
            "partnership_type",
            "start_date",
            "status",
            "revenue_contribution",
            "opportunities_generated",
            "effectiveness_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Enablement Feedback", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Strategic Initiative", "Strategic Review"]}
)
