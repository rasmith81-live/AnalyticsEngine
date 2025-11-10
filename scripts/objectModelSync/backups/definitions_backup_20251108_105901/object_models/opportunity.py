"""
Opportunity Object Model

Represents qualified sales prospects in the pipeline.
"""

from analytics_models import ObjectModel

OPPORTUNITY = ObjectModel(
    name="Opportunity",
    code="OPPORTUNITY",
    description="Qualified sales prospects that have been vetted and are actively being pursued",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Opportunity {
}

class Lead {
}

class Deal {
}

class Account {
}

class SalesRepresentative {
}

class Pipeline {
}

' Sales Development Specific
class LeadQualification {
}

class Appointment {
}

class Prospect {
}

' Relationships - Core
Lead "1" -- "0..1" Opportunity : converts to >
Opportunity "1" -- "0..1" Deal : becomes >
Account "1" -- "0..*" Opportunity : has >
SalesRepresentative "1" -- "0..*" Opportunity : owns >
Pipeline "1" -- "0..*" Opportunity : contains >

' Relationships - Sales Development
LeadQualification "1" -- "0..1" Opportunity : creates (if SQL) >
Appointment "1" -- "0..1" Opportunity : may convert to >
Prospect "0..1" -- "0..1" Opportunity : converts to >

@enduml

' Related Objects

class Assessment {
}

class Benchmark {
}

class Call {
}

class ChannelPartner {
}

class CoachingSession {
}

class Contract {
}

class Customer {
}

class Demo {
}

class Goal {
}

class Meeting {
}

class PerformanceScorecard {
}

' Relationships to Related Objects
Opportunity "1" -- "*" Account : relates to
Opportunity "1" -- "*" Appointment : relates to
Opportunity "1" -- "*" Assessment : relates to
Opportunity "1" -- "*" Benchmark : relates to
Opportunity "1" -- "*" Call : relates to
Opportunity "1" -- "*" ChannelPartner : relates to
Opportunity "1" -- "*" CoachingSession : relates to
Opportunity "1" -- "*" Contract : relates to
Opportunity "1" -- "*" Customer : relates to
Opportunity "1" -- "*" Deal : manages
Opportunity "1" -- "*" Demo : relates to
Opportunity "1" -- "*" Goal : relates to
Opportunity "1" -- "*" Lead : relates to
Opportunity "1" -- "*" Meeting : relates to
Opportunity "1" -- "*" PerformanceScorecard : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT"],
        "related_kpis": [
            "COST_PER_OPPORTUNITY",
            "OPPORTUNITY_PIPELINE",
            "OPPORTUNITY_TO_CLOSE_RATE",
            "LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
            "NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED",
            "PIPELINE_GROWTH_RATE"
        ],
        "key_attributes": [
            "opportunity_name",
            "stage",
            "probability",
            "expected_value",
            "expected_close_date",
            "account_id",
            "owner_id",
            "created_date",
            "last_activity_date"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Demo", "Goal", "Lead", "Meeting", "Performance Scorecard"]}
)
