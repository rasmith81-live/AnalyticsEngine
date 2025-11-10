"""
Product Adoption Object Model

Represents customer product adoption tracking and feature usage.
"""

from analytics_models import ObjectModel

PRODUCT_ADOPTION = ObjectModel(
    name="Product Adoption",
    code="PRODUCT_ADOPTION",
    description="Customer product adoption tracking and feature usage metrics",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ProductAdoption {
}

class Customer {
}

class Product {
}

class Feature {
}

class AdoptionMilestone {
}

' Relationships
Customer "1" -- "0..*" ProductAdoption : has >
Product "1" -- "0..*" ProductAdoption : tracked by >
ProductAdoption "1" -- "0..*" Feature : includes >
ProductAdoption "1" -- "0..*" AdoptionMilestone : progresses through >

@enduml

' Relationships to Related Objects
ProductAdoption "1" -- "*" Account : relates to
ProductAdoption "1" -- "*" AccountPenetration : relates to
ProductAdoption "1" -- "*" AccountPlan : relates to
ProductAdoption "1" -- "*" AccountRisk : relates to
ProductAdoption "1" -- "*" Appointment : relates to
ProductAdoption "1" -- "*" Certification : relates to
ProductAdoption "1" -- "*" ChannelConflict : relates to
ProductAdoption "1" -- "*" ChannelDeal : relates to
ProductAdoption "1" -- "*" ChannelMarket : relates to
ProductAdoption "1" -- "*" ChannelPartner : relates to
ProductAdoption "1" -- "*" CompetitiveAnalysis : relates to
ProductAdoption "1" -- "*" Customer : relates to
ProductAdoption "1" -- "*" CustomerAdvocacyProgram : relates to
ProductAdoption "1" -- "*" CustomerCohort : relates to
ProductAdoption "1" -- "*" CustomerCommunity : relates to
ProductAdoption "1" -- "*" CustomerEducation : relates to
ProductAdoption "1" -- "*" CustomerFeedback : relates to
ProductAdoption "1" -- "*" CustomerGoal : relates to
ProductAdoption "1" -- "*" CustomerHealthRecord : relates to
ProductAdoption "1" -- "*" CustomerJourney : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "PRODUCT_ADOPTION_RATE",
            "CUSTOMER_SUCCESS_SOFTWARE_ADOPTION_RATE",
            "PRODUCT_ONBOARDING_SUCCESS_RATE"
        ],
        "key_attributes": [
            "adoption_id",
            "customer_id",
            "product_id",
            "adoption_stage",
            "features_adopted",
            "usage_frequency",
            "time_to_adopt",
            "adoption_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]}
)
