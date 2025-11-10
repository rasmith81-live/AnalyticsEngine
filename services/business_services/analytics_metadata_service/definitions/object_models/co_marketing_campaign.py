"""
Co-Marketing Campaign Object Model

Represents joint marketing efforts between company and channel partners.
"""

CO_MARKETING_CAMPAIGN = {
    "code": "CO_MARKETING_CAMPAIGN",
    "name": "Co-Marketing Campaign",
    "description": "Joint marketing campaigns with channel partners",
    "table_schema": {"table_name": "co_marketing_campaign", "class_name": "Co-Marketing Campaign", "columns": [{"name": "campaign_id", "type": "Integer", "index": True}, {"name": "campaign_name", "type": "String", "length": 255}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "budget", "type": "String", "length": 255}, {"name": "investment", "type": "String", "length": 255}, {"name": "leads_generated", "type": "String", "length": 255}, {"name": "revenue_generated", "type": "String", "length": 255}, {"name": "roi", "type": "String", "length": 255}, {"name": "participating_partners", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_co_marketing_campaign_campaign_id", "columns": ["campaign_id"]}, {"name": "ix_co_marketing_campaign_start_date", "columns": ["start_date"]}, {"name": "ix_co_marketing_campaign_end_date", "columns": ["end_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
CoMarketingCampaign "0..*" -- "1..*" ChannelPartner : involves >
CoMarketingCampaign "1" -- "0..*" Lead : generates >
CoMarketingCampaign "1" -- "0..*" Revenue : produces >
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
@enduml
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "related_kpis": ["CO_MARKETING_CONTRIBUTION"], "key_attributes": ["campaign_id", "campaign_name", "start_date", "end_date", "budget", "investment", "leads_generated", "revenue_generated", "roi", "participating_partners"], "related_objects": ["Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Lead", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard"]},
}
