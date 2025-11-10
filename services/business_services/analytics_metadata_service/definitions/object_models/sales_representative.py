"""
Sales Representative Object Model

Represents individual salespeople on the team.
"""

from analytics_models import ObjectModel

SALES_REP = ObjectModel(
    name="Sales Representative",
    code="SALES_REP",
    description="Individual salesperson responsible for managing leads, opportunities, and deals",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "sales_rep",
        "class_name": "Sales Representative",
        "columns": [
            {
                "name": "rep_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "employee_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "hire_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "team_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "quota",
                "type": "String",
                "length": 255
            },
            {
                "name": "quota_attainment",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "total_revenue",
                "type": "String",
                "length": 255
            },
            {
                "name": "training_status",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "performance_rating",
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
                "name": "ix_sales_rep_employee_id",
                "columns": ["employee_id"]
            },
            {
                "name": "ix_sales_rep_hire_date",
                "columns": ["hire_date"]
            },
            {
                "name": "ix_sales_rep_team_id",
                "columns": ["team_id"]
            },
            {
                "name": "ix_sales_rep_quota_attainment",
                "columns": ["quota_attainment"]
            },
            {
                "name": "ix_sales_rep_training_status",
                "columns": ["training_status"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesTeam "1" -- "1..*" SalesRepresentative : has >
SalesRepresentative "1" -- "0..*" Lead : manages >
SalesRepresentative "1" -- "0..*" Opportunity : owns >
SalesRepresentative "1" -- "0..*" Deal : handles >
SalesRepresentative "1" -- "1" SalesQuota : has >
SalesRepresentative "1" -- "0..*" SalesActivity : performs >
SalesRepresentative "1" -- "0..*" Training : completes >
' Related Objects
' Relationships to Related Objects
SalesRepresentative "1" -- "*" Account : relates to
SalesRepresentative "1" -- "*" Appointment : relates to
SalesRepresentative "1" -- "*" Assessment : relates to
SalesRepresentative "1" -- "*" Benchmark : relates to
SalesRepresentative "1" -- "*" Call : relates to
SalesRepresentative "1" -- "*" Certification : relates to
SalesRepresentative "1" -- "*" ChannelPartner : relates to
SalesRepresentative "1" -- "*" CoachingSession : relates to
SalesRepresentative "1" -- "*" Contract : relates to
SalesRepresentative "1" -- "*" Customer : relates to
SalesRepresentative "1" -- "*" Deal : relates to
SalesRepresentative "1" -- "*" Demo : relates to
SalesRepresentative "1" -- "*" Email : relates to
SalesRepresentative "1" -- "*" Goal : relates to
SalesRepresentative "1" -- "*" Lead : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "REVENUE_PER_SALES_REPRESENTATIVE",
            "QUOTA_ATTAINMENT_RATE",
            "SALES_TRAINING_COMPLETION_RATE",
            "SALES_TEAM_RESPONSE_TIME",
            "LEAD_RESPONSE_TIME"
        ],
        "key_attributes": [
            "rep_name",
            "employee_id",
            "hire_date",
            "team_id",
            "quota",
            "quota_attainment",
            "total_revenue",
            "training_status",
            "performance_rating"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Certification", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Email", "Goal", "Lead"]}

)
