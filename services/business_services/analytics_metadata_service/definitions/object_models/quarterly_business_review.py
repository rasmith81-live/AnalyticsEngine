"""
Quarterly Business Review Object Model

Represents quarterly business reviews with strategic customers.
"""

from analytics_models import ObjectModel

QUARTERLY_BUSINESS_REVIEW = ObjectModel(
    name="Quarterly Business Review",
    code="QUARTERLY_BUSINESS_REVIEW",
    description="Quarterly business reviews with strategic customers",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "quarterly_business_review",
        "class_name": "Quarterly Business Review",
        "columns": [
            {
                "name": "qbr_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "customer_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "date",
                "type": "String",
                "length": 255
            },
            {
                "name": "quarter",
                "type": "String",
                "length": 255
            },
            {
                "name": "attendees",
                "type": "String",
                "length": 255
            },
            {
                "name": "topics_covered",
                "type": "String",
                "length": 255
            },
            {
                "name": "action_items",
                "type": "String",
                "length": 255
            },
            {
                "name": "satisfaction_score",
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
                "name": "ix_quarterly_business_review_qbr_id",
                "columns": ["qbr_id"]
            },
            {
                "name": "ix_quarterly_business_review_customer_id",
                "columns": ["customer_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Customer "1" -- "0..*" QuarterlyBusinessReview : attends >
QuarterlyBusinessReview "1" -- "0..*" ActionItem : produces >
QuarterlyBusinessReview "1" -- "1..*" PerformanceMetric : reviews >
' Relationships to Related Objects
QuarterlyBusinessReview "1" -- "*" Account : relates to
QuarterlyBusinessReview "1" -- "*" AccountPenetration : relates to
QuarterlyBusinessReview "1" -- "*" AccountPlan : relates to
QuarterlyBusinessReview "1" -- "*" AccountRisk : relates to
QuarterlyBusinessReview "1" -- "*" Appointment : relates to
QuarterlyBusinessReview "1" -- "*" Assessment : relates to
QuarterlyBusinessReview "1" -- "*" Call : relates to
QuarterlyBusinessReview "1" -- "*" ChannelConflict : relates to
QuarterlyBusinessReview "1" -- "*" ChannelDeal : relates to
QuarterlyBusinessReview "1" -- "*" ChannelMarket : relates to
QuarterlyBusinessReview "1" -- "*" ChannelPartner : relates to
QuarterlyBusinessReview "1" -- "*" ChurnEvent : relates to
QuarterlyBusinessReview "1" -- "*" CoachingSession : relates to
QuarterlyBusinessReview "1" -- "*" CompetitiveAnalysis : relates to
QuarterlyBusinessReview "1" -- "*" Contract : relates to
QuarterlyBusinessReview "1" -- "*" Customer : relates to
QuarterlyBusinessReview "1" -- "*" CustomerAdvocacyProgram : relates to
QuarterlyBusinessReview "1" -- "*" CustomerCohort : relates to
QuarterlyBusinessReview "1" -- "*" CustomerCommunity : relates to
QuarterlyBusinessReview "1" -- "*" CustomerEducation : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "QUARTERLY_BUSINESS_REVIEWS_QBR_COMPLETED"
        ],
        "key_attributes": [
            "qbr_id",
            "customer_id",
            "date",
            "quarter",
            "attendees",
            "topics_covered",
            "action_items",
            "satisfaction_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education"]}

)
