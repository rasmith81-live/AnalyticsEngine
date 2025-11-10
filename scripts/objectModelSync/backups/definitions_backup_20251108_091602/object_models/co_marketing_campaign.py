"""
Co-Marketing Campaign Object Model

Represents joint marketing efforts between company and channel partners.
"""

from analytics_models import ObjectModel

CO_MARKETING_CAMPAIGN = ObjectModel(
    name="Co-Marketing Campaign",
    code="CO_MARKETING_CAMPAIGN",
    description="Joint marketing campaigns with channel partners",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class CoMarketingCampaign {
}

class ChannelPartner {
}

class Lead {
}

class Revenue {
}

' Relationships
CoMarketingCampaign "0..*" -- "1..*" ChannelPartner : involves >
CoMarketingCampaign "1" -- "0..*" Lead : generates >
CoMarketingCampaign "1" -- "0..*" Revenue : produces >

@enduml

' Relationships to Related Objects
Co-marketingCampaign "1" -- "*" Assessment : relates to
Co-marketingCampaign "1" -- "*" ChannelConflict : relates to
Co-marketingCampaign "1" -- "*" ChannelDeal : relates to
Co-marketingCampaign "1" -- "*" ChannelMarket : relates to
Co-marketingCampaign "1" -- "*" ChannelPartner : relates to
Co-marketingCampaign "1" -- "*" Customer : relates to
Co-marketingCampaign "1" -- "*" Lead : relates to
Co-marketingCampaign "1" -- "*" PartnerAgreement : relates to
Co-marketingCampaign "1" -- "*" PartnerIncentive : relates to
Co-marketingCampaign "1" -- "*" PartnerPerformanceScorecard : relates to
Co-marketingCampaign "1" -- "*" PartnerPortal : relates to
Co-marketingCampaign "1" -- "*" PartnerTraining : relates to
Co-marketingCampaign "1" -- "*" RevenueForecast : relates to
Co-marketingCampaign "1" -- "*" SalesActivity : relates to
Co-marketingCampaign "1" -- "*" SalesAppointment : relates to
Co-marketingCampaign "1" -- "*" SalesAssessment : relates to
Co-marketingCampaign "1" -- "*" SalesCall : relates to
Co-marketingCampaign "1" -- "*" SalesCoachingSession : relates to
Co-marketingCampaign "1" -- "*" SalesContent : relates to
Co-marketingCampaign "1" -- "*" SalesDashboard : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "related_kpis": [
            "CO_MARKETING_CONTRIBUTION"
        ],
        "key_attributes": [
            "campaign_id",
            "campaign_name",
            "start_date",
            "end_date",
            "budget",
            "investment",
            "leads_generated",
            "revenue_generated",
            "roi",
            "participating_partners"
        ],
        "related_objects": ["Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Lead", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard"]}
)
