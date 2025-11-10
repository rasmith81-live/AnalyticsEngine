"""
Referral Object Model

Represents customer referrals and word-of-mouth leads.
"""

REFERRAL = {
    "code": "REFERRAL",
    "name": "Referral",
    "description": "Leads generated through customer referrals",
    "table_schema": {"table_name": "referral", "class_name": "Referral", "columns": [{"name": "referrer_customer_id", "type": "Integer", "index": True}, {"name": "referred_contact", "type": "String", "length": 255}, {"name": "referral_date", "type": "DateTime", "index": True}, {"name": "status", "type": "String", "length": 255}, {"name": "converted", "type": "String", "length": 255}, {"name": "incentive_given", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_referral_referrer_customer_id", "columns": ["referrer_customer_id"]}, {"name": "ix_referral_referral_date", "columns": ["referral_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" Referral : generates >
Referral "1" -- "1" Lead : creates >
Referral "1" -- "0..1" Opportunity : becomes >
' Relationships to Related Objects
Referral "1" -- "*" Account : relates to
Referral "1" -- "*" AccountPenetration : relates to
Referral "1" -- "*" AccountPlan : relates to
Referral "1" -- "*" AccountRisk : relates to
Referral "1" -- "*" KeyAccount : relates to
Referral "1" -- "*" KeyAccountManager : relates to
Referral "1" -- "*" LoyaltyProgram : relates to
Referral "1" -- "*" RenewalManagement : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CUSTOMER_RETENTION", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"], "related_kpis": ["REFERRAL_RATE"], "key_attributes": ["referrer_customer_id", "referred_contact", "referral_date", "status", "converted", "incentive_given"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Loyalty Program", "Renewal Management"]},
}
