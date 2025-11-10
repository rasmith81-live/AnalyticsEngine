"""
Appointment Object Model

Represents appointments booked by SDRs/BDRs with prospects.
"""

from analytics_models import ObjectModel

APPOINTMENT = ObjectModel(
    name="Appointment",
    code="APPOINTMENT",
    description="Appointments booked by sales development representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Appointment {
}

class SalesRepresentative {
}

class Prospect {
}

class Demo {
}

class Opportunity {
}

' Relationships
SalesRepresentative "1" -- "0..*" Appointment : books >
Appointment "0..*" -- "1" Prospect : with >
Appointment "1" -- "0..1" Demo : may lead to >
Appointment "1" -- "0..1" Opportunity : may convert to >

@enduml

' Related Objects

class Call {
}

class Deal {
}

class Lead {
}

class Meeting {
}

class Product {
}

class SalesTeam {
}

class SupportTicket {
}

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
""",
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "related_kpis": [
            "APPOINTMENTS_PER_MONTH",
            "MEETING_BOOKING_RATE"
        ],
        "key_attributes": [
            "appointment_id",
            "sdr_id",
            "prospect_id",
            "scheduled_date",
            "appointment_type",
            "status",
            "show_rate"
        ],
        "related_objects": ["Call", "Deal", "Demo", "Lead", "Meeting", "Opportunity", "Product", "Sale", "Sales Representative", "Sales Team", "Support Ticket"]}
)
