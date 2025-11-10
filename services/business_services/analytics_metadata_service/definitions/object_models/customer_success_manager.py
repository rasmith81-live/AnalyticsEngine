"""
Customer Success Manager Object Model

Represents CSMs who proactively manage customer accounts and drive value realization.
"""

CUSTOMER_SUCCESS_MANAGER = {
    "code": "CUSTOMER_SUCCESS_MANAGER",
    "name": "Customer Success Manager",
    "description": "Customer Success Managers who proactively manage customer portfolios",
    "table_schema": {"table_name": "customer_success_manager", "class_name": "Customer Success Manager", "columns": [{"name": "csm_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "customer_portfolio", "type": "String", "length": 255}, {"name": "portfolio_size", "type": "String", "length": 255}, {"name": "utilization_rate", "type": "Float"}, {"name": "engagement_score", "type": "Float"}, {"name": "attrition_risk", "type": "String", "length": 255}, {"name": "performance_metrics", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_customer_success_manager_csm_id", "columns": ["csm_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
CustomerSuccessManager "1" -- "0..*" Customer : manages >
CustomerSuccessManager "1" -- "0..*" QuarterlyBusinessReview : conducts >
CustomerSuccessManager "1" -- "0..*" CustomerHealthRecord : monitors >
CustomerSuccessManager "1" -- "0..*" CustomerOnboarding : leads >
CustomerSuccessManager "1" -- "0..*" RenewalManagement : oversees >
CustomerSuccessManager "1" -- "0..*" ExpansionOpportunity : identifies >
' Relationships to Related Objects
CustomerSuccessManager "1" -- "*" Account : relates to
CustomerSuccessManager "1" -- "*" AccountPenetration : relates to
CustomerSuccessManager "1" -- "*" AccountPlan : relates to
CustomerSuccessManager "1" -- "*" AccountRisk : relates to
CustomerSuccessManager "1" -- "*" Call : relates to
CustomerSuccessManager "1" -- "*" ChannelConflict : relates to
CustomerSuccessManager "1" -- "*" ChannelDeal : relates to
CustomerSuccessManager "1" -- "*" ChannelMarket : relates to
CustomerSuccessManager "1" -- "*" ChannelPartner : relates to
CustomerSuccessManager "1" -- "*" ChurnEvent : relates to
CustomerSuccessManager "1" -- "*" CompetitiveAnalysis : relates to
CustomerSuccessManager "1" -- "*" Contract : relates to
CustomerSuccessManager "1" -- "*" Customer : relates to
CustomerSuccessManager "1" -- "*" CustomerAdvocacyProgram : relates to
CustomerSuccessManager "1" -- "*" CustomerCohort : relates to
CustomerSuccessManager "1" -- "*" CustomerCommunity : relates to
CustomerSuccessManager "1" -- "*" CustomerEducation : relates to
CustomerSuccessManager "1" -- "*" CustomerFeedback : relates to
CustomerSuccessManager "1" -- "*" CustomerGoal : relates to
CustomerSuccessManager "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["CUSTOMER_SUCCESS_MANAGER_CSM_RATIO", "CUSTOMER_SUCCESS_TEAM_ATTRITION_RATE", "CUSTOMER_SUCCESS_TEAM_ENGAGEMENT", "CUSTOMER_SUCCESS_TEAM_UTILIZATION_RATE"], "key_attributes": ["csm_id", "name", "customer_portfolio", "portfolio_size", "utilization_rate", "engagement_score", "attrition_risk", "performance_metrics"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]},
}
