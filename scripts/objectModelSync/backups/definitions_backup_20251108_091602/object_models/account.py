"""
Account Object Model

Represents target companies/organizations in the sales process.
"""

from analytics_models import ObjectModel

ACCOUNT = ObjectModel(
    name="Account",
    code="ACCOUNT",
    description="Target companies or organizations in the sales pipeline",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class Account {
}

class SalesTeam {
}

class SalesRepresentative {
}

class Lead {
}

class Customer {
}

class Opportunity {
}

' Outside Sales Specific
class SalesTerritory {
}

class FieldVisit {
}

class SalesAppointment {
}

' Key Account Management
class KeyAccount {
}

' Relationships - Sales Management
SalesTeam "1..*" -- "0..*" Account : manages >
SalesRepresentative "1" -- "0..*" Account : manages >

' Relationships - Sales Process
Account "1" -- "0..*" Lead : generates >
Account "1" -- "0..1" Customer : becomes >
Account "1" -- "0..*" Opportunity : has >

' Relationships - Outside Sales
SalesTerritory "1" -- "0..*" Account : contains >
FieldVisit "0..*" -- "1" Account : to >
SalesAppointment "0..*" -- "1" Account : with >

' Relationships - Key Account Management
Account "0..1" -- "0..1" KeyAccount : may be >

@enduml

' Related Objects

class Call {
}

class Contract {
}

class Deal {
}

class Product {
}

class SalesPipeline {
}

class SalesQuota {
}

class Subscription {
}

class SupportTicket {
}

' Relationships to Related Objects
Account "1" -- "*" Call : relates to
Account "1" -- "*" Contract : relates to
Account "1" -- "*" Customer : relates to
Account "1" -- "*" Deal : manages
Account "1" -- "*" Lead : relates to
Account "1" -- "*" Opportunity : relates to
Account "1" -- "*" Product : relates to
Account "1" -- "*" Sale : relates to
Account "1" -- "*" SalesPipeline : relates to
Account "1" -- "*" SalesQuota : relates to
Account "1" -- "*" SalesRepresentative : relates to
Account "1" -- "*" SalesTeam : relates to
Account "1" -- "*" Subscription : relates to
Account "1" -- "*" SupportTicket : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "OUTSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT"],
        "related_kpis": [
            "ACCOUNT_COVERAGE_RATIO",
            "ACCOUNT_PENETRATION_RATE",
            "LAND_AND_EXPAND_SUCCESS_RATE"
        ],
        "key_attributes": [
            "account_name",
            "account_type",
            "industry",
            "size",
            "status",
            "assigned_team"
        ],
        "related_objects": ["Call", "Contract", "Customer", "Deal", "Lead", "Opportunity", "Product", "Sale", "Sales Pipeline", "Sales Quota", "Sales Representative", "Sales Team", "Subscription", "Support Ticket"]}
)
