"""
Sales Training Program Object Model

Represents training programs for sales team development.
"""

from analytics_models import ObjectModel

SALES_TRAINING_PROGRAM = ObjectModel(
    name="Sales Training Program",
    code="SALES_TRAINING_PROGRAM",
    description="Training programs for sales team skill development and onboarding",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesTrainingProgram {
}

class SalesRepresentative {
}

class EnablementTeam {
}

class TrainingMaterial {
}

class SalesAssessment {
}

class Product {
}

' Relationships
SalesRepresentative "0..*" -- "0..*" SalesTrainingProgram : attends >
EnablementTeam "1" -- "0..*" SalesTrainingProgram : delivers >
SalesTrainingProgram "1" -- "0..*" TrainingMaterial : includes >
SalesTrainingProgram "1" -- "0..*" SalesAssessment : measured by >
SalesTrainingProgram "0..*" -- "0..*" Product : covers >

@enduml

' Relationships to Related Objects
SalesTrainingProgram "1" -- "*" Account : relates to
SalesTrainingProgram "1" -- "*" AccountPenetration : relates to
SalesTrainingProgram "1" -- "*" AccountPlan : relates to
SalesTrainingProgram "1" -- "*" AccountRisk : relates to
SalesTrainingProgram "1" -- "*" Appointment : relates to
SalesTrainingProgram "1" -- "*" Assessment : relates to
SalesTrainingProgram "1" -- "*" Call : relates to
SalesTrainingProgram "1" -- "*" Certification : relates to
SalesTrainingProgram "1" -- "*" ChannelConflict : relates to
SalesTrainingProgram "1" -- "*" ChannelDeal : relates to
SalesTrainingProgram "1" -- "*" ChannelMarket : relates to
SalesTrainingProgram "1" -- "*" ChannelPartner : relates to
SalesTrainingProgram "1" -- "*" ChurnEvent : relates to
SalesTrainingProgram "1" -- "*" Co-marketingCampaign : relates to
SalesTrainingProgram "1" -- "*" CoachingSession : relates to
SalesTrainingProgram "1" -- "*" CompetitiveAnalysis : relates to
SalesTrainingProgram "1" -- "*" Contract : relates to
SalesTrainingProgram "1" -- "*" Customer : relates to
SalesTrainingProgram "1" -- "*" CustomerAdvocacyProgram : relates to
SalesTrainingProgram "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_TRAINING_ATTENDANCE_RATE",
            "SALES_TRAINING_COMPLETION_RATE",
            "TRAINING_IMPACT_SCORE",
            "SALES_ONBOARDING_EFFICIENCY"
        ],
        "key_attributes": [
            "program_id",
            "name",
            "type",
            "duration",
            "completion_rate",
            "impact_score",
            "attendance_rate"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
