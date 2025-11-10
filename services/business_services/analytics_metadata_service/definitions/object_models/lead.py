"""
Lead Object Model

Represents potential customers showing interest in products/services.
"""

LEAD = {
    "code": "LEAD",
    "name": "Lead",
    "description": "Potential customers who have shown interest in the company's offerings",
    "table_schema": {"table_name": "lead", "class_name": "Lead", "columns": [{"name": "lead_source", "type": "String", "length": 255}, {"name": "contact_name", "type": "String", "length": 255}, {"name": "contact_email", "type": "String", "length": 255, "unique": True}, {"name": "contact_phone", "type": "String", "length": 255}, {"name": "company", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "score", "type": "String", "length": 255}, {"name": "assigned_to", "type": "String", "length": 255}, {"name": "created_date", "type": "DateTime", "index": True}, {"name": "last_contact_date", "type": "DateTime", "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_lead_contact_email", "columns": ["contact_email"], "unique": True}, {"name": "ix_lead_created_date", "columns": ["created_date"]}, {"name": "ix_lead_last_contact_date", "columns": ["last_contact_date"]}]},
    "schema_definition": """
    @startuml
' Sales Development Specific
' Relationships - Core
Account "1" -- "0..*" Lead : generates >
Lead "1" -- "0..1" Opportunity : converts to >
SalesRepresentative "1" -- "0..*" Lead : manages >
Lead "1" -- "0..1" LeadScore : has >
' Relationships - Sales Development
OutboundCall "0..*" -- "0..1" Lead : to >
Lead "1" -- "0..1" LeadQualification : undergoes >
Lead "0..1" -- "0..1" Prospect : becomes >
' Related Objects
' Relationships to Related Objects
Lead "1" -- "*" Account : relates to
Lead "1" -- "*" Appointment : relates to
Lead "1" -- "*" Assessment : relates to
Lead "1" -- "*" Benchmark : relates to
Lead "1" -- "*" Call : relates to
Lead "1" -- "*" ChannelPartner : relates to
Lead "1" -- "*" CoachingSession : relates to
Lead "1" -- "*" Contract : relates to
Lead "1" -- "*" Customer : relates to
Lead "1" -- "*" Deal : relates to
Lead "1" -- "*" Goal : relates to
Lead "1" -- "*" Meeting : relates to
Lead "1" -- "*" Opportunity : manages
Lead "1" -- "*" PerformanceScorecard : relates to
Lead "1" -- "*" Product : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT"], "related_kpis": ["COST_PER_LEAD", "LEAD_RESPONSE_TIME", "LEAD_QUALITY_SCORE", "LEAD_NURTURING_SUCCESS_RATE", "LEAD_TO_OPPORTUNITY_CONVERSION_RATE", "MARKETING_QUALIFIED_LEADS_MQL", "SALES_QUALIFIED_LEADS_SQL", "QUALIFIED_LEADS_PER_MONTH", "AVERAGE_LEAD_SCORE"], "key_attributes": ["lead_source", "contact_name", "contact_email", "contact_phone", "company", "status", "score", "assigned_to", "created_date", "last_contact_date"], "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Goal", "Meeting", "Opportunity", "Performance Scorecard", "Product"]},
}
