"""
Field Visit Object Model

Represents in-person customer visits made by field sales representatives.
"""

from analytics_models import ObjectModel

FIELD_VISIT = ObjectModel(
    name="Field Visit",
    code="FIELD_VISIT",
    description="In-person customer visits by field sales representatives",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "field_visit",
        "class_name": "Field Visit",
        "columns": [
            {
                "name": "visit_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "rep_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "account_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "date",
                "type": "String",
                "length": 255
            },
            {
                "name": "duration",
                "type": "String",
                "length": 255
            },
            {
                "name": "purpose",
                "type": "String",
                "length": 255
            },
            {
                "name": "outcome",
                "type": "String",
                "length": 255
            },
            {
                "name": "travel_time",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "effectiveness_score",
                "type": "Float"
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
                "name": "ix_field_visit_visit_id",
                "columns": ["visit_id"]
            },
            {
                "name": "ix_field_visit_rep_id",
                "columns": ["rep_id"]
            },
            {
                "name": "ix_field_visit_account_id",
                "columns": ["account_id"]
            },
            {
                "name": "ix_field_visit_travel_time",
                "columns": ["travel_time"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" FieldVisit : makes >
FieldVisit "0..*" -- "1" Account : to >
FieldVisit "0..*" -- "0..1" Customer : with >
FieldVisit "1" -- "0..1" Opportunity : may result in >
@enduml
    """,

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
