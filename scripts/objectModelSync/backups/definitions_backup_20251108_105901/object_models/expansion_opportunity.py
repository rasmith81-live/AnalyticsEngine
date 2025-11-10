"""
Expansion Opportunity Object Model

Represents upsell and cross-sell opportunities for existing customers.
"""

from analytics_models import ObjectModel

EXPANSION_OPPORTUNITY = ObjectModel(
    name="Expansion Opportunity",
    code="EXPANSION_OPPORTUNITY",
    description="Upsell and cross-sell opportunities for existing customers",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ExpansionOpportunity {
}

class Customer {
}

class Product {
}

class CustomerSuccessManager {
}

class Revenue {
}

' Relationships
Customer "1" -- "0..*" ExpansionOpportunity : has >
ExpansionOpportunity "0..*" -- "1..*" Product : includes >
ExpansionOpportunity "0..*" -- "1" CustomerSuccessManager : identified by >
ExpansionOpportunity "1" -- "0..1" Revenue : generates >

@enduml

' Relationships to Related Objects
ExpansionOpportunity "1" -- "*" Account : relates to
ExpansionOpportunity "1" -- "*" AccountPenetration : relates to
ExpansionOpportunity "1" -- "*" AccountPlan : relates to
ExpansionOpportunity "1" -- "*" AccountRisk : relates to
ExpansionOpportunity "1" -- "*" Assessment : relates to
ExpansionOpportunity "1" -- "*" ChannelConflict : relates to
ExpansionOpportunity "1" -- "*" ChannelDeal : manages
ExpansionOpportunity "1" -- "*" ChannelMarket : relates to
ExpansionOpportunity "1" -- "*" ChannelPartner : relates to
ExpansionOpportunity "1" -- "*" EnablementFeedback : relates to
ExpansionOpportunity "1" -- "*" EnablementPlatform : relates to
ExpansionOpportunity "1" -- "*" KeyAccount : relates to
ExpansionOpportunity "1" -- "*" KeyAccountManager : relates to
ExpansionOpportunity "1" -- "*" Lead : relates to
ExpansionOpportunity "1" -- "*" LeadQualification : relates to
ExpansionOpportunity "1" -- "*" LostSale : relates to
ExpansionOpportunity "1" -- "*" LoyaltyProgram : relates to
ExpansionOpportunity "1" -- "*" MarketSegment : relates to
ExpansionOpportunity "1" -- "*" Opportunity : relates to
ExpansionOpportunity "1" -- "*" PartnerAgreement : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
        "related_kpis": [
            "EXPANSION_REVENUE_RATE",
            "UPSELL_AND_CROSS_SELL_RATE",
            "CUSTOMER_ACCOUNT_GROWTH_RATE"
        ],
        "key_attributes": [
            "opportunity_id",
            "customer_id",
            "csm_id",
            "type",
            "value",
            "probability",
            "close_date",
            "status",
            "products_included"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Enablement Feedback", "Enablement Platform", "Key Account", "Key Account Manager", "Lead", "Lead Qualification", "Lost Sale", "Loyalty Program", "Market Segment", "Opportunity", "Partner Agreement"]}
)
