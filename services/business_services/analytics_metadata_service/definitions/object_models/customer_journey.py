"""
Customer Journey Object Model

Represents the customer journey with touchpoints and effort tracking.
"""

from analytics_models import ObjectModel

CUSTOMER_JOURNEY = ObjectModel(
    name="Customer Journey",
    code="CUSTOMER_JOURNEY",
    description="Customer journey mapping with touchpoints and effort tracking",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "customer_journey",
        "class_name": "Customer Journey",
        "columns": [
            {
                "name": "journey_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "customer_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "start_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "completion_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "completion_status",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "effort_score",
                "type": "Float"
            },
            {
                "name": "touchpoint_count",
                "type": "Integer"
            },
            {
                "name": "stage_completion",
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
                "name": "ix_customer_journey_journey_id",
                "columns": ["journey_id"]
            },
            {
                "name": "ix_customer_journey_customer_id",
                "columns": ["customer_id"]
            },
            {
                "name": "ix_customer_journey_start_date",
                "columns": ["start_date"]
            },
            {
                "name": "ix_customer_journey_completion_date",
                "columns": ["completion_date"]
            },
            {
                "name": "ix_customer_journey_completion_status",
                "columns": ["completion_status"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Customer "1" -- "0..*" CustomerJourney : experiences >
CustomerJourney "1" -- "1..*" Touchpoint : has >
CustomerJourney "1" -- "1..*" JourneyStage : progresses through >
' Relationships to Related Objects
CustomerJourney "1" -- "*" Account : relates to
CustomerJourney "1" -- "*" AccountPenetration : relates to
CustomerJourney "1" -- "*" AccountPlan : relates to
CustomerJourney "1" -- "*" AccountRisk : relates to
CustomerJourney "1" -- "*" Call : relates to
CustomerJourney "1" -- "*" ChannelConflict : relates to
CustomerJourney "1" -- "*" ChannelDeal : relates to
CustomerJourney "1" -- "*" ChannelMarket : relates to
CustomerJourney "1" -- "*" ChannelPartner : relates to
CustomerJourney "1" -- "*" ChurnEvent : relates to
CustomerJourney "1" -- "*" CompetitiveAnalysis : relates to
CustomerJourney "1" -- "*" Contract : relates to
CustomerJourney "1" -- "*" Customer : relates to
CustomerJourney "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerJourney "1" -- "*" CustomerCohort : relates to
CustomerJourney "1" -- "*" CustomerCommunity : relates to
CustomerJourney "1" -- "*" CustomerEducation : relates to
CustomerJourney "1" -- "*" CustomerFeedback : relates to
CustomerJourney "1" -- "*" CustomerGoal : relates to
CustomerJourney "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_JOURNEY_COMPLETION_RATE",
            "CUSTOMER_EFFORT_SCORE_CES"
        ],
        "key_attributes": [
            "journey_id",
            "customer_id",
            "start_date",
            "completion_date",
            "completion_status",
            "effort_score",
            "touchpoint_count",
            "stage_completion"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}

)
