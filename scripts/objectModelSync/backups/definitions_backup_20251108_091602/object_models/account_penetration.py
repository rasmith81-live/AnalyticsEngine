"""
Account Penetration Object Model

Represents account penetration metrics and analysis.
"""

from analytics_models import ObjectModel

ACCOUNT_PENETRATION = ObjectModel(
    name="Account Penetration",
    code="ACCOUNT_PENETRATION",
    description="Account penetration and market share analysis",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class AccountPenetration {
}

class KeyAccount {
}

class Product {
}

class Department {
}

' Relationships
KeyAccount "1" -- "1" AccountPenetration : measured by >
AccountPenetration "1" -- "0..*" Product : tracks adoption of >
AccountPenetration "1" -- "0..*" Department : covers >

@enduml

' Relationships to Related Objects
AccountPenetration "1" -- "*" Account : relates to
AccountPenetration "1" -- "*" AccountPlan : relates to
AccountPenetration "1" -- "*" AccountRisk : relates to
AccountPenetration "1" -- "*" Call : relates to
AccountPenetration "1" -- "*" ChannelConflict : relates to
AccountPenetration "1" -- "*" ChannelDeal : manages
AccountPenetration "1" -- "*" ChannelMarket : relates to
AccountPenetration "1" -- "*" ChannelPartner : relates to
AccountPenetration "1" -- "*" CompetitiveAnalysis : relates to
AccountPenetration "1" -- "*" Contract : relates to
AccountPenetration "1" -- "*" Customer : relates to
AccountPenetration "1" -- "*" CustomerAdvocacyProgram : relates to
AccountPenetration "1" -- "*" CustomerCohort : relates to
AccountPenetration "1" -- "*" CustomerCommunity : relates to
AccountPenetration "1" -- "*" CustomerEducation : relates to
AccountPenetration "1" -- "*" CustomerFeedback : relates to
AccountPenetration "1" -- "*" CustomerGoal : relates to
AccountPenetration "1" -- "*" CustomerHealthRecord : relates to
AccountPenetration "1" -- "*" CustomerJourney : relates to
AccountPenetration "1" -- "*" CustomerOnboarding : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "ACCOUNT_PENETRATION_INDEX",
            "ACCOUNT_SATURATION_INDEX",
            "ACCOUNT_SHARE_OF_WALLET"
        ],
        "key_attributes": [
            "penetration_id",
            "account_id",
            "departments_served",
            "total_departments",
            "products_adopted",
            "total_products",
            "wallet_share",
            "saturation_level",
            "penetration_score"
        ],
        "related_objects": ["Account", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]}
)
