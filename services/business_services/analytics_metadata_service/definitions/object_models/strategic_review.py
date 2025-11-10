"""
Strategic Review Object Model

Represents strategic business reviews with key accounts.
"""

STRATEGIC_REVIEW = {
    "code": "STRATEGIC_REVIEW",
    "name": "Strategic Review",
    "description": "Strategic business reviews with key accounts",
    "table_schema": {"table_name": "strategic_review", "class_name": "Strategic Review", "columns": [{"name": "review_id", "type": "Integer", "index": True}, {"name": "account_id", "type": "Integer", "index": True}, {"name": "kam_id", "type": "Integer", "index": True}, {"name": "date", "type": "String", "length": 255}, {"name": "attendees", "type": "String", "length": 255}, {"name": "topics_covered", "type": "String", "length": 255}, {"name": "action_items", "type": "String", "length": 255}, {"name": "outcomes", "type": "String", "length": 255}, {"name": "next_review_date", "type": "DateTime", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_strategic_review_review_id", "columns": ["review_id"]}, {"name": "ix_strategic_review_account_id", "columns": ["account_id"]}, {"name": "ix_strategic_review_kam_id", "columns": ["kam_id"]}, {"name": "ix_strategic_review_next_review_date", "columns": ["next_review_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
KeyAccount "1" -- "0..*" StrategicReview : reviewed in >
KeyAccountManager "1" -- "0..*" StrategicReview : conducts >
StrategicReview "0..*" -- "1..*" Stakeholder : includes >
StrategicReview "0..*" -- "1" AccountPlan : reviews >
StrategicReview "1" -- "0..*" ActionItem : produces >
' Relationships to Related Objects
StrategicReview "1" -- "*" Account : relates to
StrategicReview "1" -- "*" AccountPenetration : relates to
StrategicReview "1" -- "*" AccountPlan : relates to
StrategicReview "1" -- "*" AccountRisk : relates to
StrategicReview "1" -- "*" Assessment : relates to
StrategicReview "1" -- "*" Call : relates to
StrategicReview "1" -- "*" ChannelConflict : relates to
StrategicReview "1" -- "*" ChannelDeal : relates to
StrategicReview "1" -- "*" ChannelMarket : relates to
StrategicReview "1" -- "*" ChannelPartner : relates to
StrategicReview "1" -- "*" CompetitiveAnalysis : relates to
StrategicReview "1" -- "*" EnablementFeedback : relates to
StrategicReview "1" -- "*" EnablementPlatform : relates to
StrategicReview "1" -- "*" Goal : relates to
StrategicReview "1" -- "*" KeyAccount : relates to
StrategicReview "1" -- "*" KeyAccountManager : relates to
StrategicReview "1" -- "*" LostSale : relates to
StrategicReview "1" -- "*" PartnerAgreement : relates to
StrategicReview "1" -- "*" PartnerIncentive : relates to
StrategicReview "1" -- "*" PartnerPerformanceScorecard : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_ENABLEMENT"], "related_kpis": ["STRATEGIC_ACCOUNT_CONTACT_FREQUENCY"], "key_attributes": ["review_id", "account_id", "kam_id", "date", "attendees", "topics_covered", "action_items", "outcomes", "next_review_date"], "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Enablement Feedback", "Enablement Platform", "Goal", "Key Account", "Key Account Manager", "Lost Sale", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard"]},
}
