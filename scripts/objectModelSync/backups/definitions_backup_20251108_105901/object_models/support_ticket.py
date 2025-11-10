"""
Support Ticket Object Model

Represents customer support requests and issues.
"""

from analytics_models import ObjectModel

SUPPORT_TICKET = ObjectModel(
    name="Support Ticket",
    code="SUPPORT_TICKET",
    description="Customer service requests and support issues",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SupportTicket {
}

class Customer {
}

class Resolution {
}

' Support Teams
class SalesRepresentative {
}

class CustomerSuccessManager {
}

class SupportTeam {
}

' Related Entities
class CustomerHealthRecord {
}

class ServiceLevelAgreement {
}

class Escalation {
}

' Relationships - Creation
Customer "1" -- "0..*" SupportTicket : creates >

' Relationships - Handling
SalesRepresentative "1" -- "0..*" SupportTicket : handles >
CustomerSuccessManager "1" -- "0..*" SupportTicket : handles >
SupportTeam "1" -- "0..*" SupportTicket : manages >

' Relationships - Resolution & Impact
SupportTicket "1" -- "0..1" Resolution : has >
SupportTicket "0..*" -- "0..1" Escalation : may have >
SupportTicket "0..*" -- "1" CustomerHealthRecord : impacts >
SupportTicket "0..*" -- "0..1" ServiceLevelAgreement : governed by >

@enduml

' Related Objects

class Account {
}

class Appointment {
}

class Assessment {
}

class ChannelPartner {
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

class Proposal {
}

class SalesQuota {
}

class SalesTeam {
}

' Relationships to Related Objects
SupportTicket "1" -- "*" Account : relates to
SupportTicket "1" -- "*" Appointment : relates to
SupportTicket "1" -- "*" Assessment : relates to
SupportTicket "1" -- "*" ChannelPartner : relates to
SupportTicket "1" -- "*" Customer : relates to
SupportTicket "1" -- "*" Deal : relates to
SupportTicket "1" -- "*" Lead : relates to
SupportTicket "1" -- "*" Meeting : relates to
SupportTicket "1" -- "*" Opportunity : relates to
SupportTicket "1" -- "*" Product : relates to
SupportTicket "1" -- "*" Proposal : relates to
SupportTicket "1" -- "*" Sale : relates to
SupportTicket "1" -- "*" SalesQuota : relates to
SupportTicket "1" -- "*" SalesRepresentative : relates to
SupportTicket "1" -- "*" SalesTeam : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"],
        "related_kpis": [
            "CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME",
            "FIRST_CONTACT_RESOLUTION_FCR"
        ],
        "key_attributes": [
            "ticket_number",
            "created_date",
            "priority",
            "category",
            "status",
            "assigned_to",
            "resolution_time",
            "first_contact_resolved"
        ],
        "related_objects": ["Account", "Appointment", "Assessment", "Channel Partner", "Customer", "Deal", "Lead", "Meeting", "Opportunity", "Product", "Proposal", "Sale", "Sales Quota", "Sales Representative", "Sales Team"]}
)
