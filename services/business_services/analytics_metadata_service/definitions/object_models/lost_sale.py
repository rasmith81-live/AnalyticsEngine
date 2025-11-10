"""
Lost Sale Object Model

Represents lost sales opportunities and analysis.
"""

LOST_SALE = {
    "code": "LOST_SALE",
    "name": "Lost Sale",
    "description": "Lost sales opportunities and competitive analysis",
    "table_schema": {"table_name": "lost_sale", "class_name": "Lost Sale", "columns": [{"name": "lost_sale_id", "type": "Integer", "index": True}, {"name": "opportunity_id", "type": "Integer", "index": True}, {"name": "loss_date", "type": "DateTime", "index": True}, {"name": "reason", "type": "String", "length": 255}, {"name": "competitor", "type": "String", "length": 255}, {"name": "value_lost", "type": "String", "length": 255}, {"name": "stage_lost", "type": "String", "length": 255}, {"name": "lessons_learned", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_lost_sale_lost_sale_id", "columns": ["lost_sale_id"]}, {"name": "ix_lost_sale_opportunity_id", "columns": ["opportunity_id"]}, {"name": "ix_lost_sale_loss_date", "columns": ["loss_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Opportunity "1" -- "0..1" LostSale : may result in >
LostSale "0..*" -- "0..1" Competitor : lost to >
LostSale "1" -- "1..*" LossReason : has >
' Relationships to Related Objects
LostSale "1" -- "*" Account : relates to
LostSale "1" -- "*" AccountPenetration : relates to
LostSale "1" -- "*" AccountPlan : relates to
LostSale "1" -- "*" AccountRisk : relates to
LostSale "1" -- "*" Appointment : relates to
LostSale "1" -- "*" Assessment : relates to
LostSale "1" -- "*" Call : relates to
LostSale "1" -- "*" ChannelConflict : relates to
LostSale "1" -- "*" ChannelDeal : relates to
LostSale "1" -- "*" ChannelMarket : relates to
LostSale "1" -- "*" ChannelPartner : relates to
LostSale "1" -- "*" ChurnEvent : relates to
LostSale "1" -- "*" CompetitiveAnalysis : relates to
LostSale "1" -- "*" Customer : relates to
LostSale "1" -- "*" CustomerAdvocacyProgram : relates to
LostSale "1" -- "*" CustomerCohort : relates to
LostSale "1" -- "*" CustomerCommunity : relates to
LostSale "1" -- "*" CustomerEducation : relates to
LostSale "1" -- "*" CustomerFeedback : relates to
LostSale "1" -- "*" CustomerGoal : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["LOST_SALE_ANALYSIS"], "key_attributes": ["lost_sale_id", "opportunity_id", "loss_date", "reason", "competitor", "value_lost", "stage_lost", "lessons_learned"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]},
}
