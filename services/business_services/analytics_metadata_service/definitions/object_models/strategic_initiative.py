"""
Strategic Initiative Object Model

Represents strategic initiatives for sales growth.
"""

STRATEGIC_INITIATIVE = {
    "code": "STRATEGIC_INITIATIVE",
    "name": "Strategic Initiative",
    "description": "Strategic initiatives for driving sales growth and market position",
    "table_schema": {"table_name": "strategic_initiative", "class_name": "Strategic Initiative", "columns": [{"name": "initiative_id", "type": "Integer", "index": True}, {"name": "name", "type": "String", "length": 255}, {"name": "objectives", "type": "String", "length": 255}, {"name": "timeline", "type": "String", "length": 255}, {"name": "budget", "type": "String", "length": 255}, {"name": "success_metrics", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_strategic_initiative_initiative_id", "columns": ["initiative_id"]}]},
    "schema_definition": """
    @startuml
' Relationships
StrategyTeam "1" -- "0..*" StrategicInitiative : defines >
StrategicInitiative "0..*" -- "0..*" MarketSegment : targets >
SalesTeam "0..*" -- "0..*" StrategicInitiative : executes >
StrategicInitiative "1" -- "1..*" KPI : measured by >
' Relationships to Related Objects
StrategicInitiative "1" -- "*" Account : relates to
StrategicInitiative "1" -- "*" AccountPenetration : relates to
StrategicInitiative "1" -- "*" AccountPlan : relates to
StrategicInitiative "1" -- "*" AccountRisk : relates to
StrategicInitiative "1" -- "*" Assessment : relates to
StrategicInitiative "1" -- "*" ChannelConflict : relates to
StrategicInitiative "1" -- "*" ChannelDeal : relates to
StrategicInitiative "1" -- "*" ChannelMarket : relates to
StrategicInitiative "1" -- "*" ChannelPartner : relates to
StrategicInitiative "1" -- "*" CompetitiveAnalysis : relates to
StrategicInitiative "1" -- "*" EnablementFeedback : relates to
StrategicInitiative "1" -- "*" EnablementPlatform : relates to
StrategicInitiative "1" -- "*" Goal : relates to
StrategicInitiative "1" -- "*" KeyAccount : relates to
StrategicInitiative "1" -- "*" KeyAccountManager : relates to
StrategicInitiative "1" -- "*" PartnerAgreement : relates to
StrategicInitiative "1" -- "*" PartnerIncentive : relates to
StrategicInitiative "1" -- "*" PartnerPerformanceScorecard : relates to
StrategicInitiative "1" -- "*" PartnerPortal : relates to
StrategicInitiative "1" -- "*" PartnerTraining : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_ENABLEMENT"], "related_kpis": ["SALES_GROWTH", "MARKET_SHARE"], "key_attributes": ["initiative_id", "name", "objectives", "timeline", "budget", "success_metrics", "status"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Enablement Feedback", "Enablement Platform", "Goal", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training"]},
}
