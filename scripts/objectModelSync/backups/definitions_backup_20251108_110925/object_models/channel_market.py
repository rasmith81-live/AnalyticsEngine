"""
Channel Market Object Model

Represents markets and territories covered by channel partners.
"""

from analytics_models import ObjectModel

CHANNEL_MARKET = ObjectModel(
    name="Channel Market",
    code="CHANNEL_MARKET",
    description="Markets and territories covered by channel partners",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ChannelMarket {
}

class ChannelPartner {
}

class MarketShare {
}

class PenetrationMetric {
}

' Relationships
ChannelMarket "0..*" -- "0..*" ChannelPartner : covered by >
ChannelMarket "1" -- "0..*" MarketShare : has >
ChannelMarket "1" -- "1" PenetrationMetric : measured by >

@enduml

' Relationships to Related Objects
ChannelMarket "1" -- "*" Account : relates to
ChannelMarket "1" -- "*" AccountPenetration : relates to
ChannelMarket "1" -- "*" AccountPlan : relates to
ChannelMarket "1" -- "*" AccountRisk : relates to
ChannelMarket "1" -- "*" Assessment : relates to
ChannelMarket "1" -- "*" ChannelConflict : relates to
ChannelMarket "1" -- "*" ChannelDeal : relates to
ChannelMarket "1" -- "*" ChannelPartner : relates to
ChannelMarket "1" -- "*" ChurnEvent : relates to
ChannelMarket "1" -- "*" Co-marketingCampaign : relates to
ChannelMarket "1" -- "*" CompetitiveAnalysis : relates to
ChannelMarket "1" -- "*" Contract : relates to
ChannelMarket "1" -- "*" Customer : relates to
ChannelMarket "1" -- "*" CustomerAdvocacyProgram : relates to
ChannelMarket "1" -- "*" CustomerCohort : relates to
ChannelMarket "1" -- "*" CustomerCommunity : relates to
ChannelMarket "1" -- "*" CustomerEducation : relates to
ChannelMarket "1" -- "*" CustomerFeedback : relates to
ChannelMarket "1" -- "*" CustomerGoal : relates to
ChannelMarket "1" -- "*" CustomerHealthRecord : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "CHANNEL_PENETRATION_RATE",
            "MARKET_SHARE_GROWTH",
            "PARTNER_GEOGRAPHIC_EXPANSION",
            "PARTNER_COVERAGE_RATIO"
        ],
        "key_attributes": [
            "market_id",
            "market_name",
            "region",
            "country",
            "total_addressable_market",
            "current_penetration",
            "market_share",
            "growth_rate"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}
)
