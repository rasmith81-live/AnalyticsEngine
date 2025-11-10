"""
Partner Agreement Object Model

Represents contracts and agreements with channel partners.
"""

PARTNER_AGREEMENT = {
    "code": "PARTNER_AGREEMENT",
    "name": "Partner Agreement",
    "description": "Contracts and agreements with channel partners",
    "table_schema": {"table_name": "partner_agreement", "class_name": "Partner Agreement", "columns": [{"name": "agreement_id", "type": "Integer", "index": True}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "renewal_date", "type": "DateTime", "index": True}, {"name": "terms", "type": "String", "length": 255}, {"name": "compliance_status", "type": "String", "length": 50, "index": True}, {"name": "renewal_status", "type": "String", "length": 50, "index": True}, {"name": "tier", "type": "String", "length": 255}, {"name": "commission_structure", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_partner_agreement_agreement_id", "columns": ["agreement_id"]}, {"name": "ix_partner_agreement_start_date", "columns": ["start_date"]}, {"name": "ix_partner_agreement_end_date", "columns": ["end_date"]}, {"name": "ix_partner_agreement_renewal_date", "columns": ["renewal_date"]}, {"name": "ix_partner_agreement_compliance_status", "columns": ["compliance_status"]}, {"name": "ix_partner_agreement_renewal_status", "columns": ["renewal_status"]}]},
    "schema_definition": """
    @startuml
' Relationships
ChannelPartner "1" -- "1" PartnerAgreement : has >
PartnerAgreement "1" -- "0..*" Renewal : has >
PartnerAgreement "1" -- "0..*" ComplianceRecord : tracks >
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
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "related_kpis": ["PARTNER_RENEWAL_RATE", "PARTNER_PROGRAM_COMPLIANCE_RATE"], "key_attributes": ["agreement_id", "start_date", "end_date", "renewal_date", "terms", "compliance_status", "renewal_status", "tier", "commission_structure"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]},
}
