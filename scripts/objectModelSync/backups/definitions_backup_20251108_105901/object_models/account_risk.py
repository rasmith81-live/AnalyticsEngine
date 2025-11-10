"""
Account Risk Object Model

Represents risk assessment and monitoring for key accounts.
"""

from analytics_models import ObjectModel

ACCOUNT_RISK = ObjectModel(
    name="Account Risk",
    code="ACCOUNT_RISK",
    description="Risk assessment and monitoring for strategic accounts",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class AccountRisk {
}

class KeyAccount {
}

class KeyAccountManager {
}

class RiskFactor {
}

class MitigationPlan {
}

' Relationships
KeyAccount "1" -- "0..1" AccountRisk : monitored for >
KeyAccountManager "1" -- "0..*" AccountRisk : monitors >
AccountRisk "1" -- "1..*" RiskFactor : has >
AccountRisk "1" -- "0..1" MitigationPlan : has >

@enduml

' Relationships to Related Objects
AccountRisk "1" -- "*" Account : relates to
AccountRisk "1" -- "*" AccountPenetration : relates to
AccountRisk "1" -- "*" AccountPlan : relates to
AccountRisk "1" -- "*" Call : relates to
AccountRisk "1" -- "*" ChannelConflict : relates to
AccountRisk "1" -- "*" ChannelDeal : manages
AccountRisk "1" -- "*" ChannelMarket : relates to
AccountRisk "1" -- "*" ChannelPartner : relates to
AccountRisk "1" -- "*" ChurnEvent : relates to
AccountRisk "1" -- "*" CompetitiveAnalysis : relates to
AccountRisk "1" -- "*" Contract : relates to
AccountRisk "1" -- "*" Customer : relates to
AccountRisk "1" -- "*" CustomerAdvocacyProgram : relates to
AccountRisk "1" -- "*" CustomerCohort : relates to
AccountRisk "1" -- "*" CustomerCommunity : relates to
AccountRisk "1" -- "*" CustomerEducation : relates to
AccountRisk "1" -- "*" CustomerFeedback : relates to
AccountRisk "1" -- "*" CustomerGoal : relates to
AccountRisk "1" -- "*" CustomerHealthRecord : relates to
AccountRisk "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "CLIENT_RISK_EXPOSURE",
            "CUSTOMER_HEALTH_SCORE"
        ],
        "key_attributes": [
            "risk_id",
            "account_id",
            "kam_id",
            "risk_level",
            "risk_factors",
            "exposure_value",
            "mitigation_plan",
            "last_assessment_date"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
