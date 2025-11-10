"""
Sales Assessment Object Model

Represents sales skill and knowledge assessments.
"""

from analytics_models import ObjectModel

SALES_ASSESSMENT = ObjectModel(
    name="Sales Assessment",
    code="SALES_ASSESSMENT",
    description="Sales skill and knowledge assessments and certifications",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesAssessment {
}

class SalesRepresentative {
}

class SalesTrainingProgram {
}

class Certification {
}

' Relationships
SalesRepresentative "1" -- "0..*" SalesAssessment : takes >
SalesTrainingProgram "1" -- "0..*" SalesAssessment : includes >
SalesAssessment "1" -- "0..1" Certification : leads to >

@enduml

' Relationships to Related Objects
SalesAssessment "1" -- "*" Account : relates to
SalesAssessment "1" -- "*" AccountPenetration : relates to
SalesAssessment "1" -- "*" AccountPlan : relates to
SalesAssessment "1" -- "*" AccountRisk : relates to
SalesAssessment "1" -- "*" Appointment : relates to
SalesAssessment "1" -- "*" Assessment : relates to
SalesAssessment "1" -- "*" Call : relates to
SalesAssessment "1" -- "*" Certification : relates to
SalesAssessment "1" -- "*" ChannelConflict : relates to
SalesAssessment "1" -- "*" ChannelDeal : relates to
SalesAssessment "1" -- "*" ChannelMarket : relates to
SalesAssessment "1" -- "*" ChannelPartner : relates to
SalesAssessment "1" -- "*" ChurnEvent : relates to
SalesAssessment "1" -- "*" Co-marketingCampaign : relates to
SalesAssessment "1" -- "*" CoachingSession : relates to
SalesAssessment "1" -- "*" CompetitiveAnalysis : relates to
SalesAssessment "1" -- "*" Contract : relates to
SalesAssessment "1" -- "*" Customer : relates to
SalesAssessment "1" -- "*" CustomerAdvocacyProgram : relates to
SalesAssessment "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_SKILL_ASSESSMENT_COMPLETION_RATE",
            "SALES_CERTIFICATION_RATE",
            "COMPETITOR_KNOWLEDGE_ASSESSMENT_SCORES"
        ],
        "key_attributes": [
            "assessment_id",
            "rep_id",
            "type",
            "score",
            "completion_date",
            "certification_earned"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
