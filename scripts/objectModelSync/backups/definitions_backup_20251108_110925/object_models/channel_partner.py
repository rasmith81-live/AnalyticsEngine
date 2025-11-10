"""
Channel Partner Object Model

Represents external partners who sell products/services on behalf of the company.
"""

from analytics_models import ObjectModel

CHANNEL_PARTNER = ObjectModel(
    name="Channel Partner",
    code="CHANNEL_PARTNER",
    description="External partners in the indirect sales channel",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ChannelPartner {
}

class Deal {
}

class Lead {
}

class Revenue {
}

class Training {
}

class SupportTicket {
}

class CoMarketingCampaign {
}

class Customer {
}

class Market {
}

class PartnerAgreement {
}

class PerformanceScorecard {
}

' Relationships
ChannelPartner "1" -- "0..*" Deal : closes >
ChannelPartner "1" -- "0..*" Lead : receives >
ChannelPartner "1" -- "0..*" Revenue : generates >
ChannelPartner "1" -- "0..*" Training : completes >
ChannelPartner "1" -- "0..*" SupportTicket : creates >
ChannelPartner "0..*" -- "0..*" CoMarketingCampaign : participates in >
ChannelPartner "1" -- "0..*" Customer : acquires >
ChannelPartner "0..*" -- "0..*" Market : covers >
ChannelPartner "1" -- "1" PartnerAgreement : has >
ChannelPartner "1" -- "0..*" PerformanceScorecard : evaluated by >

@enduml

' Related Objects

class Assessment {
}

class Contract {
}

class Opportunity {
}

class Product {
}

class Sale {
}

class SalesPipeline {
}

class SalesQuota {
}

class SalesRepresentative {
}

class SalesTeam {
}

class Subscription {
}

' Relationships to Related Objects
ChannelPartner "1" -- "*" Assessment : relates to
ChannelPartner "1" -- "*" Contract : relates to
ChannelPartner "1" -- "*" Customer : relates to
ChannelPartner "1" -- "*" Deal : relates to
ChannelPartner "1" -- "*" Lead : relates to
ChannelPartner "1" -- "*" Opportunity : relates to
ChannelPartner "1" -- "*" PerformanceScorecard : relates to
ChannelPartner "1" -- "*" Product : relates to
ChannelPartner "1" -- "*" Sale : relates to
ChannelPartner "1" -- "*" SalesPipeline : relates to
ChannelPartner "1" -- "*" SalesQuota : relates to
ChannelPartner "1" -- "*" SalesRepresentative : relates to
ChannelPartner "1" -- "*" SalesTeam : relates to
ChannelPartner "1" -- "*" Subscription : relates to
ChannelPartner "1" -- "*" SupportTicket : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "related_kpis": [
            "NUMBER_OF_ACTIVE_CHANNEL_PARTNERS",
            "CHANNEL_PARTNER_GROWTH_RATE",
            "PARTNER_CHURN_RATE",
            "PARTNER_RETENTION_RATE",
            "PARTNER_SATISFACTION_INDEX",
            "PARTNER_LOYALTY_INDEX",
            "PARTNER_ENGAGEMENT_SCORE",
            "PARTNER_LIFECYCLE_VALUE",
            "PARTNER_PROFITABILITY",
            "PARTNER_CONTRIBUTION_MARGIN",
            "PARTNER_COVERAGE_RATIO",
            "PARTNER_ENABLEMENT_EFFECTIVENESS",
            "PARTNER_BRAND_ALIGNMENT",
            "PARTNER_PROGRAM_COMPLIANCE_RATE"
        ],
        "key_attributes": [
            "partner_id",
            "partner_name",
            "partner_type",
            "tier",
            "status",
            "region",
            "onboarding_date",
            "contract_start_date",
            "satisfaction_score",
            "loyalty_score",
            "engagement_score",
            "compliance_status"
        ],
        "related_objects": ["Assessment", "Contract", "Customer", "Deal", "Lead", "Opportunity", "Performance Scorecard", "Product", "Sale", "Sales Pipeline", "Sales Quota", "Sales Representative", "Sales Team", "Subscription", "Support Ticket"]}
)
