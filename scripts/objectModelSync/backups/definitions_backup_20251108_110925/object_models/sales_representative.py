"""
Sales Representative Object Model

Represents individual salespeople on the team.
"""

from analytics_models import ObjectModel

SALES_REPRESENTATIVE = ObjectModel(
    name="Sales Representative",
    code="SALES_REP",
    description="Individual salesperson responsible for managing leads, opportunities, and deals",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesRepresentative {
}

class SalesTeam {
}

class Lead {
}

class Opportunity {
}

class Deal {
}

class SalesQuota {
}

class SalesActivity {
}

class Training {
}

' Relationships
SalesTeam "1" -- "1..*" SalesRepresentative : has >
SalesRepresentative "1" -- "0..*" Lead : manages >
SalesRepresentative "1" -- "0..*" Opportunity : owns >
SalesRepresentative "1" -- "0..*" Deal : handles >
SalesRepresentative "1" -- "1" SalesQuota : has >
SalesRepresentative "1" -- "0..*" SalesActivity : performs >
SalesRepresentative "1" -- "0..*" Training : completes >

@enduml

' Related Objects

class Account {
}

class Appointment {
}

class Assessment {
}

class Benchmark {
}

class Call {
}

class Certification {
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

class Email {
}

class Goal {
}

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
""",
    
    is_active=True,
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
