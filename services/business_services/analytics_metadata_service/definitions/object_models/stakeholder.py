"""
Stakeholder Object Model

Represents stakeholders within key accounts for multi-level engagement.
"""

from analytics_models import ObjectModel

STAKEHOLDER = ObjectModel(
    name="Stakeholder",
    code="STAKEHOLDER",
    description="Key stakeholders within strategic accounts",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "stakeholder",
        "class_name": "Stakeholder",
        "columns": [
            {
                "name": "stakeholder_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "account_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "name",
                "type": "String",
                "length": 255
            },
            {
                "name": "role",
                "type": "String",
                "length": 255
            },
            {
                "name": "title",
                "type": "String",
                "length": 255
            },
            {
                "name": "department",
                "type": "String",
                "length": 255
            },
            {
                "name": "influence_level",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "engagement_level",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "decision_authority",
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
                "name": "ix_stakeholder_stakeholder_id",
                "columns": ["stakeholder_id"]
            },
            {
                "name": "ix_stakeholder_account_id",
                "columns": ["account_id"]
            },
            {
                "name": "ix_stakeholder_influence_level",
                "columns": ["influence_level"]
            },
            {
                "name": "ix_stakeholder_engagement_level",
                "columns": ["engagement_level"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
KeyAccount "1" -- "1..*" Stakeholder : has >
KeyAccountManager "0..*" -- "0..*" Stakeholder : engages >
Stakeholder "0..*" -- "0..*" Stakeholder : influences >
Stakeholder "1" -- "0..1" InfluenceNetwork : part of >
@enduml
    """,

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
