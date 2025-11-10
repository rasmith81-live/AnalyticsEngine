"""
Territory Assignment Object Model

Represents territory assignments to sales representatives.
"""

from analytics_models import ObjectModel

TERRITORY_ASSIGNMENT = ObjectModel(
    name="Territory Assignment",
    code="TERRITORY_ASSIGNMENT",
    description="Territory assignments and management for sales representatives",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "territory_assignment",
        "class_name": "Territory Assignment",
        "columns": [
            {
                "name": "assignment_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "territory_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "rep_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "effective_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "account_count",
                "type": "Integer"
            },
            {
                "name": "quota",
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
                "name": "ix_territory_assignment_assignment_id",
                "columns": ["assignment_id"]
            },
            {
                "name": "ix_territory_assignment_territory_id",
                "columns": ["territory_id"]
            },
            {
                "name": "ix_territory_assignment_rep_id",
                "columns": ["rep_id"]
            },
            {
                "name": "ix_territory_assignment_effective_date",
                "columns": ["effective_date"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesOperationsTeam "1" -- "0..*" TerritoryAssignment : manages >
TerritoryAssignment "1" -- "1" SalesTerritory : assigns >
TerritoryAssignment "1" -- "1" SalesRepresentative : to >
TerritoryAssignment "1" -- "1" QuotaPlan : defines >
' Relationships to Related Objects
TerritoryAssignment "1" -- "*" AccountPenetration : relates to
TerritoryAssignment "1" -- "*" Appointment : relates to
TerritoryAssignment "1" -- "*" CompetitiveAnalysis : relates to
TerritoryAssignment "1" -- "*" Deal : relates to
TerritoryAssignment "1" -- "*" KnowledgeBase : relates to
TerritoryAssignment "1" -- "*" Lead : relates to
TerritoryAssignment "1" -- "*" MarketSegment : relates to
TerritoryAssignment "1" -- "*" Meeting : relates to
TerritoryAssignment "1" -- "*" Opportunity : relates to
TerritoryAssignment "1" -- "*" PerformanceBenchmark : relates to
TerritoryAssignment "1" -- "*" PerformanceScorecard : relates to
TerritoryAssignment "1" -- "*" ProductAdoption : relates to
TerritoryAssignment "1" -- "*" ProductUsage : relates to
TerritoryAssignment "1" -- "*" QuarterlyBusinessReview : relates to
TerritoryAssignment "1" -- "*" QuotaPlan : relates to
TerritoryAssignment "1" -- "*" RenewalManagement : relates to
TerritoryAssignment "1" -- "*" Sale : relates to
TerritoryAssignment "1" -- "*" SalesActivity : relates to
TerritoryAssignment "1" -- "*" SalesAppointment : relates to
TerritoryAssignment "1" -- "*" SalesAssessment : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "ACCOUNT_PENETRATION_RATE",
            "SALES_BY_REGION"
        ],
        "key_attributes": [
            "assignment_id",
            "territory_id",
            "rep_id",
            "effective_date",
            "account_count",
            "quota"
        ],
        "related_objects": ["Account Penetration", "Appointment", "Competitive Analysis", "Deal", "Knowledge Base", "Lead", "Market Segment", "Meeting", "Opportunity", "Performance Benchmark", "Performance Scorecard", "Product Adoption", "Product Usage", "Quarterly Business Review", "Quota Plan", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment"]}

)
