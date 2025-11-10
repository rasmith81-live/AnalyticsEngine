"""
Customer Education Object Model

Represents customer education content and engagement.
"""

from analytics_models import ObjectModel

CUSTOMER_EDUCATION = ObjectModel(
    name="Customer Education",
    code="CUSTOMER_EDUCATION",
    description="Customer education content and engagement tracking",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "customer_education",
        "class_name": "Customer Education",
        "columns": [
            {
                "name": "education_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "content_type",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "topic",
                "type": "String",
                "length": 255
            },
            {
                "name": "engagement_rate",
                "type": "Float"
            },
            {
                "name": "completion_rate",
                "type": "Float"
            },
            {
                "name": "customer_count",
                "type": "Integer"
            },
            {
                "name": "effectiveness_score",
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
                "name": "ix_customer_education_education_id",
                "columns": ["education_id"]
            },
            {
                "name": "ix_customer_education_content_type",
                "columns": ["content_type"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
CustomerEducation "1" -- "0..*" EducationContent : contains >
Customer "0..*" -- "0..*" EducationContent : consumes >
Customer "1" -- "0..*" EngagementRecord : has >
EngagementRecord "0..*" -- "1" EducationContent : for >
' Relationships to Related Objects
CustomerEducation "1" -- "*" Account : relates to
CustomerEducation "1" -- "*" AccountPenetration : relates to
CustomerEducation "1" -- "*" AccountPlan : relates to
CustomerEducation "1" -- "*" AccountRisk : relates to
CustomerEducation "1" -- "*" Call : relates to
CustomerEducation "1" -- "*" ChannelConflict : relates to
CustomerEducation "1" -- "*" ChannelDeal : relates to
CustomerEducation "1" -- "*" ChannelMarket : relates to
CustomerEducation "1" -- "*" ChannelPartner : relates to
CustomerEducation "1" -- "*" ChurnEvent : relates to
CustomerEducation "1" -- "*" CompetitiveAnalysis : relates to
CustomerEducation "1" -- "*" Contract : relates to
CustomerEducation "1" -- "*" Customer : relates to
CustomerEducation "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerEducation "1" -- "*" CustomerCohort : relates to
CustomerEducation "1" -- "*" CustomerCommunity : relates to
CustomerEducation "1" -- "*" CustomerFeedback : relates to
CustomerEducation "1" -- "*" CustomerGoal : relates to
CustomerEducation "1" -- "*" CustomerHealthRecord : relates to
CustomerEducation "1" -- "*" CustomerJourney : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_EDUCATION_ENGAGEMENT_RATE"
        ],
        "key_attributes": [
            "education_id",
            "content_type",
            "topic",
            "engagement_rate",
            "completion_rate",
            "customer_count",
            "effectiveness_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}

)
