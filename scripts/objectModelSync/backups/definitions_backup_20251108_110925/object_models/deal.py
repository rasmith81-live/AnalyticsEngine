"""
Deal Object Model

Represents active sales negotiations and proposals.
"""

from analytics_models import ObjectModel

DEAL = ObjectModel(
    name="Deal",
    code="DEAL",
    description="Active sales negotiations with specific terms and pricing",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Deal {
}

class Opportunity {
}

class Sale {
}

class Product {
}

class SalesRepresentative {
}

class Discount {
}

' Relationships
Opportunity "1" -- "0..1" Deal : becomes >
Deal "1" -- "0..1" Sale : results in >
Deal "0..*" -- "1..*" Product : includes >
SalesRepresentative "1" -- "0..*" Deal : handles >
Deal "1" -- "0..1" Discount : has >

@enduml

' Related Objects

class Account {
}

class Appointment {
}

class Assessment {
}

class Benchmark {
}

class Call {
}

class ChannelPartner {
}

class CoachingSession {
}

class Contract {
}

class Customer {
}

class Demo {
}

class Goal {
}

class Lead {
}

class Meeting {
}

class PerformanceScorecard {
}

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
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "DEAL_SIZE",
            "AVERAGE_DEAL_DISCOUNT",
            "LOST_DEAL_ANALYSIS",
            "TIME_TO_CLOSE",
            "WIN_RATE",
            "COMPETITIVE_WIN_RATE"
        ],
        "key_attributes": [
            "deal_value",
            "discount_percentage",
            "proposed_terms",
            "close_date",
            "status",
            "win_probability",
            "competitor",
            "loss_reason"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Demo", "Goal", "Lead", "Meeting", "Opportunity", "Performance Scorecard"]}
)
