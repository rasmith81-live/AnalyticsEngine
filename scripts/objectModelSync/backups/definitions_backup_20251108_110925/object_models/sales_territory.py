"""
Sales Territory Object Model

Represents geographic sales territories assigned to field sales representatives.
"""

from analytics_models import ObjectModel

SALES_TERRITORY = ObjectModel(
    name="Sales Territory",
    code="SALES_TERRITORY",
    description="Geographic sales territories for field sales management",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesTerritory {
}

class SalesRepresentative {
}

class Account {
}

class MarketPotential {
}

' Relationships
SalesRepresentative "1" -- "0..*" SalesTerritory : assigned to >
SalesTerritory "1" -- "0..*" Account : contains >
SalesTerritory "1" -- "1" MarketPotential : has >

@enduml

' Related Objects

class Customer {
}

class Product {
}

class SalesContent {
}

class SalesTeam {
}

' Relationships to Related Objects
SalesTerritory "1" -- "*" Customer : relates to
SalesTerritory "1" -- "*" Product : relates to
SalesTerritory "1" -- "*" Sale : relates to
SalesTerritory "1" -- "*" SalesContent : relates to
SalesTerritory "1" -- "*" SalesRepresentative : relates to
SalesTerritory "1" -- "*" SalesTeam : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "related_kpis": [
            "TERRITORY_PENETRATION_RATE",
            "MARKET_PENETRATION_RATE"
        ],
        "key_attributes": [
            "territory_id",
            "territory_name",
            "geographic_area",
            "account_count",
            "potential_value",
            "penetration_rate",
            "assigned_rep_id"
        ],
        "related_objects": ["Customer", "Product", "Sale", "Sales Content", "Sales Representative", "Sales Team"]}
)
