"""
Enablement Feedback Object Model

Represents feedback from sales teams on enablement programs.
"""

from analytics_models import ObjectModel

ENABLEMENT_FEEDBACK = ObjectModel(
    name="Enablement Feedback",
    code="ENABLEMENT_FEEDBACK",
    description="Feedback from sales teams on enablement programs and content",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "enablement_feedback",
        "class_name": "Enablement Feedback",
        "columns": [
            {
                "name": "feedback_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "rep_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "date",
                "type": "String",
                "length": 255
            },
            {
                "name": "type",
                "type": "String",
                "length": 255
            },
            {
                "name": "satisfaction_score",
                "type": "Float"
            },
            {
                "name": "response_time",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "action_taken",
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
                "name": "ix_enablement_feedback_feedback_id",
                "columns": ["feedback_id"]
            },
            {
                "name": "ix_enablement_feedback_rep_id",
                "columns": ["rep_id"]
            },
            {
                "name": "ix_enablement_feedback_response_time",
                "columns": ["response_time"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" EnablementFeedback : provides >
EnablementTeam "1" -- "0..*" EnablementFeedback : receives >
EnablementFeedback "0..*" -- "0..1" SalesContent : influences >
EnablementFeedback "0..*" -- "0..1" SalesTrainingProgram : influences >
' Relationships to Related Objects
EnablementFeedback "1" -- "*" Account : relates to
EnablementFeedback "1" -- "*" AccountPenetration : relates to
EnablementFeedback "1" -- "*" AccountPlan : relates to
EnablementFeedback "1" -- "*" AccountRisk : relates to
EnablementFeedback "1" -- "*" Assessment : relates to
EnablementFeedback "1" -- "*" Call : relates to
EnablementFeedback "1" -- "*" Certification : relates to
EnablementFeedback "1" -- "*" ChannelConflict : relates to
EnablementFeedback "1" -- "*" ChannelDeal : relates to
EnablementFeedback "1" -- "*" ChannelMarket : relates to
EnablementFeedback "1" -- "*" ChannelPartner : relates to
EnablementFeedback "1" -- "*" ChurnEvent : relates to
EnablementFeedback "1" -- "*" CoachingSession : relates to
EnablementFeedback "1" -- "*" CompetitiveAnalysis : relates to
EnablementFeedback "1" -- "*" Customer : relates to
EnablementFeedback "1" -- "*" CustomerAdvocacyProgram : relates to
EnablementFeedback "1" -- "*" CustomerCohort : relates to
EnablementFeedback "1" -- "*" CustomerCommunity : relates to
EnablementFeedback "1" -- "*" CustomerEducation : relates to
EnablementFeedback "1" -- "*" CustomerFeedback : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "SALES_ENABLEMENT", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_ENABLEMENT_SATISFACTION_SCORE",
            "SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME",
            "SALES_FEEDBACK_LOOP_EFFECTIVENESS"
        ],
        "key_attributes": [
            "feedback_id",
            "rep_id",
            "date",
            "type",
            "satisfaction_score",
            "response_time",
            "action_taken"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Coaching Session", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback"]}

)
