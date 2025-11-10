"""
Competitive Analysis Object Model

Represents competitive analysis and intelligence.
"""

COMPETITIVE_ANALYSIS = {
    "code": "COMPETITIVE_ANALYSIS",
    "name": "Competitive Analysis",
    "description": "Competitive analysis and intelligence for strategic planning",
    "table_schema": {"table_name": "competitive_analysis", "class_name": "Competitive Analysis", "columns": [{"name": "analysis_id", "type": "Integer", "index": True}, {"name": "competitor_id", "type": "Integer", "index": True}, {"name": "strengths", "type": "String", "length": 255}, {"name": "weaknesses", "type": "String", "length": 255}, {"name": "market_position", "type": "String", "length": 255}, {"name": "strategy_response", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_competitive_analysis_analysis_id", "columns": ["analysis_id"]}, {"name": "ix_competitive_analysis_competitor_id", "columns": ["competitor_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
StrategyTeam "1" -- "0..*" CompetitiveAnalysis : conducts >
CompetitiveAnalysis "1" -- "1" Competitor : for >
CompetitiveAnalysis "0..*" -- "1" MarketSegment : in >
CompetitiveAnalysis "0..*" -- "0..*" StrategicInitiative : influences >
' Relationships to Related Objects
CompetitiveAnalysis "1" -- "*" Account : relates to
CompetitiveAnalysis "1" -- "*" AccountPenetration : relates to
CompetitiveAnalysis "1" -- "*" AccountPlan : relates to
CompetitiveAnalysis "1" -- "*" AccountRisk : relates to
CompetitiveAnalysis "1" -- "*" Appointment : relates to
CompetitiveAnalysis "1" -- "*" Assessment : relates to
CompetitiveAnalysis "1" -- "*" Call : relates to
CompetitiveAnalysis "1" -- "*" ChannelConflict : relates to
CompetitiveAnalysis "1" -- "*" ChannelDeal : relates to
CompetitiveAnalysis "1" -- "*" ChannelMarket : relates to
CompetitiveAnalysis "1" -- "*" ChannelPartner : relates to
CompetitiveAnalysis "1" -- "*" Customer : relates to
CompetitiveAnalysis "1" -- "*" CustomerAdvocacyProgram : relates to
CompetitiveAnalysis "1" -- "*" CustomerCohort : relates to
CompetitiveAnalysis "1" -- "*" CustomerCommunity : relates to
CompetitiveAnalysis "1" -- "*" CustomerEducation : relates to
CompetitiveAnalysis "1" -- "*" CustomerFeedback : relates to
CompetitiveAnalysis "1" -- "*" CustomerGoal : relates to
CompetitiveAnalysis "1" -- "*" CustomerHealthRecord : relates to
CompetitiveAnalysis "1" -- "*" CustomerJourney : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"], "related_kpis": ["MARKET_SHARE", "WIN_RATE"], "key_attributes": ["analysis_id", "competitor_id", "strengths", "weaknesses", "market_position", "strategy_response"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey"]},
}
