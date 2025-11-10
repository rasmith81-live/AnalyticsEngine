"""
Lead Qualification Object Model

Represents the lead qualification process and results.
"""

from analytics_models import ObjectModel

LEAD_QUALIFICATION = ObjectModel(
    name="Lead Qualification",
    code="LEAD_QUALIFICATION",
    description="Lead qualification process and sales-readiness assessment",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class LeadQualification {
}

class Lead {
}

class SalesRepresentative {
}

class Opportunity {
}

class ProspectEngagement {
}

' Relationships
Lead "1" -- "0..1" LeadQualification : undergoes >
SalesRepresentative "1" -- "0..*" LeadQualification : performs >
LeadQualification "1" -- "0..1" Opportunity : creates (if SQL) >
ProspectEngagement "1" -- "0..1" LeadQualification : influences >

@enduml

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
""",
    
    is_active=True,
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
