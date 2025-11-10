"""
Partner Training Object Model

Represents training programs and completions for channel partners.
"""

from analytics_models import ObjectModel

PARTNER_TRAINING = ObjectModel(
    name="Partner Training",
    code="PARTNER_TRAINING",
    description="Training programs for channel partner enablement",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class PartnerTraining {
}

class ChannelPartner {
}

class TrainingCompletion {
}

class PerformanceMetric {
}

' Relationships
PartnerTraining "0..*" -- "0..*" ChannelPartner : enrolled in >
PartnerTraining "1" -- "0..*" TrainingCompletion : has >
TrainingCompletion "1" -- "1" ChannelPartner : completed by >
TrainingCompletion "1" -- "0..1" PerformanceMetric : impacts >

@enduml

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
""",
    
    is_active=True,
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
