"""
Outbound Call Object Model

Represents outbound sales calls made by SDRs/BDRs during prospecting.
"""

from analytics_models import ObjectModel

OUTBOUND_CALL = ObjectModel(
    name="Outbound Call",
    code="OUTBOUND_CALL",
    description="Outbound sales calls made during prospecting and lead qualification",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class OutboundCall {
}

class SalesRepresentative {
}

class Prospect {
}

class Lead {
}

class Appointment {
}

' Relationships
SalesRepresentative "1" -- "0..*" OutboundCall : makes >
OutboundCall "0..*" -- "0..1" Prospect : to >
OutboundCall "0..*" -- "0..1" Lead : to >
OutboundCall "1" -- "0..1" Appointment : may result in >

@enduml

' Relationships to Related Objects
OutboundCall "1" -- "*" Account : relates to
OutboundCall "1" -- "*" AccountPenetration : relates to
OutboundCall "1" -- "*" AccountPlan : relates to
OutboundCall "1" -- "*" AccountRisk : relates to
OutboundCall "1" -- "*" Appointment : relates to
OutboundCall "1" -- "*" Call : relates to
OutboundCall "1" -- "*" CompetitiveAnalysis : relates to
OutboundCall "1" -- "*" Deal : relates to
OutboundCall "1" -- "*" EnablementFeedback : relates to
OutboundCall "1" -- "*" EnablementPlatform : relates to
OutboundCall "1" -- "*" Goal : relates to
OutboundCall "1" -- "*" KeyAccount : relates to
OutboundCall "1" -- "*" KeyAccountManager : relates to
OutboundCall "1" -- "*" Lead : relates to
OutboundCall "1" -- "*" LeadQualification : relates to
OutboundCall "1" -- "*" LostSale : relates to
OutboundCall "1" -- "*" Meeting : relates to
OutboundCall "1" -- "*" Opportunity : relates to
OutboundCall "1" -- "*" PerformanceBenchmark : relates to
OutboundCall "1" -- "*" PerformanceScorecard : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
        "related_kpis": [
            "OUTBOUND_CALLS_PER_DAY",
            "OUTBOUND_CALL_CONVERSION_RATE",
            "SALES_CALL_EFFECTIVENESS"
        ],
        "key_attributes": [
            "call_id",
            "sdr_id",
            "prospect_id",
            "date",
            "duration",
            "outcome",
            "disposition",
            "follow_up_required"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Call", "Competitive Analysis", "Deal", "Enablement Feedback", "Enablement Platform", "Goal", "Key Account", "Key Account Manager", "Lead", "Lead Qualification", "Lost Sale", "Meeting", "Opportunity", "Performance Benchmark", "Performance Scorecard"]}
)
