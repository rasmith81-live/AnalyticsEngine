"""
Demo Object Model

Represents product demonstrations and presentations.
"""

DEMO = {
    "code": "DEMO",
    "name": "Demo",
    "description": "Product or service demonstrations given to prospects",
    "table_schema": {"table_name": "demo", "class_name": "Demo", "columns": [{"name": "demo_date", "type": "DateTime", "index": True}, {"name": "duration", "type": "String", "length": 255}, {"name": "attendees", "type": "String", "length": 255}, {"name": "products_shown", "type": "String", "length": 255}, {"name": "outcome", "type": "String", "length": 255}, {"name": "follow_up_scheduled", "type": "String", "length": 255}, {"name": "converted_to_sale", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_demo_demo_date", "columns": ["demo_date"]}]},
    "schema_definition": """
    @startuml
' Relationships
Opportunity "1" -- "0..*" Demo : includes >
SalesRepresentative "1" -- "0..*" Demo : conducts >
Demo "0..*" -- "1..*" Product : showcases >
Demo "1" -- "1" Meeting : part of >
' Related Objects
' Relationships to Related Objects
Demo "1" -- "*" Appointment : relates to
Demo "1" -- "*" Deal : relates to
Demo "1" -- "*" Opportunity : relates to
Demo "1" -- "*" Product : relates to
Demo "1" -- "*" Proposal : relates to
Demo "1" -- "*" Sale : relates to
Demo "1" -- "*" SalesRepresentative : relates to
Demo "1" -- "*" SalesTeam : relates to
Demo "1" -- "*" TrainingProgram : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["DEMO_TO_CLOSING_RATE", "SALES_MEETING_CONVERSION_RATIO"], "key_attributes": ["demo_date", "duration", "attendees", "products_shown", "outcome", "follow_up_scheduled", "converted_to_sale"], "related_objects": ["Appointment", "Deal", "Opportunity", "Product", "Proposal", "Sale", "Sales Representative", "Sales Team", "Training Program"]},
}
