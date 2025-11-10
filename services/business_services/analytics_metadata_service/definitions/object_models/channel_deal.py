"""
Channel Deal Object Model

Represents sales deals closed through channel partners.
"""

from analytics_models import ObjectModel

CHANNEL_DEAL = ObjectModel(
    name="Channel Deal",
    code="CHANNEL_DEAL",
    description="Sales deals closed through channel partners",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "channel_deal",
        "class_name": "Channel Deal",
        "columns": [
            {
                "name": "deal_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "deal_size",
                "type": "String",
                "length": 255
            },
            {
                "name": "registration_date",
                "type": "DateTime",
                "index": True
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
                "name": "win_status",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "time_to_close_days",
                "type": "String",
                "length": 255
            },
            {
                "name": "products_included",
                "type": "String",
                "length": 255
            },
            {
                "name": "discount_applied",
                "type": "String",
                "length": 255
            },
            {
                "name": "conflict_flag",
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
                "name": "ix_channel_deal_deal_id",
                "columns": ["deal_id"]
            },
            {
                "name": "ix_channel_deal_registration_date",
                "columns": ["registration_date"]
            },
            {
                "name": "ix_channel_deal_close_date",
                "columns": ["close_date"]
            },
            {
                "name": "ix_channel_deal_win_status",
                "columns": ["win_status"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
ChannelPartner "1" -- "0..*" ChannelDeal : closes >
ChannelDeal "0..*" -- "1..*" Product : includes >
ChannelDeal "1" -- "0..1" Revenue : generates >
ChannelDeal "1" -- "1" Customer : for >
' Relationships to Related Objects
ChannelDeal "1" -- "*" Account : relates to
ChannelDeal "1" -- "*" AccountPenetration : relates to
ChannelDeal "1" -- "*" AccountPlan : relates to
ChannelDeal "1" -- "*" AccountRisk : relates to
ChannelDeal "1" -- "*" Assessment : relates to
ChannelDeal "1" -- "*" ChannelConflict : relates to
ChannelDeal "1" -- "*" ChannelMarket : relates to
ChannelDeal "1" -- "*" ChannelPartner : relates to
ChannelDeal "1" -- "*" ChurnEvent : relates to
ChannelDeal "1" -- "*" Co-marketingCampaign : relates to
ChannelDeal "1" -- "*" CompetitiveAnalysis : relates to
ChannelDeal "1" -- "*" Contract : relates to
ChannelDeal "1" -- "*" Customer : relates to
ChannelDeal "1" -- "*" CustomerAdvocacyProgram : relates to
ChannelDeal "1" -- "*" CustomerCohort : relates to
ChannelDeal "1" -- "*" CustomerCommunity : relates to
ChannelDeal "1" -- "*" CustomerEducation : relates to
ChannelDeal "1" -- "*" CustomerFeedback : relates to
ChannelDeal "1" -- "*" CustomerGoal : relates to
ChannelDeal "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "AVERAGE_DEAL_SIZE",
            "PARTNER_DEAL_SIZE_GROWTH",
            "DEAL_REGISTRATION_RATE",
            "TIME_TO_CLOSE",
            "WIN_RATE",
            "CHANNEL_CONFLICT_RATE"
        ],
        "key_attributes": [
            "deal_id",
            "deal_size",
            "registration_date",
            "close_date",
            "status",
            "win_status",
            "time_to_close_days",
            "products_included",
            "discount_applied",
            "conflict_flag"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}

)
