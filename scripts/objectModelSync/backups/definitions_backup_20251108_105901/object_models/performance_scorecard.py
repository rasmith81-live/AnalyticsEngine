"""
Performance Scorecard Object Model

Represents performance scorecards for sales representatives and teams.
"""

from analytics_models import ObjectModel

PERFORMANCE_SCORECARD = ObjectModel(
    name="Performance Scorecard",
    code="PERFORMANCE_SCORECARD",
    description="Performance scorecards tracking sales representative and team metrics",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class PerformanceScorecard {
}

class SalesRepresentative {
}

class SalesTeam {
}

class Metric {
}

class PerformanceBenchmark {
}

class PerformanceReview {
}

class Compensation {
}

' Relationships
SalesRepresentative "1" -- "0..*" PerformanceScorecard : has >
SalesTeam "1" -- "0..*" PerformanceScorecard : has >
PerformanceScorecard "1" -- "1..*" Metric : tracks >
PerformanceScorecard "0..*" -- "0..*" PerformanceBenchmark : compared to >
PerformanceScorecard "1" -- "0..*" PerformanceReview : drives >
PerformanceScorecard "1" -- "0..1" Compensation : influences >

@enduml

' Related Objects

class Call {
}

class ChannelPartner {
}

class Customer {
}

class Deal {
}

class Email {
}

class Lead {
}

class Meeting {
}

class Opportunity {
}

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
""",
    
    is_active=True,
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
