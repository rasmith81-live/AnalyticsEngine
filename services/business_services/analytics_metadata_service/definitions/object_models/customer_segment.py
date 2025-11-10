"""
Customer Segment Object Model

Represents customer segmentation for targeted strategies.
"""

from analytics_models import ObjectModel

CUSTOMER_SEGMENT = ObjectModel(
    name="Customer Segment",
    code="CUSTOMER_SEGMENT",
    description="Customer segmentation for targeted retention strategies",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "customer_segment",
        "class_name": "Customer Segment",
        "columns": [
            {
                "name": "segment_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "segment_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "criteria",
                "type": "String",
                "length": 255
            },
            {
                "name": "customer_count",
                "type": "Integer"
            },
            {
                "name": "revenue_contribution",
                "type": "String",
                "length": 255
            },
            {
                "name": "retention_rate",
                "type": "Float"
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
                "name": "ix_customer_segment_segment_id",
                "columns": ["segment_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
CustomerSegment "0..*" -- "0..*" Customer : contains >
CustomerSegment "1" -- "1..*" SegmentCriteria : defined by >
CustomerSegment "1" -- "0..*" SegmentStrategy : has >
' Relationships to Related Objects
CustomerSegment "1" -- "*" Account : relates to
CustomerSegment "1" -- "*" AccountPenetration : relates to
CustomerSegment "1" -- "*" AccountPlan : relates to
CustomerSegment "1" -- "*" AccountRisk : relates to
CustomerSegment "1" -- "*" Call : relates to
CustomerSegment "1" -- "*" ChannelConflict : relates to
CustomerSegment "1" -- "*" ChannelDeal : relates to
CustomerSegment "1" -- "*" ChannelMarket : relates to
CustomerSegment "1" -- "*" ChannelPartner : relates to
CustomerSegment "1" -- "*" ChurnEvent : relates to
CustomerSegment "1" -- "*" CompetitiveAnalysis : relates to
CustomerSegment "1" -- "*" Contract : relates to
CustomerSegment "1" -- "*" Customer : relates to
CustomerSegment "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerSegment "1" -- "*" CustomerCohort : relates to
CustomerSegment "1" -- "*" CustomerCommunity : relates to
CustomerSegment "1" -- "*" CustomerEducation : relates to
CustomerSegment "1" -- "*" CustomerFeedback : relates to
CustomerSegment "1" -- "*" CustomerGoal : relates to
CustomerSegment "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_SEGMENTATION_EFFECTIVENESS",
            "CUSTOMER_CONCENTRATION_RISK"
        ],
        "key_attributes": [
            "segment_id",
            "segment_name",
            "criteria",
            "customer_count",
            "revenue_contribution",
            "retention_rate",
            "effectiveness_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}

)
