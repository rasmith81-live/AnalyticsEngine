"""
Referral Object Model

Represents customer referrals and word-of-mouth leads.
"""

from analytics_models import ObjectModel

REFERRAL = ObjectModel(
    name="Referral",
    code="REFERRAL",
    description="Leads generated through customer referrals",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Referral {
}

class Customer {
}

class Lead {
}

class Opportunity {
}

' Relationships
Customer "1" -- "0..*" Referral : generates >
Referral "1" -- "1" Lead : creates >
Referral "1" -- "0..1" Opportunity : becomes >

@enduml

' Relationships to Related Objects
Referral "1" -- "*" Account : relates to
Referral "1" -- "*" AccountPenetration : relates to
Referral "1" -- "*" AccountPlan : relates to
Referral "1" -- "*" AccountRisk : relates to
Referral "1" -- "*" KeyAccount : relates to
Referral "1" -- "*" KeyAccountManager : relates to
Referral "1" -- "*" LoyaltyProgram : relates to
Referral "1" -- "*" RenewalManagement : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CUSTOMER_RETENTION", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
        "related_kpis": [
            "REFERRAL_RATE"
        ],
        "key_attributes": [
            "referrer_customer_id",
            "referred_contact",
            "referral_date",
            "status",
            "converted",
            "incentive_given"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Loyalty Program", "Renewal Management"]}
)
