"""
Strategic Initiative Object Model

Represents strategic initiatives for sales growth.
"""

from analytics_models import ObjectModel

STRATEGIC_INITIATIVE = ObjectModel(
    name="Strategic Initiative",
    code="STRATEGIC_INITIATIVE",
    description="Strategic initiatives for driving sales growth and market position",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class StrategicInitiative {
}

class StrategyTeam {
}

class MarketSegment {
}

class SalesTeam {
}

class KPI {
}

' Relationships
StrategyTeam "1" -- "0..*" StrategicInitiative : defines >
StrategicInitiative "0..*" -- "0..*" MarketSegment : targets >
SalesTeam "0..*" -- "0..*" StrategicInitiative : executes >
StrategicInitiative "1" -- "1..*" KPI : measured by >

@enduml

' Relationships to Related Objects
StrategicInitiative "1" -- "*" Account : relates to
StrategicInitiative "1" -- "*" AccountPenetration : relates to
StrategicInitiative "1" -- "*" AccountPlan : relates to
StrategicInitiative "1" -- "*" AccountRisk : relates to
StrategicInitiative "1" -- "*" Assessment : relates to
StrategicInitiative "1" -- "*" ChannelConflict : relates to
StrategicInitiative "1" -- "*" ChannelDeal : relates to
StrategicInitiative "1" -- "*" ChannelMarket : relates to
StrategicInitiative "1" -- "*" ChannelPartner : relates to
StrategicInitiative "1" -- "*" CompetitiveAnalysis : relates to
StrategicInitiative "1" -- "*" EnablementFeedback : relates to
StrategicInitiative "1" -- "*" EnablementPlatform : relates to
StrategicInitiative "1" -- "*" Goal : relates to
StrategicInitiative "1" -- "*" KeyAccount : relates to
StrategicInitiative "1" -- "*" KeyAccountManager : relates to
StrategicInitiative "1" -- "*" PartnerAgreement : relates to
StrategicInitiative "1" -- "*" PartnerIncentive : relates to
StrategicInitiative "1" -- "*" PartnerPerformanceScorecard : relates to
StrategicInitiative "1" -- "*" PartnerPortal : relates to
StrategicInitiative "1" -- "*" PartnerTraining : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_ENABLEMENT"],
        "related_kpis": [
            "SALES_GROWTH",
            "MARKET_SHARE"
        ],
        "key_attributes": [
            "initiative_id",
            "name",
            "objectives",
            "timeline",
            "budget",
            "success_metrics",
            "status"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Enablement Feedback", "Enablement Platform", "Goal", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training"]}
)
