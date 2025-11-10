"""
Partnership Object Model

Represents strategic business partnerships and alliances.
"""

PARTNERSHIP = {
    "code": "PARTNERSHIP",
    "name": "Partnership",
    "description": "Strategic partnerships and business alliances",
    "table_schema": {"table_name": "partnership", "class_name": "Partnership", "columns": [{"name": "partner_name", "type": "String", "length": 255}, {"name": "partnership_type", "type": "String", "length": 50, "index": True}, {"name": "start_date", "type": "DateTime", "index": True}, {"name": "status", "type": "String", "length": 255}, {"name": "revenue_contribution", "type": "String", "length": 255}, {"name": "opportunities_generated", "type": "String", "length": 255}, {"name": "effectiveness_score", "type": "Float"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_partnership_partnership_type", "columns": ["partnership_type"]}, {"name": "ix_partnership_start_date", "columns": ["start_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Partnership "0..*" -- "1" Account : with >
Partnership "1" -- "0..*" Opportunity : generates >
Partnership "1" -- "0..*" Revenue : produces >
' Relationships to Related Objects
Partnership "1" -- "*" Account : relates to
Partnership "1" -- "*" AccountPenetration : relates to
Partnership "1" -- "*" AccountPlan : relates to
Partnership "1" -- "*" AccountRisk : relates to
Partnership "1" -- "*" Assessment : relates to
Partnership "1" -- "*" ChannelConflict : relates to
Partnership "1" -- "*" ChannelDeal : relates to
Partnership "1" -- "*" ChannelMarket : relates to
Partnership "1" -- "*" ChannelPartner : relates to
Partnership "1" -- "*" EnablementFeedback : relates to
Partnership "1" -- "*" KeyAccount : relates to
Partnership "1" -- "*" KeyAccountManager : relates to
Partnership "1" -- "*" PartnerAgreement : relates to
Partnership "1" -- "*" PartnerIncentive : relates to
Partnership "1" -- "*" PartnerPerformanceScorecard : relates to
Partnership "1" -- "*" PartnerPortal : relates to
Partnership "1" -- "*" PartnerTraining : relates to
Partnership "1" -- "*" RevenueForecast : relates to
Partnership "1" -- "*" StrategicInitiative : relates to
Partnership "1" -- "*" StrategicReview : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES"], "related_kpis": ["STRATEGIC_PARTNER_DEVELOPMENT_INDEX"], "key_attributes": ["partner_name", "partnership_type", "start_date", "status", "revenue_contribution", "opportunities_generated", "effectiveness_score"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Enablement Feedback", "Key Account", "Key Account Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Strategic Initiative", "Strategic Review"]},
}
