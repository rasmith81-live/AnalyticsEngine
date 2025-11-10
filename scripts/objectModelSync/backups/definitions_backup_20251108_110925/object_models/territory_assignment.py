"""
Territory Assignment Object Model

Represents territory assignments to sales representatives.
"""

from analytics_models import ObjectModel

TERRITORY_ASSIGNMENT = ObjectModel(
    name="Territory Assignment",
    code="TERRITORY_ASSIGNMENT",
    description="Territory assignments and management for sales representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class TerritoryAssignment {
}

class SalesOperationsTeam {
}

class SalesTerritory {
}

class SalesRepresentative {
}

class QuotaPlan {
}

' Relationships
SalesOperationsTeam "1" -- "0..*" TerritoryAssignment : manages >
TerritoryAssignment "1" -- "1" SalesTerritory : assigns >
TerritoryAssignment "1" -- "1" SalesRepresentative : to >
TerritoryAssignment "1" -- "1" QuotaPlan : defines >

@enduml

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
""",
    
    is_active=True,
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
