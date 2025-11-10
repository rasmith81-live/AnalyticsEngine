"""
Stakeholder Object Model

Represents stakeholders within key accounts for multi-level engagement.
"""

from analytics_models import ObjectModel

STAKEHOLDER = ObjectModel(
    name="Stakeholder",
    code="STAKEHOLDER",
    description="Key stakeholders within strategic accounts",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Stakeholder {
}

class KeyAccount {
}

class KeyAccountManager {
}

class InfluenceNetwork {
}

' Relationships
KeyAccount "1" -- "1..*" Stakeholder : has >
KeyAccountManager "0..*" -- "0..*" Stakeholder : engages >
Stakeholder "0..*" -- "0..*" Stakeholder : influences >
Stakeholder "1" -- "0..1" InfluenceNetwork : part of >

@enduml
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "related_kpis": [
            "CUSTOMER_INFLUENCE_EFFECTIVENESS",
            "INTERDEPARTMENTAL_COLLABORATION_INDEX"
        ],
        "key_attributes": [
            "stakeholder_id",
            "account_id",
            "name",
            "role",
            "title",
            "department",
            "influence_level",
            "engagement_level",
            "decision_authority"
        ]
    }
)
