"""
Opportunity Object Model

Represents qualified sales prospects in the pipeline.
"""

OPPORTUNITY = {
    "code": "OPPORTUNITY",
    "name": "Opportunity",
    "description": "Qualified sales prospects that have been vetted and are actively being pursued",
    "table_schema": {"table_name": "opportunity", "class_name": "Opportunity", "columns": [{"name": "opportunity_name", "type": "String", "length": 255}, {"name": "stage", "type": "String", "length": 255}, {"name": "probability", "type": "String", "length": 255}, {"name": "expected_value", "type": "Float"}, {"name": "expected_close_date", "type": "DateTime", "index": True}, {"name": "account_id", "type": "Integer", "index": True}, {"name": "owner_id", "type": "Integer", "index": True}, {"name": "created_date", "type": "DateTime", "index": True}, {"name": "last_activity_date", "type": "DateTime", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_opportunity_expected_close_date", "columns": ["expected_close_date"]}, {"name": "ix_opportunity_account_id", "columns": ["account_id"]}, {"name": "ix_opportunity_owner_id", "columns": ["owner_id"]}, {"name": "ix_opportunity_created_date", "columns": ["created_date"]}, {"name": "ix_opportunity_last_activity_date", "columns": ["last_activity_date"]}]},
    "schema_definition": """
    @startuml
' Sales Development Specific
' Relationships - Core
Lead "1" -- "0..1" Opportunity : converts to >
Opportunity "1" -- "0..1" Deal : becomes >
Account "1" -- "0..*" Opportunity : has >
SalesRepresentative "1" -- "0..*" Opportunity : owns >
Pipeline "1" -- "0..*" Opportunity : contains >
' Relationships - Sales Development
LeadQualification "1" -- "0..1" Opportunity : creates (if SQL) >
Appointment "1" -- "0..1" Opportunity : may convert to >
Prospect "0..1" -- "0..1" Opportunity : converts to >
' Related Objects
' Relationships to Related Objects
Opportunity "1" -- "*" Account : relates to
Opportunity "1" -- "*" Appointment : relates to
Opportunity "1" -- "*" Assessment : relates to
Opportunity "1" -- "*" Benchmark : relates to
Opportunity "1" -- "*" Call : relates to
Opportunity "1" -- "*" ChannelPartner : relates to
Opportunity "1" -- "*" CoachingSession : relates to
Opportunity "1" -- "*" Contract : relates to
Opportunity "1" -- "*" Customer : relates to
Opportunity "1" -- "*" Deal : manages
Opportunity "1" -- "*" Demo : relates to
Opportunity "1" -- "*" Goal : relates to
Opportunity "1" -- "*" Lead : relates to
Opportunity "1" -- "*" Meeting : relates to
Opportunity "1" -- "*" PerformanceScorecard : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT"], "related_kpis": ["COST_PER_OPPORTUNITY", "OPPORTUNITY_PIPELINE", "OPPORTUNITY_TO_CLOSE_RATE", "LEAD_TO_OPPORTUNITY_CONVERSION_RATE", "NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED", "PIPELINE_GROWTH_RATE"], "key_attributes": ["opportunity_name", "stage", "probability", "expected_value", "expected_close_date", "account_id", "owner_id", "created_date", "last_activity_date"], "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Goal", "Lead", "Meeting", "Performance Scorecard"]},
}
