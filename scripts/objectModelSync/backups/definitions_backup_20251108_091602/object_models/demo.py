"""
Demo Object Model

Represents product demonstrations and presentations.
"""

from analytics_models import ObjectModel

DEMO = ObjectModel(
    name="Demo",
    code="DEMO",
    description="Product or service demonstrations given to prospects",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Demo {
}

class Opportunity {
}

class SalesRepresentative {
}

class Product {
}

class Meeting {
}

' Relationships
Opportunity "1" -- "0..*" Demo : includes >
SalesRepresentative "1" -- "0..*" Demo : conducts >
Demo "0..*" -- "1..*" Product : showcases >
Demo "1" -- "1" Meeting : part of >

@enduml

' Related Objects

class Appointment {
}

class Deal {
}

class Proposal {
}

class SalesTeam {
}

class TrainingProgram {
}

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
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "DEMO_TO_CLOSING_RATE",
            "SALES_MEETING_CONVERSION_RATIO"
        ],
        "key_attributes": [
            "demo_date",
            "duration",
            "attendees",
            "products_shown",
            "outcome",
            "follow_up_scheduled",
            "converted_to_sale"
        ],
        "related_objects": ["Appointment", "Deal", "Opportunity", "Product", "Proposal", "Sale", "Sales Representative", "Sales Team", "Training Program"]}
)
