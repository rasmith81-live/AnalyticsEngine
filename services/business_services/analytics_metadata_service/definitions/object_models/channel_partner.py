"""
Channel Partner Object Model

Represents external partners who sell products/services on behalf of the company.
"""

CHANNEL_PARTNER = {
    "code": "CHANNEL_PARTNER",
    "name": "Channel Partner",
    "description": "External partners in the indirect sales channel",
    "table_schema": {"table_name": "channel_partner", "class_name": "Channel Partner", "columns": [{"name": "partner_id", "type": "Integer", "index": True}, {"name": "partner_name", "type": "String", "length": 255}, {"name": "partner_type", "type": "String", "length": 50, "index": True}, {"name": "tier", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "region", "type": "String", "length": 255}, {"name": "onboarding_date", "type": "DateTime", "index": True}, {"name": "contract_start_date", "type": "DateTime", "index": True}, {"name": "satisfaction_score", "type": "Float"}, {"name": "loyalty_score", "type": "Float"}, {"name": "engagement_score", "type": "Float"}, {"name": "compliance_status", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_channel_partner_partner_id", "columns": ["partner_id"]}, {"name": "ix_channel_partner_partner_type", "columns": ["partner_type"]}, {"name": "ix_channel_partner_onboarding_date", "columns": ["onboarding_date"]}, {"name": "ix_channel_partner_contract_start_date", "columns": ["contract_start_date"]}, {"name": "ix_channel_partner_compliance_status", "columns": ["compliance_status"]}]},
    "schema_definition": """
    @startuml
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
' Related Objects
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
@enduml
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "related_kpis": ["NUMBER_OF_ACTIVE_CHANNEL_PARTNERS", "CHANNEL_PARTNER_GROWTH_RATE", "PARTNER_CHURN_RATE", "PARTNER_RETENTION_RATE", "PARTNER_SATISFACTION_INDEX", "PARTNER_LOYALTY_INDEX", "PARTNER_ENGAGEMENT_SCORE", "PARTNER_LIFECYCLE_VALUE", "PARTNER_PROFITABILITY", "PARTNER_CONTRIBUTION_MARGIN", "PARTNER_COVERAGE_RATIO", "PARTNER_ENABLEMENT_EFFECTIVENESS", "PARTNER_BRAND_ALIGNMENT", "PARTNER_PROGRAM_COMPLIANCE_RATE"], "key_attributes": ["partner_id", "partner_name", "partner_type", "tier", "status", "region", "onboarding_date", "contract_start_date", "satisfaction_score", "loyalty_score", "engagement_score", "compliance_status"], "related_objects": ["Assessment", "Contract", "Customer", "Deal", "Lead", "Opportunity", "Performance Scorecard", "Product", "Sale", "Sales Pipeline", "Sales Quota", "Sales Representative", "Sales Team", "Subscription", "Support Ticket"]},
}
