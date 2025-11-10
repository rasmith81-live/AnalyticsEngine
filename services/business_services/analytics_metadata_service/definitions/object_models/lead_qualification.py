"""
Lead Qualification Object Model

Represents the lead qualification process and results.
"""

from analytics_models import ObjectModel

LEAD_QUALIFICATION = ObjectModel(
    name="Lead Qualification",
    code="LEAD_QUALIFICATION",
    description="Lead qualification process and sales-readiness assessment",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "lead_qualification",
        "class_name": "Lead Qualification",
        "columns": [
            {
                "name": "qualification_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "lead_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "sdr_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "qualification_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "score",
                "type": "String",
                "length": 255
            },
            {
                "name": "criteria_met",
                "type": "String",
                "length": 255
            },
            {
                "name": "sql_flag",
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
                "name": "ix_lead_qualification_qualification_id",
                "columns": ["qualification_id"]
            },
            {
                "name": "ix_lead_qualification_lead_id",
                "columns": ["lead_id"]
            },
            {
                "name": "ix_lead_qualification_sdr_id",
                "columns": ["sdr_id"]
            },
            {
                "name": "ix_lead_qualification_qualification_date",
                "columns": ["qualification_date"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Lead "1" -- "0..1" LeadQualification : undergoes >
SalesRepresentative "1" -- "0..*" LeadQualification : performs >
LeadQualification "1" -- "0..1" Opportunity : creates (if SQL) >
ProspectEngagement "1" -- "0..1" LeadQualification : influences >
' Relationships to Related Objects
LeadQualification "1" -- "*" Account : relates to
LeadQualification "1" -- "*" AccountPenetration : relates to
LeadQualification "1" -- "*" AccountPlan : relates to
LeadQualification "1" -- "*" AccountRisk : relates to
LeadQualification "1" -- "*" Appointment : relates to
LeadQualification "1" -- "*" Call : relates to
LeadQualification "1" -- "*" ChannelConflict : relates to
LeadQualification "1" -- "*" ChannelDeal : relates to
LeadQualification "1" -- "*" ChannelMarket : relates to
LeadQualification "1" -- "*" ChannelPartner : relates to
LeadQualification "1" -- "*" CompetitiveAnalysis : relates to
LeadQualification "1" -- "*" Deal : relates to
LeadQualification "1" -- "*" Demo : relates to
LeadQualification "1" -- "*" ExpansionOpportunity : manages
LeadQualification "1" -- "*" KeyAccount : relates to
LeadQualification "1" -- "*" KeyAccountManager : relates to
LeadQualification "1" -- "*" KnowledgeBase : relates to
LeadQualification "1" -- "*" Lead : relates to
LeadQualification "1" -- "*" LostSale : relates to
LeadQualification "1" -- "*" MarketSegment : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "LEAD_QUALIFICATION_ACCURACY",
            "SALES_QUALIFIED_LEAD_SQL_CONVERSION_RATE",
            "LEAD_TO_OPPORTUNITY_RATIO"
        ],
        "key_attributes": [
            "qualification_id",
            "lead_id",
            "sdr_id",
            "qualification_date",
            "score",
            "criteria_met",
            "sql_flag"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Deal", "Demo", "Expansion Opportunity", "Key Account", "Key Account Manager", "Knowledge Base", "Lead", "Lost Sale", "Market Segment"]}

)
