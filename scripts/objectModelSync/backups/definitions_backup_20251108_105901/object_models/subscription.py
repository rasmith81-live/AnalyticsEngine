"""
Subscription Object Model

Represents customer subscriptions or contracts for products/services.
"""

from analytics_models import ObjectModel

SUBSCRIPTION = ObjectModel(
    name="Subscription",
    code="SUBSCRIPTION",
    description="Customer subscriptions or contracts for recurring services",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Subscription {
}

class Customer {
}

class Product {
}

class Renewal {
}

class Revenue {
}

' Relationships
Customer "1" -- "0..*" Subscription : has >
Subscription "0..*" -- "1..*" Product : includes >
Subscription "1" -- "0..*" Renewal : has >
Subscription "1" -- "0..*" Revenue : generates >

@enduml

' Related Objects

class Account {
}

class ChannelPartner {
}

class Deal {
}

class Lead {
}

class Opportunity {
}

class Sale {
}

' Relationships to Related Objects
Subscription "1" -- "*" Account : relates to
Subscription "1" -- "*" ChannelPartner : relates to
Subscription "1" -- "*" Customer : relates to
Subscription "1" -- "*" Deal : relates to
Subscription "1" -- "*" Lead : relates to
Subscription "1" -- "*" Opportunity : relates to
Subscription "1" -- "*" Product : relates to
Subscription "1" -- "*" Sale : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "related_kpis": [
            "CONTRACT_UTILIZATION_RATE",
            "RENEWAL_RATE",
            "RENEWAL_UPSELL_RATE",
            "REVENUE_RETENTION_RATE",
            "NET_REVENUE_RETENTION_NRR"
        ],
        "key_attributes": [
            "subscription_id",
            "customer_id",
            "start_date",
            "end_date",
            "renewal_date",
            "contract_value",
            "utilization_rate",
            "status",
            "renewal_status"
        ],
        "related_objects": ["Account", "Channel Partner", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale"]}
)
