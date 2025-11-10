"""
Sales Content Object Model

Represents sales content, collateral, and materials.
"""

from analytics_models import ObjectModel

SALES_CONTENT = ObjectModel(
    name="Sales Content",
    code="SALES_CONTENT",
    description="Sales content, collateral, and materials for sales effectiveness",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesContent {
}

class SalesRepresentative {
}

class EnablementTeam {
}

class EnablementPlatform {
}

class Product {
}

' Relationships
EnablementTeam "1" -- "0..*" SalesContent : creates >
SalesRepresentative "0..*" -- "0..*" SalesContent : uses >
EnablementPlatform "1" -- "0..*" SalesContent : hosts >
SalesContent "0..*" -- "0..*" Product : for >

@enduml

' Related Objects

class Assessment {
}

class Customer {
}

class Deal {
}

class Lead {
}

class Opportunity {
}

class Proposal {
}

class SalesQuota {
}

class SalesTeam {
}

class SalesTerritory {
}

class TrainingProgram {
}

' Relationships to Related Objects
SalesContent "1" -- "*" Assessment : relates to
SalesContent "1" -- "*" Customer : relates to
SalesContent "1" -- "*" Deal : relates to
SalesContent "1" -- "*" Lead : relates to
SalesContent "1" -- "*" Opportunity : relates to
SalesContent "1" -- "*" Product : relates to
SalesContent "1" -- "*" Proposal : relates to
SalesContent "1" -- "*" Sale : relates to
SalesContent "1" -- "*" SalesQuota : relates to
SalesContent "1" -- "*" SalesRepresentative : relates to
SalesContent "1" -- "*" SalesTeam : relates to
SalesContent "1" -- "*" SalesTerritory : relates to
SalesContent "1" -- "*" TrainingProgram : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "related_kpis": [
            "CONTENT_UTILIZATION_RATE",
            "SALES_CONTENT_USAGE_RATE",
            "SALES_CONTENT_EFFECTIVENESS_RATE",
            "SALES_CONTENT_PERSONALIZATION_RATE"
        ],
        "key_attributes": [
            "content_id",
            "type",
            "title",
            "usage_rate",
            "effectiveness_score",
            "last_updated",
            "personalization_level"
        ],
        "related_objects": ["Assessment", "Customer", "Deal", "Lead", "Opportunity", "Product", "Proposal", "Sale", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Training Program"]}
)
