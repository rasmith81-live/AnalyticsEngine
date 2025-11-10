"""
Sales Playbook Object Model

Represents sales playbooks with best practices and processes.
"""

from analytics_models import ObjectModel

SALES_PLAYBOOK = ObjectModel(
    name="Sales Playbook",
    code="SALES_PLAYBOOK",
    description="Sales playbooks containing best practices and standardized processes",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesPlaybook {
}

class SalesRepresentative {
}

class EnablementTeam {
}

class BestPractice {
}

class SalesProcess {
}

' Relationships
EnablementTeam "1" -- "0..*" SalesPlaybook : creates >
SalesRepresentative "0..*" -- "0..*" SalesPlaybook : adopts >
SalesPlaybook "1" -- "0..*" BestPractice : contains >
SalesPlaybook "1" -- "1" SalesProcess : defines >

@enduml

' Related Objects

class SalesTeam {
}

' Relationships to Related Objects
SalesPlaybook "1" -- "*" Sale : relates to
SalesPlaybook "1" -- "*" SalesRepresentative : relates to
SalesPlaybook "1" -- "*" SalesTeam : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "related_kpis": [
            "SALES_PLAYBOOK_ADOPTION_RATE",
            "SALES_PROCESS_COMPLIANCE_RATE",
            "SALES_BEST_PRACTICE_SHARING_RATE"
        ],
        "key_attributes": [
            "playbook_id",
            "name",
            "adoption_rate",
            "compliance_rate",
            "last_updated",
            "version"
        ],
        "related_objects": ["Sale", "Sales Representative", "Sales Team"]}
)
