"""
Expansion Opportunity Object Model

Represents upsell and cross-sell opportunities for existing customers.
"""

from analytics_models import ObjectModel

EXPANSION_OPPORTUNITY = ObjectModel(
    name="Expansion Opportunity",
    code="EXPANSION_OPPORTUNITY",
    description="Upsell and cross-sell opportunities for existing customers",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "expansion_opportunity",
        "class_name": "Expansion Opportunity",
        "columns": [
            {
                "name": "opportunity_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "customer_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "csm_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "type",
                "type": "String",
                "length": 255
            },
            {
                "name": "value",
                "type": "String",
                "length": 255
            },
            {
                "name": "probability",
                "type": "String",
                "length": 255
            },
            {
                "name": "close_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "status",
                "type": "String",
                "length": 255
            },
            {
                "name": "products_included",
                "type": "String",
                "length": 255
            },
            {
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            },
            {
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            }
        ],
        "indexes": [
            {
                "name": "ix_expansion_opportunity_opportunity_id",
                "columns": ["opportunity_id"]
            },
            {
                "name": "ix_expansion_opportunity_customer_id",
                "columns": ["customer_id"]
            },
            {
                "name": "ix_expansion_opportunity_csm_id",
                "columns": ["csm_id"]
            },
            {
                "name": "ix_expansion_opportunity_close_date",
                "columns": ["close_date"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Customer "1" -- "0..*" ExpansionOpportunity : has >
ExpansionOpportunity "0..*" -- "1..*" Product : includes >
ExpansionOpportunity "0..*" -- "1" CustomerSuccessManager : identified by >
ExpansionOpportunity "1" -- "0..1" Revenue : generates >
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
@enduml
    """,

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
