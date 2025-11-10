"""
Partner Portal Object Model

Represents the partner portal platform and usage metrics.
"""

from analytics_models import ObjectModel

PARTNER_PORTAL = ObjectModel(
    name="Partner Portal",
    code="PARTNER_PORTAL",
    description="Partner portal platform for resources and collaboration",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "partner_portal",
        "class_name": "Partner Portal",
        "columns": [
            {
                "name": "portal_id",
                "type": "Integer",
                "index": True
            },
            {
                "name": "total_users",
                "type": "String",
                "length": 255
            },
            {
                "name": "active_users",
                "type": "String",
                "length": 255
            },
            {
                "name": "login_frequency",
                "type": "String",
                "length": 255
            },
            {
                "name": "resources_accessed",
                "type": "String",
                "length": 255
            },
            {
                "name": "features_used",
                "type": "String",
                "length": 255
            },
            {
                "name": "utilization_rate",
                "type": "Float"
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
                "name": "ix_partner_portal_portal_id",
                "columns": ["portal_id"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
' Relationships
PartnerPortal "1" -- "0..*" ChannelPartner : used by >
ChannelPartner "1" -- "0..*" PortalUsage : has >
PartnerPortal "1" -- "0..*" Resource : contains >
PortalUsage "0..*" -- "0..*" Resource : accesses >
' Relationships to Related Objects
PartnerPortal "1" -- "*" Account : relates to
PartnerPortal "1" -- "*" AccountPenetration : relates to
PartnerPortal "1" -- "*" AccountPlan : relates to
PartnerPortal "1" -- "*" AccountRisk : relates to
PartnerPortal "1" -- "*" Assessment : relates to
PartnerPortal "1" -- "*" ChannelConflict : relates to
PartnerPortal "1" -- "*" ChannelDeal : relates to
PartnerPortal "1" -- "*" ChannelMarket : relates to
PartnerPortal "1" -- "*" ChannelPartner : relates to
PartnerPortal "1" -- "*" ChurnEvent : relates to
PartnerPortal "1" -- "*" Co-marketingCampaign : relates to
PartnerPortal "1" -- "*" CompetitiveAnalysis : relates to
PartnerPortal "1" -- "*" Contract : relates to
PartnerPortal "1" -- "*" Customer : relates to
PartnerPortal "1" -- "*" CustomerAdvocacyProgram : relates to
PartnerPortal "1" -- "*" CustomerCohort : relates to
PartnerPortal "1" -- "*" CustomerCommunity : relates to
PartnerPortal "1" -- "*" CustomerEducation : relates to
PartnerPortal "1" -- "*" CustomerFeedback : relates to
PartnerPortal "1" -- "*" CustomerGoal : relates to
@enduml
    """,

    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
        "related_kpis": [
            "PARTNER_PORTAL_UTILIZATION_RATE"
        ],
        "key_attributes": [
            "portal_id",
            "total_users",
            "active_users",
            "login_frequency",
            "resources_accessed",
            "features_used",
            "utilization_rate"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}

)
