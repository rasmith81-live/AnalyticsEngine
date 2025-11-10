"""
Lead Object Model

Represents potential customers showing interest in products/services.
"""

from analytics_models import ObjectModel

LEAD = ObjectModel(
    name="Lead",
    code="LEAD",
    description="Potential customers who have shown interest in the company's offerings",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Lead {
}

class Account {
}

class Opportunity {
}

class SalesRepresentative {
}

class LeadScore {
}

' Sales Development Specific
class OutboundCall {
}

class LeadQualification {
}

class Prospect {
}

' Relationships - Core
Account "1" -- "0..*" Lead : generates >
Lead "1" -- "0..1" Opportunity : converts to >
SalesRepresentative "1" -- "0..*" Lead : manages >
Lead "1" -- "0..1" LeadScore : has >

' Relationships - Sales Development
OutboundCall "0..*" -- "0..1" Lead : to >
Lead "1" -- "0..1" LeadQualification : undergoes >
Lead "0..1" -- "0..1" Prospect : becomes >

@enduml

' Related Objects

class Appointment {
}

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

class Deal {
}

class Goal {
}

class Meeting {
}

class PerformanceScorecard {
}

class Product {
}

' Relationships to Related Objects
Lead "1" -- "*" Account : relates to
Lead "1" -- "*" Appointment : relates to
Lead "1" -- "*" Assessment : relates to
Lead "1" -- "*" Benchmark : relates to
Lead "1" -- "*" Call : relates to
Lead "1" -- "*" ChannelPartner : relates to
Lead "1" -- "*" CoachingSession : relates to
Lead "1" -- "*" Contract : relates to
Lead "1" -- "*" Customer : relates to
Lead "1" -- "*" Deal : relates to
Lead "1" -- "*" Goal : relates to
Lead "1" -- "*" Meeting : relates to
Lead "1" -- "*" Opportunity : manages
Lead "1" -- "*" PerformanceScorecard : relates to
Lead "1" -- "*" Product : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT"],
        "related_kpis": [
            "COST_PER_LEAD",
            "LEAD_RESPONSE_TIME",
            "LEAD_QUALITY_SCORE",
            "LEAD_NURTURING_SUCCESS_RATE",
            "LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
            "MARKETING_QUALIFIED_LEADS_MQL",
            "SALES_QUALIFIED_LEADS_SQL",
            "QUALIFIED_LEADS_PER_MONTH",
            "AVERAGE_LEAD_SCORE"
        ],
        "key_attributes": [
            "lead_source",
            "contact_name",
            "contact_email",
            "contact_phone",
            "company",
            "status",
            "score",
            "assigned_to",
            "created_date",
            "last_contact_date"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Benchmark", "Call", "Channel Partner", "Coaching Session", "Contract", "Customer", "Deal", "Goal", "Meeting", "Opportunity", "Performance Scorecard", "Product"]}
)
