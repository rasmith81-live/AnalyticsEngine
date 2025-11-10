"""
Account Penetration Object Model

Represents account penetration metrics and analysis.
"""

from analytics_models import ObjectModel

ACCOUNT_PENETRATION = ObjectModel(
    name="Account Penetration",
    code="ACCOUNT_PENETRATION",
    description="Account penetration and market share analysis",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "account_penetration",
        "class_name": "Account Penetration",
        "columns": [
            {
                "name": "penetration_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "account_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "departments_served",
                "type": "String",
                "length": 255
            },
            {
                "name": "total_departments",
                "type": "String",
                "length": 255
            },
            {
                "name": "products_adopted",
                "type": "String",
                "length": 255
            },
            {
                "name": "total_products",
                "type": "String",
                "length": 255
            },
            {
                "name": "wallet_share",
                "type": "String",
                "length": 255
            },
            {
                "name": "saturation_level",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "penetration_score",
                "type": "Float"
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
                "name": "ix_account_penetration_penetration_id",
                "columns": ["penetration_id"]
            },
            {
                "name": "ix_account_penetration_account_id",
                "columns": ["account_id"]
            },
            {
                "name": "ix_account_penetration_saturation_level",
                "columns": ["saturation_level"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
KeyAccount "1" -- "1" AccountPenetration : measured by >
AccountPenetration "1" -- "0..*" Product : tracks adoption of >
AccountPenetration "1" -- "0..*" Department : covers >
' Relationships to Related Objects
AccountPenetration "1" -- "*" Account : relates to
AccountPenetration "1" -- "*" AccountPlan : relates to
AccountPenetration "1" -- "*" AccountRisk : relates to
AccountPenetration "1" -- "*" Call : relates to
AccountPenetration "1" -- "*" ChannelConflict : relates to
AccountPenetration "1" -- "*" ChannelDeal : manages
AccountPenetration "1" -- "*" ChannelMarket : relates to
AccountPenetration "1" -- "*" ChannelPartner : relates to
AccountPenetration "1" -- "*" CompetitiveAnalysis : relates to
AccountPenetration "1" -- "*" Contract : relates to
AccountPenetration "1" -- "*" Customer : relates to
AccountPenetration "1" -- "*" CustomerAdvocacyProgram : relates to
AccountPenetration "1" -- "*" CustomerCohort : relates to
AccountPenetration "1" -- "*" CustomerCommunity : relates to
AccountPenetration "1" -- "*" CustomerEducation : relates to
AccountPenetration "1" -- "*" CustomerFeedback : relates to
AccountPenetration "1" -- "*" CustomerGoal : relates to
AccountPenetration "1" -- "*" CustomerHealthRecord : relates to
AccountPenetration "1" -- "*" CustomerJourney : relates to
AccountPenetration "1" -- "*" CustomerOnboarding : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "ACCOUNT_PENETRATION_INDEX",
            "ACCOUNT_SATURATION_INDEX",
            "ACCOUNT_SHARE_OF_WALLET"
        ],
        "key_attributes": [
            "penetration_id",
            "account_id",
            "departments_served",
            "total_departments",
            "products_adopted",
            "total_products",
            "wallet_share",
            "saturation_level",
            "penetration_score"
        ],
        "related_objects": ["Account", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]}

)
