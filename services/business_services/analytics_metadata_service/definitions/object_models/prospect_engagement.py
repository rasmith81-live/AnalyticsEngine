"""
Prospect Engagement Object Model

Represents engagement tracking and scoring for active prospects.
"""

from analytics_models import ObjectModel

PROSPECT_ENGAGEMENT = ObjectModel(
    name="Prospect Engagement",
    code="PROSPECT_ENGAGEMENT",
    description="Engagement tracking and scoring for prospects",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "prospect_engagement",
        "class_name": "Prospect Engagement",
        "columns": [
            {
                "name": "engagement_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "prospect_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "engagement_score",
                "type": "Float"
            },
            {
                "name": "last_contact_date",
                "type": "DateTime",
                "index": True
            },
            {
                "name": "touchpoints",
                "type": "String",
                "length": 255
            },
            {
                "name": "response_count",
                "type": "Integer"
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
                "name": "ix_prospect_engagement_engagement_id",
                "columns": ["engagement_id"]
            },
            {
                "name": "ix_prospect_engagement_prospect_id",
                "columns": ["prospect_id"]
            },
            {
                "name": "ix_prospect_engagement_last_contact_date",
                "columns": ["last_contact_date"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
Prospect "1" -- "1" ProspectEngagement : has >
SalesRepresentative "1" -- "0..*" ProspectEngagement : tracks >
ProspectEngagement "1" -- "0..1" LeadQualification : influences >
' Relationships to Related Objects
ProspectEngagement "1" -- "*" Account : relates to
ProspectEngagement "1" -- "*" AccountPenetration : relates to
ProspectEngagement "1" -- "*" AccountPlan : relates to
ProspectEngagement "1" -- "*" AccountRisk : relates to
ProspectEngagement "1" -- "*" Call : relates to
ProspectEngagement "1" -- "*" ChannelConflict : relates to
ProspectEngagement "1" -- "*" ChannelDeal : relates to
ProspectEngagement "1" -- "*" ChannelMarket : relates to
ProspectEngagement "1" -- "*" ChannelPartner : relates to
ProspectEngagement "1" -- "*" CompetitiveAnalysis : relates to
ProspectEngagement "1" -- "*" Customer : relates to
ProspectEngagement "1" -- "*" CustomerAdvocacyProgram : relates to
ProspectEngagement "1" -- "*" CustomerCohort : relates to
ProspectEngagement "1" -- "*" CustomerCommunity : relates to
ProspectEngagement "1" -- "*" CustomerEducation : relates to
ProspectEngagement "1" -- "*" CustomerFeedback : relates to
ProspectEngagement "1" -- "*" CustomerGoal : relates to
ProspectEngagement "1" -- "*" CustomerHealthRecord : relates to
ProspectEngagement "1" -- "*" CustomerJourney : relates to
ProspectEngagement "1" -- "*" CustomerOnboarding : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "PROSPECT_ENGAGEMENT_SCORE",
            "NUMBER_OF_ACTIVE_PROSPECTS",
            "RESPONSE_RATE"
        ],
        "key_attributes": [
            "engagement_id",
            "prospect_id",
            "engagement_score",
            "last_contact_date",
            "touchpoints",
            "response_count"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding"]}

)
