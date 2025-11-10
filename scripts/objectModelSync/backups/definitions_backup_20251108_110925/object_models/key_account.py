"""
Key Account Object Model

Represents strategic, high-value customer accounts requiring dedicated management.
"""

from analytics_models import ObjectModel

KEY_ACCOUNT = ObjectModel(
    name="Key Account",
    code="KEY_ACCOUNT",
    description="Strategic, high-value customer accounts with dedicated account management",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class KeyAccount {
}

class KeyAccountManager {
}

class AccountPlan {
}

class Stakeholder {
}

class StrategicReview {
}

class AccountPenetration {
}

class AccountRisk {
}

' Relationships
KeyAccountManager "1" -- "0..*" KeyAccount : manages >
KeyAccount "1" -- "1" AccountPlan : has >
KeyAccount "1" -- "1..*" Stakeholder : has >
KeyAccount "1" -- "0..*" StrategicReview : reviewed in >
KeyAccount "1" -- "1" AccountPenetration : measured by >
KeyAccount "1" -- "0..1" AccountRisk : monitored for >

@enduml

' Relationships to Related Objects
KeyAccount "1" -- "*" Account : relates to
KeyAccount "1" -- "*" AccountPenetration : relates to
KeyAccount "1" -- "*" AccountPlan : relates to
KeyAccount "1" -- "*" AccountRisk : relates to
KeyAccount "1" -- "*" Call : relates to
KeyAccount "1" -- "*" ChannelConflict : relates to
KeyAccount "1" -- "*" ChannelDeal : manages
KeyAccount "1" -- "*" ChannelMarket : relates to
KeyAccount "1" -- "*" ChannelPartner : relates to
KeyAccount "1" -- "*" CompetitiveAnalysis : relates to
KeyAccount "1" -- "*" Contract : relates to
KeyAccount "1" -- "*" Customer : relates to
KeyAccount "1" -- "*" CustomerAdvocacyProgram : relates to
KeyAccount "1" -- "*" CustomerCohort : relates to
KeyAccount "1" -- "*" CustomerCommunity : relates to
KeyAccount "1" -- "*" CustomerEducation : relates to
KeyAccount "1" -- "*" CustomerFeedback : relates to
KeyAccount "1" -- "*" CustomerGoal : relates to
KeyAccount "1" -- "*" CustomerHealthRecord : relates to
KeyAccount "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "ACCOUNT_COVERAGE_RATIO",
            "ACCOUNT_PENETRATION_INDEX",
            "ACCOUNT_SATURATION_INDEX",
            "ACCOUNT_SHARE_OF_WALLET",
            "CUSTOMER_HEALTH_SCORE",
            "CLIENT_RISK_EXPOSURE",
            "STRATEGIC_ACCOUNT_GROWTH",
            "YEAR_OVER_YEAR_ACCOUNT_GROWTH"
        ],
        "key_attributes": [
            "account_id",
            "account_name",
            "account_tier",
            "strategic_value",
            "share_of_wallet",
            "penetration_index",
            "saturation_index",
            "health_score",
            "risk_exposure",
            "annual_contract_value"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
