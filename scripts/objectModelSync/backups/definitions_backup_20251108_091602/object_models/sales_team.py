"""
Sales Team Object Model

Represents groups of sales representatives working together.
"""

from analytics_models import ObjectModel

SALES_TEAM = ObjectModel(
    name="Sales Team",
    code="SALES_TEAM",
    description="Group of sales representatives organized to manage accounts and drive revenue",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesTeam {
}

class SalesRepresentative {
}

class Account {
}

class SalesQuota {
}

class Territory {
}

' Relationships
SalesTeam "1" -- "1..*" SalesRepresentative : has >
SalesTeam "1" -- "0..*" Account : manages >
SalesTeam "1" -- "1" SalesQuota : assigned >
SalesTeam "1" -- "0..1" Territory : covers >

@enduml

' Related Objects

class Appointment {
}

class Assessment {
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

class Demo {
}

class Goal {
}

class Lead {
}

class Meeting {
}

class Opportunity {
}

class Product {
}

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
""",
    
    is_active=True,
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
