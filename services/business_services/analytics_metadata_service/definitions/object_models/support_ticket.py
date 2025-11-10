"""
Support Ticket Object Model

Represents customer support requests and issues.
"""

SUPPORT_TICKET = {
    "code": "SUPPORT_TICKET",
    "name": "Support Ticket",
    "description": "Customer service requests and support issues",
    "table_schema": {"table_name": "support_ticket", "class_name": "Support Ticket", "columns": [{"name": "ticket_number", "type": "Integer"}, {"name": "created_date", "type": "DateTime", "index": True}, {"name": "priority", "type": "String", "length": 255}, {"name": "category", "type": "String", "length": 255}, {"name": "status", "type": "String", "length": 255}, {"name": "assigned_to", "type": "String", "length": 255}, {"name": "resolution_time", "type": "DateTime", "index": True}, {"name": "first_contact_resolved", "type": "String", "length": 255}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_support_ticket_created_date", "columns": ["created_date"]}, {"name": "ix_support_ticket_resolution_time", "columns": ["resolution_time"]}]},
    "schema_definition": """
    @startuml
' Support Teams
' Related Entities
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
' Related Objects
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
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS"], "related_kpis": ["CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME", "FIRST_CONTACT_RESOLUTION_FCR"], "key_attributes": ["ticket_number", "created_date", "priority", "category", "status", "assigned_to", "resolution_time", "first_contact_resolved"], "related_objects": ["Account", "Appointment", "Assessment", "Channel Partner", "Customer", "Deal", "Lead", "Meeting", "Opportunity", "Product", "Proposal", "Sale", "Sales Quota", "Sales Representative", "Sales Team"]},
}
