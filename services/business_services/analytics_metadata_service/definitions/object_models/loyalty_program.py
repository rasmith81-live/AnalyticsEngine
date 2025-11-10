"""
Loyalty Program Object Model

Represents customer loyalty and rewards programs.
"""

LOYALTY_PROGRAM = {
    "code": "LOYALTY_PROGRAM",
    "name": "Loyalty Program",
    "description": "Customer loyalty and rewards programs",
    "table_schema": {"table_name": "loyalty_program", "class_name": "Loyalty Program", "columns": [{"name": "program_id", "type": "Integer", "index": True}, {"name": "program_name", "type": "String", "length": 255}, {"name": "program_type", "type": "String", "length": 50, "index": True}, {"name": "benefits", "type": "String", "length": 255}, {"name": "participation_rate", "type": "Float"}, {"name": "effectiveness_score", "type": "Float"}, {"name": "member_count", "type": "Integer"}, {"name": "engagement_rate", "type": "Float"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_loyalty_program_program_id", "columns": ["program_id"]}, {"name": "ix_loyalty_program_program_type", "columns": ["program_type"]}]},
    "schema_definition": """
    @startuml
' Relationships
LoyaltyProgram "0..*" -- "0..*" Customer : has members >
LoyaltyProgram "1" -- "0..*" Reward : offers >
Customer "1" -- "0..1" LoyaltyMembership : has >
LoyaltyMembership "0..*" -- "1" LoyaltyProgram : in >
' Relationships to Related Objects
LoyaltyProgram "1" -- "*" Account : relates to
LoyaltyProgram "1" -- "*" AccountPenetration : relates to
LoyaltyProgram "1" -- "*" AccountPlan : relates to
LoyaltyProgram "1" -- "*" AccountRisk : relates to
LoyaltyProgram "1" -- "*" Certification : relates to
LoyaltyProgram "1" -- "*" ChannelConflict : relates to
LoyaltyProgram "1" -- "*" ChannelDeal : relates to
LoyaltyProgram "1" -- "*" ChannelMarket : relates to
LoyaltyProgram "1" -- "*" ChannelPartner : relates to
LoyaltyProgram "1" -- "*" CompetitiveAnalysis : relates to
LoyaltyProgram "1" -- "*" Customer : relates to
LoyaltyProgram "1" -- "*" CustomerAdvocacyProgram : relates to
LoyaltyProgram "1" -- "*" CustomerCohort : relates to
LoyaltyProgram "1" -- "*" CustomerCommunity : relates to
LoyaltyProgram "1" -- "*" CustomerEducation : relates to
LoyaltyProgram "1" -- "*" CustomerFeedback : relates to
LoyaltyProgram "1" -- "*" CustomerGoal : relates to
LoyaltyProgram "1" -- "*" CustomerHealthRecord : relates to
LoyaltyProgram "1" -- "*" CustomerJourney : relates to
LoyaltyProgram "1" -- "*" CustomerOnboarding : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["LOYALTY_PROGRAM_EFFECTIVENESS", "LOYALTY_PROGRAM_PARTICIPATION_RATE"], "key_attributes": ["program_id", "program_name", "program_type", "benefits", "participation_rate", "effectiveness_score", "member_count", "engagement_rate"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]},
}
