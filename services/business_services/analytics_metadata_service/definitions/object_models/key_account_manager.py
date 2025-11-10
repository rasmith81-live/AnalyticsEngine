"""
Key Account Manager Object Model

Represents key account managers who strategically manage high-value accounts.
"""

KEY_ACCOUNT_MANAGER = {
    "code": "KEY_ACCOUNT_MANAGER",
    "name": "Key Account Manager",
    "description": "Strategic account managers responsible for high-value customer relationships",
    "table_schema": {"table_name": "key_account_manager", "class_name": "Key Account Manager", "columns": [{"name": "kam_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "account_portfolio", "type": "String", "length": 255}, {"name": "portfolio_value", "type": "Float"}, {"name": "performance_index", "type": "String", "length": 255}, {"name": "relationship_strength", "type": "String", "length": 255}, {"name": "accounts_managed", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_key_account_manager_kam_id", "columns": ["kam_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
KeyAccountManager "1" -- "0..*" KeyAccount : manages >
KeyAccountManager "1" -- "0..*" AccountPlan : creates >
KeyAccountManager "0..*" -- "0..*" Stakeholder : engages >
KeyAccountManager "1" -- "0..*" StrategicReview : conducts >
' Relationships to Related Objects
KeyAccountManager "1" -- "*" Account : relates to
KeyAccountManager "1" -- "*" AccountPenetration : relates to
KeyAccountManager "1" -- "*" AccountPlan : relates to
KeyAccountManager "1" -- "*" AccountRisk : relates to
KeyAccountManager "1" -- "*" Call : relates to
KeyAccountManager "1" -- "*" ChannelConflict : relates to
KeyAccountManager "1" -- "*" ChannelDeal : manages
KeyAccountManager "1" -- "*" ChannelMarket : relates to
KeyAccountManager "1" -- "*" ChannelPartner : relates to
KeyAccountManager "1" -- "*" CompetitiveAnalysis : relates to
KeyAccountManager "1" -- "*" Contract : relates to
KeyAccountManager "1" -- "*" Customer : relates to
KeyAccountManager "1" -- "*" CustomerAdvocacyProgram : relates to
KeyAccountManager "1" -- "*" CustomerCohort : relates to
KeyAccountManager "1" -- "*" CustomerCommunity : relates to
KeyAccountManager "1" -- "*" CustomerEducation : relates to
KeyAccountManager "1" -- "*" CustomerFeedback : relates to
KeyAccountManager "1" -- "*" CustomerGoal : relates to
KeyAccountManager "1" -- "*" CustomerHealthRecord : relates to
KeyAccountManager "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"], "related_kpis": ["KEY_ACCOUNT_MANAGER_PERFORMANCE_INDEX", "STRATEGIC_ACCOUNT_CONTACT_FREQUENCY"], "key_attributes": ["kam_id", "name", "account_portfolio", "portfolio_value", "performance_index", "relationship_strength", "accounts_managed"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]},
}
