"""
Customer Advocacy Program Object Model

Represents customer advocacy programs and activities.
"""

CUSTOMER_ADVOCACY_PROGRAM = {
    "code": "CUSTOMER_ADVOCACY_PROGRAM",
    "name": "Customer Advocacy Program",
    "description": "Customer advocacy programs and activities",
    "table_schema": {"table_name": "customer_advocacy_program", "class_name": "Customer Advocacy Program", "columns": [{"name": "program_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "participant_count", "type": "Integer"}, {"name": "advocacy_actions_count", "type": "Integer"}, {"name": "testimonials_count", "type": "Integer"}, {"name": "case_studies_count", "type": "Integer"}, {"name": "referrals_generated", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_customer_advocacy_program_program_id", "columns": ["program_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
CustomerAdvocacyProgram "0..*" -- "0..*" Customer : has advocates >
CustomerAdvocacyProgram "1" -- "0..*" AdvocacyAction : tracks >
AdvocacyAction "1" -- "0..1" Testimonial : may produce >
AdvocacyAction "1" -- "0..1" CaseStudy : may produce >
' Relationships to Related Objects
CustomerAdvocacyProgram "1" -- "*" Account : relates to
CustomerAdvocacyProgram "1" -- "*" AccountPenetration : relates to
CustomerAdvocacyProgram "1" -- "*" AccountPlan : relates to
CustomerAdvocacyProgram "1" -- "*" AccountRisk : relates to
CustomerAdvocacyProgram "1" -- "*" Call : relates to
CustomerAdvocacyProgram "1" -- "*" Certification : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelConflict : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelDeal : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelMarket : relates to
CustomerAdvocacyProgram "1" -- "*" ChannelPartner : relates to
CustomerAdvocacyProgram "1" -- "*" ChurnEvent : relates to
CustomerAdvocacyProgram "1" -- "*" CompetitiveAnalysis : relates to
CustomerAdvocacyProgram "1" -- "*" Contract : relates to
CustomerAdvocacyProgram "1" -- "*" Customer : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerCohort : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerCommunity : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerEducation : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerFeedback : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerGoal : relates to
CustomerAdvocacyProgram "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["ADVOCACY_ACTIONS", "CUSTOMER_REFERENCEABILITY_RATE"], "key_attributes": ["program_id", "name", "participant_count", "advocacy_actions_count", "testimonials_count", "case_studies_count", "referrals_generated"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]},
}
