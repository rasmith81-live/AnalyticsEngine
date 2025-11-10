"""
Partner Agreement Object Model

Represents contracts and agreements with channel partners.
"""

from analytics_models import ObjectModel

PARTNER_AGREEMENT = ObjectModel(
    name="Partner Agreement",
    code="PARTNER_AGREEMENT",
    description="Contracts and agreements with channel partners",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class PartnerAgreement {
}

class ChannelPartner {
}

class Renewal {
}

class ComplianceRecord {
}

' Relationships
ChannelPartner "1" -- "1" PartnerAgreement : has >
PartnerAgreement "1" -- "0..*" Renewal : has >
PartnerAgreement "1" -- "0..*" ComplianceRecord : tracks >

@enduml

' Relationships to Related Objects
PartnerAgreement "1" -- "*" Account : relates to
PartnerAgreement "1" -- "*" AccountPenetration : relates to
PartnerAgreement "1" -- "*" AccountPlan : relates to
PartnerAgreement "1" -- "*" AccountRisk : relates to
PartnerAgreement "1" -- "*" Assessment : relates to
PartnerAgreement "1" -- "*" ChannelConflict : relates to
PartnerAgreement "1" -- "*" ChannelDeal : relates to
PartnerAgreement "1" -- "*" ChannelMarket : relates to
PartnerAgreement "1" -- "*" ChannelPartner : relates to
PartnerAgreement "1" -- "*" ChurnEvent : relates to
PartnerAgreement "1" -- "*" Co-marketingCampaign : relates to
PartnerAgreement "1" -- "*" CompetitiveAnalysis : relates to
PartnerAgreement "1" -- "*" Contract : relates to
PartnerAgreement "1" -- "*" Customer : relates to
PartnerAgreement "1" -- "*" CustomerAdvocacyProgram : relates to
PartnerAgreement "1" -- "*" CustomerCohort : relates to
PartnerAgreement "1" -- "*" CustomerCommunity : relates to
PartnerAgreement "1" -- "*" CustomerEducation : relates to
PartnerAgreement "1" -- "*" CustomerFeedback : relates to
PartnerAgreement "1" -- "*" CustomerGoal : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
        "related_kpis": [
            "PARTNER_RENEWAL_RATE",
            "PARTNER_PROGRAM_COMPLIANCE_RATE"
        ],
        "key_attributes": [
            "agreement_id",
            "start_date",
            "end_date",
            "renewal_date",
            "terms",
            "compliance_status",
            "renewal_status",
            "tier",
            "commission_structure"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}
)
