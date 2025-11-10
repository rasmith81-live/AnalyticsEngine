"""
Customer Advocacy Program Object Model

Represents customer advocacy programs and activities.
"""

from analytics_models import ObjectModel

CUSTOMER_ADVOCACY_PROGRAM = ObjectModel(
    name="Customer Advocacy Program",
    code="CUSTOMER_ADVOCACY_PROGRAM",
    description="Customer advocacy programs and activities",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerAdvocacyProgram {
}

class Customer {
}

class AdvocacyAction {
}

class Testimonial {
}

class CaseStudy {
}

' Relationships
CustomerAdvocacyProgram "0..*" -- "0..*" Customer : has advocates >
CustomerAdvocacyProgram "1" -- "0..*" AdvocacyAction : tracks >
AdvocacyAction "1" -- "0..1" Testimonial : may produce >
AdvocacyAction "1" -- "0..1" CaseStudy : may produce >

@enduml

' Relationships to Related Objects
CustomerAdvocacyProgram "1" -- "*" Account : relates to
CustomerAdvocacyProgram "1" -- "*" AccountPenetration : relates to
CustomerAdvocacyProgram "1" -- "*" AccountPlan : relates to
CustomerAdvocacyProgram "1" -- "*" AccountRisk : relates to
CustomerAdvocacyProgram "1" -- "*" Call : relates to
CustomerAdvocacyProgram "1" -- "*" Certification : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelConflict : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelDeal : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelMarket : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelPartner : relates to
CustomerAdvocacyProgram "1" -- "*" ChurnEvent : relates to
CustomerAdvocacyProgram "1" -- "*" CompetitiveAnalysis : relates to
CustomerAdvocacyProgram "1" -- "*" Contract : relates to
CustomerAdvocacyProgram "1" -- "*" Customer : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerCohort : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerCommunity : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerEducation : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerFeedback : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerGoal : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerHealthRecord : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "ADVOCACY_ACTIONS",
            "CUSTOMER_REFERENCEABILITY_RATE"
        ],
        "key_attributes": [
            "program_id",
            "name",
            "participant_count",
            "advocacy_actions_count",
            "testimonials_count",
            "case_studies_count",
            "referrals_generated"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}
)
