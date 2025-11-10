"""
Performance Scorecard Object Model

Represents performance scorecards for sales representatives and teams.
"""

from analytics_models import ObjectModel

PERFORMANCE_SCORECARD = ObjectModel(
    name="Performance Scorecard",
    code="PERFORMANCE_SCORECARD",
    description="Performance scorecards tracking sales representative and team metrics",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "performance_scorecard",
        "class_name": "Performance Scorecard",
        "columns": [
            {
                "name": "scorecard_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "rep_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "team_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "period",
                "type": "String",
                "length": 255
            },
            {
                "name": "metrics",
                "type": "String",
                "length": 255
            },
            {
                "name": "scores",
                "type": "String",
                "length": 255
            },
            {
                "name": "ranking",
                "type": "String",
                "length": 255
            },
            {
                "name": "benchmark_comparison",
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
                "name": "ix_performance_scorecard_scorecard_id",
                "columns": ["scorecard_id"]
            },
            {
                "name": "ix_performance_scorecard_rep_id",
                "columns": ["rep_id"]
            },
            {
                "name": "ix_performance_scorecard_team_id",
                "columns": ["team_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" PerformanceScorecard : has >
SalesTeam "1" -- "0..*" PerformanceScorecard : has >
PerformanceScorecard "1" -- "1..*" Metric : tracks >
PerformanceScorecard "0..*" -- "0..*" PerformanceBenchmark : compared to >
PerformanceScorecard "1" -- "0..*" PerformanceReview : drives >
PerformanceScorecard "1" -- "0..1" Compensation : influences >
' Related Objects
' Relationships to Related Objects
PerformanceScorecard "1" -- "*" Call : relates to
PerformanceScorecard "1" -- "*" ChannelPartner : relates to
PerformanceScorecard "1" -- "*" Customer : relates to
PerformanceScorecard "1" -- "*" Deal : relates to
PerformanceScorecard "1" -- "*" Email : relates to
PerformanceScorecard "1" -- "*" Lead : relates to
PerformanceScorecard "1" -- "*" Meeting : relates to
PerformanceScorecard "1" -- "*" Opportunity : relates to
PerformanceScorecard "1" -- "*" Sale : relates to
PerformanceScorecard "1" -- "*" SalesRepresentative : relates to
@enduml
    """,

    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "related_kpis": [
            "QUOTA_ATTAINMENT_PER_SALESPERSON",
            "SALES_PER_REPRESENTATIVE",
            "SALES_PRODUCTIVITY",
            "SALES_FORCE_EFFECTIVENESS"
        ],
        "key_attributes": [
            "scorecard_id",
            "rep_id",
            "team_id",
            "period",
            "metrics",
            "scores",
            "ranking",
            "benchmark_comparison"
        ],
        "related_objects": ["Call", "Channel Partner", "Customer", "Deal", "Email", "Lead", "Meeting", "Opportunity", "Sale", "Sales Representative"]}

)
