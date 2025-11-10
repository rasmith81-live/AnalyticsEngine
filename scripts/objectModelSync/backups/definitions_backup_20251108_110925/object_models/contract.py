"""
Contract Object Model

Represents agreements and contracts with customers.
"""

from analytics_models import ObjectModel

CONTRACT = ObjectModel(
    name="Contract",
    code="CONTRACT",
    description="Legal agreements and contracts with customers",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Contract {
}

class Customer {
}

class Renewal {
}

class Product {
}

' Relationships
Customer "1" -- "0..*" Contract : has >
Contract "1" -- "0..*" Renewal : has >
Contract "0..*" -- "1..*" Product : covers >

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

class SalesRepresentative {
}

class SalesTeam {
}

' Relationships to Related Objects
Contract "1" -- "*" Account : relates to
Contract "1" -- "*" ChannelPartner : relates to
Contract "1" -- "*" Customer : relates to
Contract "1" -- "*" Deal : relates to
Contract "1" -- "*" Lead : relates to
Contract "1" -- "*" Opportunity : relates to
Contract "1" -- "*" Product : relates to
Contract "1" -- "*" Sale : relates to
Contract "1" -- "*" SalesRepresentative : relates to
Contract "1" -- "*" SalesTeam : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "CONTRACT_RENEWAL_RATE"
        ],
        "key_attributes": [
            "contract_number",
            "start_date",
            "end_date",
            "renewal_date",
            "contract_value",
            "terms",
            "status",
            "auto_renew"
        ],
        "related_objects": ["Account", "Channel Partner", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale", "Sales Representative", "Sales Team"]}
)
