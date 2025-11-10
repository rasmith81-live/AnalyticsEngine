"""
Renewal Management Object Model

Represents renewal tracking and management processes.
"""

RENEWAL_MANAGEMENT = {
    "code": "RENEWAL_MANAGEMENT",
    "name": "Renewal Management",
    "description": "Renewal tracking and management processes",
    "table_schema": {"table_name": "renewal_management", "class_name": "Renewal Management", "columns": [{"name": "renewal_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "subscription_id", "type": "Integer", "index": True}, {"name": "csm_id", "type": "Integer", "index": True}, {"name": "renewal_date", "type": "DateTime", "index": True}, {"name": "intent_score", "type": "Float"}, {"name": "outcome", "type": "String", "length": 255}, {"name": "upgrade_downgrade_flag", "type": "String", "length": 255}, {"name": "value_change", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_renewal_management_renewal_id", "columns": ["renewal_id"]}, {"name": "ix_renewal_management_customer_id", "columns": ["customer_id"]}, {"name": "ix_renewal_management_subscription_id", "columns": ["subscription_id"]}, {"name": "ix_renewal_management_csm_id", "columns": ["csm_id"]}, {"name": "ix_renewal_management_renewal_date", "columns": ["renewal_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" RenewalManagement : has >
RenewalManagement "1" -- "1" Subscription : for >
RenewalManagement "0..*" -- "1" CustomerSuccessManager : managed by >
RenewalManagement "1" -- "0..1" RenewalIntent : tracked by >
' Relationships to Related Objects
RenewalManagement "1" -- "*" Account : relates to
RenewalManagement "1" -- "*" AccountPenetration : relates to
RenewalManagement "1" -- "*" AccountPlan : relates to
RenewalManagement "1" -- "*" AccountRisk : relates to
RenewalManagement "1" -- "*" Call : relates to
RenewalManagement "1" -- "*" ChannelConflict : relates to
RenewalManagement "1" -- "*" ChannelDeal : relates to
RenewalManagement "1" -- "*" ChannelMarket : relates to
RenewalManagement "1" -- "*" ChannelPartner : relates to
RenewalManagement "1" -- "*" ChurnEvent : relates to
RenewalManagement "1" -- "*" CompetitiveAnalysis : relates to
RenewalManagement "1" -- "*" Contract : relates to
RenewalManagement "1" -- "*" Customer : relates to
RenewalManagement "1" -- "*" CustomerAdvocacyProgram : relates to
RenewalManagement "1" -- "*" CustomerCohort : relates to
RenewalManagement "1" -- "*" CustomerCommunity : relates to
RenewalManagement "1" -- "*" CustomerEducation : relates to
RenewalManagement "1" -- "*" CustomerFeedback : relates to
RenewalManagement "1" -- "*" CustomerGoal : relates to
RenewalManagement "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"], "related_kpis": ["RENEWAL_RATE", "CUSTOMER_RENEWAL_INTENT", "CUSTOMER_DOWNGRADE_RATE", "CUSTOMER_UPGRADE_RATE"], "key_attributes": ["renewal_id", "customer_id", "subscription_id", "csm_id", "renewal_date", "intent_score", "outcome", "upgrade_downgrade_flag", "value_change"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]},
}
