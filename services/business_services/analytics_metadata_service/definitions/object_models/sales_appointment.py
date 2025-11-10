"""
Sales Appointment Object Model

Represents scheduled sales appointments and meetings.
"""

from analytics_models import ObjectModel

SALES_APPOINTMENT = ObjectModel(
    name="Sales Appointment",
    code="SALES_APPOINTMENT",
    description="Scheduled sales appointments and meetings",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "sales_appointment",
        "class_name": "Sales Appointment",
        "columns": [
            {
                "name": "appointment_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "rep_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "account_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "scheduled_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "appointment_type",
                "type": "String",
                "length": 50,
                "index": True
            },
            {
                "name": "status",
                "type": "String",
                "length": 255
            },
            {
                "name": "outcome",
                "type": "String",
                "length": 255
            },
            {
                "name": "conversion_flag",
                "type": "String",
                "length": 255
            },
            {
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            },
            {
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            }
        ],
        "indexes": [
            {
                "name": "ix_sales_appointment_appointment_id",
                "columns": ["appointment_id"]
            },
            {
                "name": "ix_sales_appointment_rep_id",
                "columns": ["rep_id"]
            },
            {
                "name": "ix_sales_appointment_account_id",
                "columns": ["account_id"]
            },
            {
                "name": "ix_sales_appointment_scheduled_date",
                "columns": ["scheduled_date"]
            },
            {
                "name": "ix_sales_appointment_appointment_type",
                "columns": ["appointment_type"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" SalesAppointment : schedules >
SalesAppointment "0..*" -- "1" Account : with >
SalesAppointment "1" -- "0..1" Demo : may lead to >
SalesAppointment "1" -- "0..1" Opportunity : may convert to >
' Relationships to Related Objects
SalesAppointment "1" -- "*" Account : relates to
SalesAppointment "1" -- "*" AccountPenetration : relates to
SalesAppointment "1" -- "*" AccountPlan : relates to
SalesAppointment "1" -- "*" AccountRisk : relates to
SalesAppointment "1" -- "*" Appointment : relates to
SalesAppointment "1" -- "*" Assessment : relates to
SalesAppointment "1" -- "*" Call : relates to
SalesAppointment "1" -- "*" Certification : relates to
SalesAppointment "1" -- "*" ChannelConflict : relates to
SalesAppointment "1" -- "*" ChannelDeal : relates to
SalesAppointment "1" -- "*" ChannelMarket : relates to
SalesAppointment "1" -- "*" ChannelPartner : relates to
SalesAppointment "1" -- "*" ChurnEvent : relates to
SalesAppointment "1" -- "*" Co-marketingCampaign : relates to
SalesAppointment "1" -- "*" CoachingSession : relates to
SalesAppointment "1" -- "*" CompetitiveAnalysis : relates to
SalesAppointment "1" -- "*" Contract : relates to
SalesAppointment "1" -- "*" Customer : relates to
SalesAppointment "1" -- "*" CustomerAdvocacyProgram : relates to
SalesAppointment "1" -- "*" CustomerCohort : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "APPOINTMENT_TO_DEMO_RATIO",
            "SALES_CALL_TO_APPOINTMENT_RATIO",
            "MEETING_CONVERSION_RATE"
        ],
        "key_attributes": [
            "appointment_id",
            "rep_id",
            "account_id",
            "scheduled_date",
            "appointment_type",
            "status",
            "outcome",
            "conversion_flag"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}

)
