"""
Prospect Object Model

Represents active prospects being engaged by sales development.
"""

from analytics_models import ObjectModel

PROSPECT = ObjectModel(
    name="Prospect",
    code="PROSPECT",
    description="Active prospects being engaged and qualified by sales development",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "prospect",
        "class_name": "Prospect",
        "columns": [
            {
                "name": "prospect_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "contact_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "company",
                "type": "String",
                "length": 255
            },
            {
                "name": "title",
                "type": "String",
                "length": 255
            },
            {
                "name": "email",
                "type": "String",
                "length": 255,
                "unique": True
            },
            {
                "name": "phone",
                "type": "String",
                "length": 255
            },
            {
                "name": "status",
                "type": "String",
                "length": 255
            },
            {
                "name": "engagement_score",
                "type": "Float"
            },
            {
                "name": "assigned_sdr",
                "type": "String",
                "length": 255
            },
            {
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            },
            {
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            }
        ],
        "indexes": [
            {
                "name": "ix_prospect_prospect_id",
                "columns": ["prospect_id"]
            },
            {
                "name": "ix_prospect_email",
                "columns": ["email"],
                "unique": True
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Lead "0..1" -- "0..1" Prospect : becomes >
SalesRepresentative "1" -- "0..*" Prospect : engages >
OutboundCall "0..*" -- "0..1" Prospect : to >
Appointment "0..*" -- "1" Prospect : with >
Prospect "1" -- "1" ProspectEngagement : has >
Prospect "0..1" -- "0..1" Opportunity : converts to >
' Relationships to Related Objects
Prospect "1" -- "*" EnablementFeedback : relates to
Prospect "1" -- "*" EnablementPlatform : relates to
Prospect "1" -- "*" ProspectEngagement : relates to
Prospect "1" -- "*" ServiceLevelAgreement : relates to
@enduml
    """,

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
