"""
Outbound Call Object Model

Represents outbound sales calls made by SDRs/BDRs during prospecting.
"""

from analytics_models import ObjectModel

OUTBOUND_CALL = ObjectModel(
    name="Outbound Call",
    code="OUTBOUND_CALL",
    description="Outbound sales calls made during prospecting and lead qualification",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "outbound_call",
        "class_name": "Outbound Call",
        "columns": [
            {
                "name": "call_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "sdr_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "prospect_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "date",
                "type": "String",
                "length": 255
            },
            {
                "name": "duration",
                "type": "String",
                "length": 255
            },
            {
                "name": "outcome",
                "type": "String",
                "length": 255
            },
            {
                "name": "disposition",
                "type": "String",
                "length": 255
            },
            {
                "name": "follow_up_required",
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
                "name": "ix_outbound_call_call_id",
                "columns": ["call_id"]
            },
            {
                "name": "ix_outbound_call_sdr_id",
                "columns": ["sdr_id"]
            },
            {
                "name": "ix_outbound_call_prospect_id",
                "columns": ["prospect_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
SalesRepresentative "1" -- "0..*" OutboundCall : makes >
OutboundCall "0..*" -- "0..1" Prospect : to >
OutboundCall "0..*" -- "0..1" Lead : to >
OutboundCall "1" -- "0..1" Appointment : may result in >
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
@enduml
    """,

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
