"""
Market Segment Object Model

Represents market segments for strategic analysis and targeting.
"""

from analytics_models import ObjectModel

MARKET_SEGMENT = ObjectModel(
    name="Market Segment",
    code="MARKET_SEGMENT",
    description="Market segments for strategic analysis and targeting",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class MarketSegment {
}

class StrategyTeam {
}

class Customer {
}

class Product {
}

class SalesTerritory {
}

class CompetitivePosition {
}

' Relationships
StrategyTeam "1" -- "0..*" MarketSegment : analyzes >
MarketSegment "1" -- "0..*" Customer : contains >
Product "0..*" -- "0..*" MarketSegment : targets >
SalesTerritory "0..*" -- "0..*" MarketSegment : covers >
MarketSegment "1" -- "1" CompetitivePosition : has >

@enduml

' Relationships to Related Objects
MarketSegment "1" -- "*" Account : relates to
MarketSegment "1" -- "*" AccountPenetration : relates to
MarketSegment "1" -- "*" AccountPlan : relates to
MarketSegment "1" -- "*" AccountRisk : relates to
MarketSegment "1" -- "*" ChannelConflict : relates to
MarketSegment "1" -- "*" ChannelDeal : relates to
MarketSegment "1" -- "*" ChannelMarket : relates to
MarketSegment "1" -- "*" ChannelPartner : relates to
MarketSegment "1" -- "*" CompetitiveAnalysis : relates to
MarketSegment "1" -- "*" Customer : relates to
MarketSegment "1" -- "*" CustomerAdvocacyProgram : relates to
MarketSegment "1" -- "*" CustomerCohort : relates to
MarketSegment "1" -- "*" CustomerCommunity : relates to
MarketSegment "1" -- "*" CustomerEducation : relates to
MarketSegment "1" -- "*" CustomerFeedback : relates to
MarketSegment "1" -- "*" CustomerGoal : relates to
MarketSegment "1" -- "*" CustomerHealthRecord : relates to
MarketSegment "1" -- "*" CustomerJourney : relates to
MarketSegment "1" -- "*" CustomerOnboarding : relates to
MarketSegment "1" -- "*" CustomerSegment : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "MARKET_SHARE",
            "PRODUCT_PENETRATION_RATE",
            "SALES_TERRITORY_PERFORMANCE"
        ],
        "key_attributes": [
            "segment_id",
            "name",
            "size",
            "growth_rate",
            "penetration",
            "strategy"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment"]}
)
