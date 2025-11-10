"""
Customer Health Record Object Model

Represents customer health tracking and predictive churn indicators.
"""

from analytics_models import ObjectModel

CUSTOMER_HEALTH_RECORD = ObjectModel(
    name="Customer Health Record",
    code="CUSTOMER_HEALTH_RECORD",
    description="Customer health tracking with predictive churn indicators",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CustomerHealthRecord {
}

class Customer {
}

class HealthMetric {
}

class ChurnRiskIndicator {
}

class Intervention {
}

' Relationships
Customer "1" -- "0..*" CustomerHealthRecord : tracked by >
CustomerHealthRecord "1" -- "1..*" HealthMetric : includes >
CustomerHealthRecord "1" -- "0..1" ChurnRiskIndicator : has >
ChurnRiskIndicator "1" -- "0..*" Intervention : triggers >

@enduml

' Relationships to Related Objects
CustomerHealthRecord "1" -- "*" Account : relates to
CustomerHealthRecord "1" -- "*" AccountPenetration : relates to
CustomerHealthRecord "1" -- "*" AccountPlan : relates to
CustomerHealthRecord "1" -- "*" AccountRisk : relates to
CustomerHealthRecord "1" -- "*" Call : relates to
CustomerHealthRecord "1" -- "*" ChannelConflict : relates to
CustomerHealthRecord "1" -- "*" ChannelDeal : relates to
CustomerHealthRecord "1" -- "*" ChannelMarket : relates to
CustomerHealthRecord "1" -- "*" ChannelPartner : relates to
CustomerHealthRecord "1" -- "*" ChurnEvent : relates to
CustomerHealthRecord "1" -- "*" CompetitiveAnalysis : relates to
CustomerHealthRecord "1" -- "*" Contract : relates to
CustomerHealthRecord "1" -- "*" Customer : relates to
CustomerHealthRecord "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerHealthRecord "1" -- "*" CustomerCohort : relates to
CustomerHealthRecord "1" -- "*" CustomerCommunity : relates to
CustomerHealthRecord "1" -- "*" CustomerEducation : relates to
CustomerHealthRecord "1" -- "*" CustomerFeedback : relates to
CustomerHealthRecord "1" -- "*" CustomerGoal : relates to
CustomerHealthRecord "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CUSTOMER_HEALTH_SCORE"
        ],
        "key_attributes": [
            "health_record_id",
            "customer_id",
            "date",
            "health_score",
            "usage_score",
            "engagement_score",
            "satisfaction_score",
            "churn_risk_level",
            "intervention_required"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Journey"]}
)
