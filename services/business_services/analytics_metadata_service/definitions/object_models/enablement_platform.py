"""
Enablement Platform Object Model

Represents sales enablement platforms and technology.
"""

from analytics_models import ObjectModel

ENABLEMENT_PLATFORM = ObjectModel(
    name="Enablement Platform",
    code="ENABLEMENT_PLATFORM",
    description="Sales enablement platforms and technology systems",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "enablement_platform",
        "class_name": "Enablement Platform",
        "columns": [
            {
                "name": "platform_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "name",
                "type": "String",
                "length": 255
            },
            {
                "name": "utilization_rate",
                "type": "Float"
            },
            {
                "name": "adoption_rate",
                "type": "Float"
            },
            {
                "name": "integration_level",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "user_count",
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
                "name": "ix_enablement_platform_platform_id",
                "columns": ["platform_id"]
            },
            {
                "name": "ix_enablement_platform_integration_level",
                "columns": ["integration_level"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "0..*" -- "0..*" EnablementPlatform : uses >
EnablementPlatform "1" -- "0..*" SalesContent : hosts >
EnablementPlatform "0..*" -- "0..*" CRMSystem : integrates with >
EnablementTeam "1" -- "0..*" EnablementPlatform : manages >
' Relationships to Related Objects
EnablementPlatform "1" -- "*" Assessment : relates to
EnablementPlatform "1" -- "*" Call : relates to
EnablementPlatform "1" -- "*" Certification : relates to
EnablementPlatform "1" -- "*" ChannelConflict : relates to
EnablementPlatform "1" -- "*" ChannelDeal : relates to
EnablementPlatform "1" -- "*" ChannelMarket : relates to
EnablementPlatform "1" -- "*" ChannelPartner : relates to
EnablementPlatform "1" -- "*" ChurnEvent : relates to
EnablementPlatform "1" -- "*" CoachingSession : relates to
EnablementPlatform "1" -- "*" Customer : relates to
EnablementPlatform "1" -- "*" CustomerAdvocacyProgram : relates to
EnablementPlatform "1" -- "*" CustomerCohort : relates to
EnablementPlatform "1" -- "*" CustomerCommunity : relates to
EnablementPlatform "1" -- "*" CustomerEducation : relates to
EnablementPlatform "1" -- "*" CustomerFeedback : relates to
EnablementPlatform "1" -- "*" CustomerGoal : relates to
EnablementPlatform "1" -- "*" CustomerHealthRecord : relates to
EnablementPlatform "1" -- "*" CustomerJourney : relates to
EnablementPlatform "1" -- "*" CustomerOnboarding : relates to
EnablementPlatform "1" -- "*" CustomerSegment : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "SALES_ENABLEMENT"],
        "related_kpis": [
            "SALES_ENABLEMENT_PLATFORM_UTILIZATION_RATE",
            "SALES_TECHNOLOGY_ADOPTION_RATE",
            "SALES_TOOL_INTEGRATION_LEVEL"
        ],
        "key_attributes": [
            "platform_id",
            "name",
            "utilization_rate",
            "adoption_rate",
            "integration_level",
            "user_count"
        ],
        "related_objects": ["Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment"]}

)
