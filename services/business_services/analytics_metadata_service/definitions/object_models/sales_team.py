"""
Sales Team Object Model

Represents groups of sales representatives working together.
"""

from analytics_models import ObjectModel

SALES_TEAM = ObjectModel(
    name="Sales Team",
    code="SALES_TEAM",
    description="Group of sales representatives organized to manage accounts and drive revenue",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "sales_team",
        "class_name": "Sales Team",
        "columns": [
            {
                "name": "team_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "team_lead",
                "type": "String",
                "length": 255
            },
            {
                "name": "member_count",
                "type": "Integer"
            },
            {
                "name": "assigned_accounts",
                "type": "String",
                "length": 255
            },
            {
                "name": "target_accounts",
                "type": "String",
                "length": 255
            },
            {
                "name": "team_quota",
                "type": "String",
                "length": 255
            },
            {
                "name": "territory",
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
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesTeam "1" -- "1..*" SalesRepresentative : has >
SalesTeam "1" -- "0..*" Account : manages >
SalesTeam "1" -- "1" SalesQuota : assigned >
SalesTeam "1" -- "0..1" Territory : covers >
' Related Objects
' Relationships to Related Objects
SalesTeam "1" -- "*" Account : relates to
SalesTeam "1" -- "*" Appointment : relates to
SalesTeam "1" -- "*" Assessment : relates to
SalesTeam "1" -- "*" Call : relates to
SalesTeam "1" -- "*" ChannelPartner : relates to
SalesTeam "1" -- "*" CoachingSession : relates to
SalesTeam "1" -- "*" Contract : relates to
SalesTeam "1" -- "*" Customer : relates to
SalesTeam "1" -- "*" Deal : relates to
SalesTeam "1" -- "*" Demo : relates to
SalesTeam "1" -- "*" Goal : relates to
SalesTeam "1" -- "*" Lead : relates to
SalesTeam "1" -- "*" Meeting : relates to
SalesTeam "1" -- "*" Opportunity : relates to
SalesTeam "1" -- "*" Product : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "ACCOUNT_COVERAGE_RATIO",
            "SALES_TEAM_RESPONSE_TIME",
            "SALES_GROWTH"
        ],
        "key_attributes": [
            "team_name",
            "team_lead",
            "member_count",
            "assigned_accounts",
            "target_accounts",
            "team_quota",
            "territory"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Goal", "Lead", "Meeting", "Opportunity", "Product"]}

)
