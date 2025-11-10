"""
Customer Community Object Model

Represents customer communities and engagement platforms.
"""

from analytics_models import ObjectModel

CUSTOMER_COMMUNITY = ObjectModel(
    name="Customer Community",
    code="CUSTOMER_COMMUNITY",
    description="Customer communities and engagement platforms",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "customer_community",
        "class_name": "Customer Community",
        "columns": [
            {
                "name": "community_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "name",
                "type": "String",
                "length": 255
            },
            {
                "name": "member_count",
                "type": "Integer"
            },
            {
                "name": "active_members",
                "type": "String",
                "length": 255
            },
            {
                "name": "engagement_rate",
                "type": "Float"
            },
            {
                "name": "post_count",
                "type": "Integer"
            },
            {
                "name": "event_count",
                "type": "Integer"
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
                "name": "ix_customer_community_community_id",
                "columns": ["community_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
CustomerCommunity "0..*" -- "0..*" Customer : has members >
CustomerCommunity "1" -- "0..*" CommunityPost : contains >
CustomerCommunity "1" -- "0..*" CommunityEvent : hosts >
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
@enduml
    """,

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
