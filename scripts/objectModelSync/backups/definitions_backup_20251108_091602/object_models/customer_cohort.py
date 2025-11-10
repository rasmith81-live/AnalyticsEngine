"""
Customer Cohort Object Model

Represents customer cohorts for retention and trend analysis.
"""

from analytics_models import ObjectModel

CUSTOMER_COHORT = ObjectModel(
    name="Customer Cohort",
    code="CUSTOMER_COHORT",
    description="Customer cohorts for retention and trend analysis",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerCohort {
}

class Customer {
}

class RetentionMetric {
}

' Relationships
CustomerCohort "0..*" -- "0..*" Customer : contains >
CustomerCohort "1" -- "0..*" RetentionMetric : tracked by >

@enduml

' Relationships to Related Objects
CustomerCohort "1" -- "*" Account : relates to
CustomerCohort "1" -- "*" AccountPenetration : relates to
CustomerCohort "1" -- "*" AccountPlan : relates to
CustomerCohort "1" -- "*" AccountRisk : relates to
CustomerCohort "1" -- "*" Call : relates to
CustomerCohort "1" -- "*" ChannelConflict : relates to
CustomerCohort "1" -- "*" ChannelDeal : relates to
CustomerCohort "1" -- "*" ChannelMarket : relates to
CustomerCohort "1" -- "*" ChannelPartner : relates to
CustomerCohort "1" -- "*" ChurnEvent : relates to
CustomerCohort "1" -- "*" CompetitiveAnalysis : relates to
CustomerCohort "1" -- "*" Contract : relates to
CustomerCohort "1" -- "*" Customer : relates to
CustomerCohort "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerCohort "1" -- "*" CustomerCommunity : relates to
CustomerCohort "1" -- "*" CustomerEducation : relates to
CustomerCohort "1" -- "*" CustomerFeedback : relates to
CustomerCohort "1" -- "*" CustomerGoal : relates to
CustomerCohort "1" -- "*" CustomerHealthRecord : relates to
CustomerCohort "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_COHORT_RETENTION_RATE"
        ],
        "key_attributes": [
            "cohort_id",
            "cohort_name",
            "acquisition_period",
            "customer_count",
            "retention_rate",
            "churn_rate",
            "cohort_age"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
