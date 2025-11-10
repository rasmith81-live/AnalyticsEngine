"""
Performance Benchmark Object Model

Represents performance benchmarks and standards for comparison.
"""

from analytics_models import ObjectModel

PERFORMANCE_BENCHMARK = ObjectModel(
    name="Performance Benchmark",
    code="PERFORMANCE_BENCHMARK",
    description="Performance benchmarks and standards for sales performance comparison",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "performance_benchmark",
        "class_name": "Performance Benchmark",
        "columns": [
            {
                "name": "benchmark_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "metric_name",
                "type": "String",
                "length": 255
            },
            {
                "name": "industry_average",
                "type": "String",
                "length": 255
            },
            {
                "name": "top_performer",
                "type": "String",
                "length": 255
            },
            {
                "name": "target",
                "type": "String",
                "length": 255
            },
            {
                "name": "actual",
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
                "name": "ix_performance_benchmark_benchmark_id",
                "columns": ["benchmark_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
PerformanceBenchmark "1" -- "1" Metric : for >
PerformanceScorecard "0..*" -- "0..*" PerformanceBenchmark : compared to >
PerformanceBenchmark "0..*" -- "0..1" Industry : varies by >
PerformanceBenchmark "0..*" -- "0..1" Role : varies by >
' Relationships to Related Objects
PerformanceBenchmark "1" -- "*" Account : relates to
PerformanceBenchmark "1" -- "*" AccountPenetration : relates to
PerformanceBenchmark "1" -- "*" AccountPlan : relates to
PerformanceBenchmark "1" -- "*" AccountRisk : relates to
PerformanceBenchmark "1" -- "*" Benchmark : relates to
PerformanceBenchmark "1" -- "*" Call : relates to
PerformanceBenchmark "1" -- "*" ChannelConflict : relates to
PerformanceBenchmark "1" -- "*" ChannelDeal : relates to
PerformanceBenchmark "1" -- "*" ChannelMarket : relates to
PerformanceBenchmark "1" -- "*" ChannelPartner : relates to
PerformanceBenchmark "1" -- "*" CoachingSession : relates to
PerformanceBenchmark "1" -- "*" CompetitiveAnalysis : relates to
PerformanceBenchmark "1" -- "*" Customer : relates to
PerformanceBenchmark "1" -- "*" CustomerAdvocacyProgram : relates to
PerformanceBenchmark "1" -- "*" CustomerCohort : relates to
PerformanceBenchmark "1" -- "*" CustomerCommunity : relates to
PerformanceBenchmark "1" -- "*" CustomerEducation : relates to
PerformanceBenchmark "1" -- "*" CustomerFeedback : relates to
PerformanceBenchmark "1" -- "*" CustomerGoal : relates to
PerformanceBenchmark "1" -- "*" CustomerHealthRecord : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_FORCE_EFFECTIVENESS",
            "SALES_PRODUCTIVITY"
        ],
        "key_attributes": [
            "benchmark_id",
            "metric_name",
            "industry_average",
            "top_performer",
            "target",
            "actual"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Benchmark", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Coaching Session", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}

)
