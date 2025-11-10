"""
Sales Quota Object Model

Represents sales targets and quotas for teams and individuals.
"""

from analytics_models import ObjectModel

SALES_QUOTA = ObjectModel(
    name="Sales Quota",
    code="SALES_QUOTA",
    description="Sales targets and quotas assigned to teams and representatives",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesQuota {
}

class SalesRepresentative {
}

class SalesTeam {
}

class Period {
}

' Relationships
SalesRepresentative "1" -- "1" SalesQuota : has >
SalesTeam "1" -- "1" SalesQuota : assigned >
SalesQuota "0..*" -- "1" Period : for >

@enduml

' Related Objects

class Account {
}

class ChannelPartner {
}

class CoachingSession {
}

class Customer {
}

class Deal {
}

class Lead {
}

class Meeting {
}

class Opportunity {
}

class Product {
}

class SalesContent {
}

class SalesPipeline {
}

class SupportTicket {
}

' Relationships to Related Objects
SalesQuota "1" -- "*" Account : relates to
SalesQuota "1" -- "*" ChannelPartner : relates to
SalesQuota "1" -- "*" CoachingSession : relates to
SalesQuota "1" -- "*" Customer : relates to
SalesQuota "1" -- "*" Deal : relates to
SalesQuota "1" -- "*" Lead : relates to
SalesQuota "1" -- "*" Meeting : relates to
SalesQuota "1" -- "*" Opportunity : relates to
SalesQuota "1" -- "*" Product : relates to
SalesQuota "1" -- "*" Sale : relates to
SalesQuota "1" -- "*" SalesContent : relates to
SalesQuota "1" -- "*" SalesPipeline : relates to
SalesQuota "1" -- "*" SalesRepresentative : relates to
SalesQuota "1" -- "*" SalesTeam : relates to
SalesQuota "1" -- "*" SupportTicket : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "QUOTA_ATTAINMENT_RATE"
        ],
        "key_attributes": [
            "quota_amount",
            "period",
            "start_date",
            "end_date",
            "actual_amount",
            "attainment_percentage",
            "assignee_type",
            "assignee_id"
        ],
        "related_objects": ["Account", "Channel Partner", "Coaching Session", "Customer", "Deal", "Lead", "Meeting", "Opportunity", "Product", "Sale", "Sales Content", "Sales Pipeline", "Sales Representative", "Sales Team", "Support Ticket"]}
)
