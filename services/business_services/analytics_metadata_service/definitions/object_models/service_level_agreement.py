"""
Service Level Agreement Object Model

Represents SLAs with customers and performance tracking.
"""

SERVICE_LEVEL_AGREEMENT = {
    "code": "SERVICE_LEVEL_AGREEMENT",
    "name": "Service Level Agreement",
    "description": "Service level agreements with performance tracking",
    "table_schema": {"table_name": "service_level_agreement", "class_name": "Service Level Agreement", "columns": [{"name": "sla_id", "type": "Integer", "index": True}, {"name": "customer_id", "type": "Integer", "index": True}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "end_date", "type": "DateTime", "index": True}, {"name": "metrics", "type": "String", "length": 255}, {"name": "targets", "type": "String", "length": 255}, {"name": "actual_performance", "type": "String", "length": 255}, {"name": "compliance_status", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_service_level_agreement_sla_id", "columns": ["sla_id"]}, {"name": "ix_service_level_agreement_customer_id", "columns": ["customer_id"]}, {"name": "ix_service_level_agreement_start_date", "columns": ["start_date"]}, {"name": "ix_service_level_agreement_end_date", "columns": ["end_date"]}, {"name": "ix_service_level_agreement_compliance_status", "columns": ["compliance_status"]}]},
    "schema_definition": """
    @startuml
' Relationships
Customer "1" -- "0..*" ServiceLevelAgreement : has >
ServiceLevelAgreement "1" -- "1..*" SLAMetric : defines >
ServiceLevelAgreement "1" -- "0..*" SLAPerformance : tracked by >
' Relationships to Related Objects
ServiceLevelAgreement "1" -- "*" Account : relates to
ServiceLevelAgreement "1" -- "*" AccountPenetration : relates to
ServiceLevelAgreement "1" -- "*" AccountPlan : relates to
ServiceLevelAgreement "1" -- "*" AccountRisk : relates to
ServiceLevelAgreement "1" -- "*" Appointment : relates to
ServiceLevelAgreement "1" -- "*" ChannelConflict : relates to
ServiceLevelAgreement "1" -- "*" ChannelDeal : relates to
ServiceLevelAgreement "1" -- "*" ChannelMarket : relates to
ServiceLevelAgreement "1" -- "*" ChannelPartner : relates to
ServiceLevelAgreement "1" -- "*" ChurnEvent : relates to
ServiceLevelAgreement "1" -- "*" Contract : relates to
ServiceLevelAgreement "1" -- "*" Customer : relates to
ServiceLevelAgreement "1" -- "*" CustomerAdvocacyProgram : relates to
ServiceLevelAgreement "1" -- "*" CustomerCohort : relates to
ServiceLevelAgreement "1" -- "*" CustomerCommunity : relates to
ServiceLevelAgreement "1" -- "*" CustomerEducation : relates to
ServiceLevelAgreement "1" -- "*" CustomerFeedback : relates to
ServiceLevelAgreement "1" -- "*" CustomerGoal : relates to
ServiceLevelAgreement "1" -- "*" CustomerHealthRecord : relates to
ServiceLevelAgreement "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["SERVICE_LEVEL_AGREEMENT_SLA_PERFORMANCE"], "key_attributes": ["sla_id", "customer_id", "start_date", "end_date", "metrics", "targets", "actual_performance", "compliance_status"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]},
}
