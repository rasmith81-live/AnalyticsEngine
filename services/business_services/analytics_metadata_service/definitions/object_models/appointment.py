"""
Appointment Object Model

Represents appointments booked by SDRs/BDRs with prospects.
"""

APPOINTMENT = {
    "code": "APPOINTMENT",
    "name": "Appointment",
    "description": "Appointments booked by sales development representatives",
    "table_schema": {"table_name": "appointment", "class_name": "Appointment", "columns": [{"name": "appointment_id", "type": "Integer", "index": True}, {"name": "sdr_id", "type": "Integer", "index": True}, {"name": "prospect_id", "type": "Integer", "index": True}, {"name": "scheduled_date", "type": "DateTime", "index": True}, {"name": "appointment_type", "type": "String", "length": 50, "index": True}, {"name": "status", "type": "String", "length": 255}, {"name": "show_rate", "type": "Float"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_appointment_appointment_id", "columns": ["appointment_id"]}, {"name": "ix_appointment_sdr_id", "columns": ["sdr_id"]}, {"name": "ix_appointment_prospect_id", "columns": ["prospect_id"]}, {"name": "ix_appointment_scheduled_date", "columns": ["scheduled_date"]}, {"name": "ix_appointment_appointment_type", "columns": ["appointment_type"]}]},
    "schema_definition": """
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" Appointment : books >
Appointment "0..*" -- "1" Prospect : with >
Appointment "1" -- "0..1" Demo : may lead to >
Appointment "1" -- "0..1" Opportunity : may convert to >
' Related Objects
' Relationships to Related Objects
Appointment "1" -- "*" Call : relates to
Appointment "1" -- "*" Deal : relates to
Appointment "1" -- "*" Demo : relates to
Appointment "1" -- "*" Lead : relates to
Appointment "1" -- "*" Meeting : relates to
Appointment "1" -- "*" Opportunity : relates to
Appointment "1" -- "*" Product : relates to
Appointment "1" -- "*" Sale : relates to
Appointment "1" -- "*" SalesRepresentative : relates to
Appointment "1" -- "*" SalesTeam : relates to
Appointment "1" -- "*" SupportTicket : relates to
@enduml
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "related_kpis": ["APPOINTMENTS_PER_MONTH", "MEETING_BOOKING_RATE"], "key_attributes": ["appointment_id", "sdr_id", "prospect_id", "scheduled_date", "appointment_type", "status", "show_rate"], "related_objects": ["Call", "Deal", "Demo", "Lead", "Meeting", "Opportunity", "Product", "Sale", "Sales Representative", "Sales Team", "Support Ticket"]},
}
