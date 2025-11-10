"""
Partner Training Object Model

Represents training programs and completions for channel partners.
"""

from analytics_models import ObjectModel

PARTNER_TRAINING = ObjectModel(
    name="Partner Training",
    code="PARTNER_TRAINING",
    description="Training programs for channel partner enablement",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "partner_training",
        "class_name": "Partner Training",
        "columns": [
            {
                "name": "training_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "training_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "training_type",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "duration",
                "type": "String",
                "length": 255
            },
            {
                "name": "completion_requirements",
                "type": "String",
                "length": 255
            },
            {
                "name": "enrollment_date",
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
                "name": "pre_training_performance",
                "type": "String",
                "length": 255
            },
            {
                "name": "post_training_performance",
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
                "name": "ix_partner_training_training_id",
                "columns": ["training_id"]
            },
            {
                "name": "ix_partner_training_training_type",
                "columns": ["training_type"]
            },
            {
                "name": "ix_partner_training_enrollment_date",
                "columns": ["enrollment_date"]
            },
            {
                "name": "ix_partner_training_completion_date",
                "columns": ["completion_date"]
            },
            {
                "name": "ix_partner_training_completion_status",
                "columns": ["completion_status"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
PartnerTraining "0..*" -- "0..*" ChannelPartner : enrolled in >
PartnerTraining "1" -- "0..*" TrainingCompletion : has >
TrainingCompletion "1" -- "1" ChannelPartner : completed by >
TrainingCompletion "1" -- "0..1" PerformanceMetric : impacts >
' Relationships to Related Objects
PartnerTraining "1" -- "*" AccountPlan : relates to
PartnerTraining "1" -- "*" Assessment : relates to
PartnerTraining "1" -- "*" Certification : relates to
PartnerTraining "1" -- "*" ChannelConflict : relates to
PartnerTraining "1" -- "*" ChannelDeal : relates to
PartnerTraining "1" -- "*" ChannelMarket : relates to
PartnerTraining "1" -- "*" ChannelPartner : relates to
PartnerTraining "1" -- "*" ChurnEvent : relates to
PartnerTraining "1" -- "*" Co-marketingCampaign : relates to
PartnerTraining "1" -- "*" CoachingSession : relates to
PartnerTraining "1" -- "*" Contract : relates to
PartnerTraining "1" -- "*" Customer : relates to
PartnerTraining "1" -- "*" CustomerAdvocacyProgram : relates to
PartnerTraining "1" -- "*" CustomerCohort : relates to
PartnerTraining "1" -- "*" CustomerCommunity : relates to
PartnerTraining "1" -- "*" CustomerEducation : relates to
PartnerTraining "1" -- "*" CustomerFeedback : relates to
PartnerTraining "1" -- "*" CustomerGoal : relates to
PartnerTraining "1" -- "*" CustomerHealthRecord : relates to
PartnerTraining "1" -- "*" CustomerJourney : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "PARTNER_TRAINING_COMPLETION_RATE",
            "PARTNER_SALES_TRAINING_EFFICACY"
        ],
        "key_attributes": [
            "training_id",
            "training_name",
            "training_type",
            "duration",
            "completion_requirements",
            "enrollment_date",
            "completion_date",
            "completion_status",
            "pre_training_performance",
            "post_training_performance"
        ],
        "related_objects": ["Account Plan", "Assessment", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}

)
