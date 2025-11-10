"""
Field Visit Object Model

Represents in-person customer visits made by field sales representatives.
"""

from analytics_models import ObjectModel

FIELD_VISIT = ObjectModel(
    name="Field Visit",
    code="FIELD_VISIT",
    description="In-person customer visits by field sales representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class FieldVisit {
}

class SalesRepresentative {
}

class Account {
}

class Customer {
}

class Opportunity {
}

' Relationships
SalesRepresentative "1" -- "0..*" FieldVisit : makes >
FieldVisit "0..*" -- "1" Account : to >
FieldVisit "0..*" -- "0..1" Customer : with >
FieldVisit "1" -- "0..1" Opportunity : may result in >

@enduml
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "related_kpis": [
            "NUMBER_OF_CUSTOMER_VISITS",
            "SALES_CALL_EFFECTIVENESS",
            "TIME_SPENT_SELLING"
        ],
        "key_attributes": [
            "visit_id",
            "rep_id",
            "account_id",
            "date",
            "duration",
            "purpose",
            "outcome",
            "travel_time",
            "effectiveness_score"
        ]
    }
)
