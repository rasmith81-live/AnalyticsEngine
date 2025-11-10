"""
Customer Onboarding Object Model

Represents the customer onboarding process and milestones.
"""

from analytics_models import ObjectModel

CUSTOMER_ONBOARDING = ObjectModel(
    name="Customer Onboarding",
    code="CUSTOMER_ONBOARDING",
    description="Customer onboarding process and success tracking",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "customer_onboarding",
        "class_name": "Customer Onboarding",
        "columns": [
            {
                "name": "onboarding_id",
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
                "name": "success_status",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "satisfaction_score",
                "type": "Float"
            },
            {
                "name": "milestones_completed",
                "type": "String",
                "length": 255
            },
            {
                "name": "time_to_value",
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
                "name": "ix_customer_onboarding_onboarding_id",
                "columns": ["onboarding_id"]
            },
            {
                "name": "ix_customer_onboarding_customer_id",
                "columns": ["customer_id"]
            },
            {
                "name": "ix_customer_onboarding_start_date",
                "columns": ["start_date"]
            },
            {
                "name": "ix_customer_onboarding_completion_date",
                "columns": ["completion_date"]
            },
            {
                "name": "ix_customer_onboarding_success_status",
                "columns": ["success_status"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Customer "1" -- "1" CustomerOnboarding : completes >
CustomerOnboarding "1" -- "0..*" OnboardingMilestone : has >
CustomerOnboarding "1" -- "0..*" Training : includes >
' Relationships to Related Objects
CustomerOnboarding "1" -- "*" Account : relates to
CustomerOnboarding "1" -- "*" AccountPenetration : relates to
CustomerOnboarding "1" -- "*" AccountPlan : relates to
CustomerOnboarding "1" -- "*" AccountRisk : relates to
CustomerOnboarding "1" -- "*" Call : relates to
CustomerOnboarding "1" -- "*" ChannelConflict : relates to
CustomerOnboarding "1" -- "*" ChannelDeal : relates to
CustomerOnboarding "1" -- "*" ChannelMarket : relates to
CustomerOnboarding "1" -- "*" ChannelPartner : relates to
CustomerOnboarding "1" -- "*" ChurnEvent : relates to
CustomerOnboarding "1" -- "*" CoachingSession : relates to
CustomerOnboarding "1" -- "*" CompetitiveAnalysis : relates to
CustomerOnboarding "1" -- "*" Contract : relates to
CustomerOnboarding "1" -- "*" Customer : relates to
CustomerOnboarding "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerOnboarding "1" -- "*" CustomerCohort : relates to
CustomerOnboarding "1" -- "*" CustomerCommunity : relates to
CustomerOnboarding "1" -- "*" CustomerEducation : relates to
CustomerOnboarding "1" -- "*" CustomerFeedback : relates to
CustomerOnboarding "1" -- "*" CustomerGoal : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_ONBOARDING_EFFECTIVENESS"
        ],
        "key_attributes": [
            "onboarding_id",
            "customer_id",
            "start_date",
            "completion_date",
            "success_status",
            "satisfaction_score",
            "milestones_completed",
            "time_to_value"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}

)
