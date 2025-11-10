"""
Sale Object Model

Represents completed transactions with customers.
"""

from analytics_models import ObjectModel

SALE = ObjectModel(
    name="Sale",
    code="SALE",
    description="Completed transaction where a deal has been won and closed",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Sale {
}

class Deal {
}

class Customer {
}

class Product {
}

class Revenue {
}

class FollowUp {
}

' Relationships
Deal "1" -- "0..1" Sale : results in >
Sale "1" -- "1" Customer : creates >
Sale "0..*" -- "1..*" Product : contains >
Sale "1" -- "1" Revenue : generates >
Sale "1" -- "0..*" FollowUp : requires >

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

class Certification {
}

class ChannelPartner {
}

class CoachingSession {
}

class Contract {
}

class Demo {
}

class Email {
}

class Goal {
}

class Lead {
}

' Relationships to Related Objects
Sale "1" -- "*" Account : relates to
Sale "1" -- "*" Appointment : relates to
Sale "1" -- "*" Assessment : relates to
Sale "1" -- "*" Benchmark : relates to
Sale "1" -- "*" Call : relates to
Sale "1" -- "*" Certification : relates to
Sale "1" -- "*" ChannelPartner : relates to
Sale "1" -- "*" CoachingSession : relates to
Sale "1" -- "*" Contract : relates to
Sale "1" -- "*" Customer : relates to
Sale "1" -- "*" Deal : relates to
Sale "1" -- "*" Demo : relates to
Sale "1" -- "*" Email : relates to
Sale "1" -- "*" Goal : relates to
Sale "1" -- "*" Lead : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "PROFIT_MARGIN_PER_SALE",
            "POST_SALE_FOLLOW_UP_RATE",
            "RETURN_ON_SALES_INVESTMENT_ROSI",
            "SALES_GROWTH",
            "AVERAGE_REVENUE_PER_UNIT_ARPU"
        ],
        "key_attributes": [
            "sale_amount",
            "sale_date",
            "cost",
            "profit_margin",
            "payment_terms",
            "follow_up_completed",
            "customer_id",
            "sales_rep_id"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Certification", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Email", "Goal", "Lead"]}
)
