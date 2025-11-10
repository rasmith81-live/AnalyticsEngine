"""
Channel Conflict Object Model

Represents conflicts between channel partners or with direct sales.
"""

from analytics_models import ObjectModel

CHANNEL_CONFLICT = ObjectModel(
    name="Channel Conflict",
    code="CHANNEL_CONFLICT",
    description="Conflicts in the channel ecosystem",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "channel_conflict",
        "class_name": "Channel Conflict",
        "columns": [
            {
                "name": "conflict_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "conflict_type",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "parties_involved",
                "type": "String",
                "length": 255
            },
            {
                "name": "deal_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "reported_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "resolution_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "resolution_outcome",
                "type": "String",
                "length": 255
            },
            {
                "name": "status",
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
                "name": "ix_channel_conflict_conflict_id",
                "columns": ["conflict_id"]
            },
            {
                "name": "ix_channel_conflict_conflict_type",
                "columns": ["conflict_type"]
            },
            {
                "name": "ix_channel_conflict_deal_id",
                "columns": ["deal_id"]
            },
            {
                "name": "ix_channel_conflict_reported_date",
                "columns": ["reported_date"]
            },
            {
                "name": "ix_channel_conflict_resolution_date",
                "columns": ["resolution_date"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
ChannelConflict "0..*" -- "1..*" ChannelPartner : involves >
ChannelConflict "1" -- "1" ChannelDeal : related to >
ChannelConflict "1" -- "0..1" Resolution : has >
' Relationships to Related Objects
ChannelConflict "1" -- "*" Account : relates to
ChannelConflict "1" -- "*" AccountPenetration : relates to
ChannelConflict "1" -- "*" AccountPlan : relates to
ChannelConflict "1" -- "*" AccountRisk : relates to
ChannelConflict "1" -- "*" Assessment : relates to
ChannelConflict "1" -- "*" ChannelDeal : relates to
ChannelConflict "1" -- "*" ChannelMarket : relates to
ChannelConflict "1" -- "*" ChannelPartner : relates to
ChannelConflict "1" -- "*" ChurnEvent : relates to
ChannelConflict "1" -- "*" Co-marketingCampaign : relates to
ChannelConflict "1" -- "*" CompetitiveAnalysis : relates to
ChannelConflict "1" -- "*" Contract : relates to
ChannelConflict "1" -- "*" Customer : relates to
ChannelConflict "1" -- "*" CustomerAdvocacyProgram : relates to
ChannelConflict "1" -- "*" CustomerCohort : relates to
ChannelConflict "1" -- "*" CustomerCommunity : relates to
ChannelConflict "1" -- "*" CustomerEducation : relates to
ChannelConflict "1" -- "*" CustomerFeedback : relates to
ChannelConflict "1" -- "*" CustomerGoal : relates to
ChannelConflict "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,

    metadata_={
        "modules": ["CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "CHANNEL_CONFLICT_RATE"
        ],
        "key_attributes": [
            "conflict_id",
            "conflict_type",
            "parties_involved",
            "deal_id",
            "reported_date",
            "resolution_date",
            "resolution_outcome",
            "status"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}

)
