"""
Deal Object Model

Represents active sales negotiations and proposals.
"""

DEAL = {
    "code": "DEAL",
    "name": "Deal",
    "description": "Active sales negotiations with specific terms and pricing",
    "table_schema": {"table_name": "deal", "class_name": "Deal", "columns": [{"name": "deal_value", "type": "Float"}, {"name": "discount_percentage", "type": "Float"}, {"name": "proposed_terms", "type": "String", "length": 255}, {"name": "close_date", "type": "DateTime", "index": True}, {"name": "status", "type": "String", "length": 255}, {"name": "win_probability", "type": "String", "length": 255}, {"name": "competitor", "type": "String", "length": 255}, {"name": "loss_reason", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_deal_close_date", "columns": ["close_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Opportunity "1" -- "0..1" Deal : becomes >
Deal "1" -- "0..1" Sale : results in >
Deal "0..*" -- "1..*" Product : includes >
SalesRepresentative "1" -- "0..*" Deal : handles >
Deal "1" -- "0..1" Discount : has >
' Related Objects
' Relationships to Related Objects
Deal "1" -- "*" Account : relates to
Deal "1" -- "*" Appointment : relates to
Deal "1" -- "*" Assessment : relates to
Deal "1" -- "*" Benchmark : relates to
Deal "1" -- "*" Call : relates to
Deal "1" -- "*" ChannelPartner : relates to
Deal "1" -- "*" CoachingSession : relates to
Deal "1" -- "*" Contract : relates to
Deal "1" -- "*" Customer : relates to
Deal "1" -- "*" Demo : relates to
Deal "1" -- "*" Goal : relates to
Deal "1" -- "*" Lead : relates to
Deal "1" -- "*" Meeting : relates to
Deal "1" -- "*" Opportunity : relates to
Deal "1" -- "*" PerformanceScorecard : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["DEAL_SIZE", "AVERAGE_DEAL_DISCOUNT", "LOST_DEAL_ANALYSIS", "TIME_TO_CLOSE", "WIN_RATE", "COMPETITIVE_WIN_RATE"], "key_attributes": ["deal_value", "discount_percentage", "proposed_terms", "close_date", "status", "win_probability", "competitor", "loss_reason"], "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Demo", "Goal", "Lead", "Meeting", "Opportunity", "Performance Scorecard"]},
}
