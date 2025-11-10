"""
Prospect Object Model

Represents active prospects being engaged by sales development.
"""

from analytics_models import ObjectModel

PROSPECT = ObjectModel(
    name="Prospect",
    code="PROSPECT",
    description="Active prospects being engaged and qualified by sales development",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Prospect {
}

class Lead {
}

class SalesRepresentative {
}

class OutboundCall {
}

class Appointment {
}

class ProspectEngagement {
}

class Opportunity {
}

' Relationships
Lead "0..1" -- "0..1" Prospect : becomes >
SalesRepresentative "1" -- "0..*" Prospect : engages >
OutboundCall "0..*" -- "0..1" Prospect : to >
Appointment "0..*" -- "1" Prospect : with >
Prospect "1" -- "1" ProspectEngagement : has >
Prospect "0..1" -- "0..1" Opportunity : converts to >

@enduml

' Relationships to Related Objects
Prospect "1" -- "*" EnablementFeedback : relates to
Prospect "1" -- "*" EnablementPlatform : relates to
Prospect "1" -- "*" ProspectEngagement : relates to
Prospect "1" -- "*" ServiceLevelAgreement : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT"],
        "related_kpis": [
            "NUMBER_OF_ACTIVE_PROSPECTS",
            "PROSPECT_ENGAGEMENT_SCORE"
        ],
        "key_attributes": [
            "prospect_id",
            "contact_name",
            "company",
            "title",
            "email",
            "phone",
            "status",
            "engagement_score",
            "assigned_sdr"
        ],
        "related_objects": ["Enablement Feedback", "Enablement Platform", "Prospect Engagement", "Service Level Agreement"]}
)
