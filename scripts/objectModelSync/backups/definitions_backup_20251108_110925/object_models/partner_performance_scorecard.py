"""
Partner Performance Scorecard Object Model

Represents performance evaluations and scorecards for channel partners.
"""

from analytics_models import ObjectModel

PARTNER_PERFORMANCE_SCORECARD = ObjectModel(
    name="Partner Performance Scorecard",
    code="PARTNER_PERFORMANCE_SCORECARD",
    description="Performance evaluation scorecards for channel partners",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class PartnerPerformanceScorecard {
}

class ChannelPartner {
}

class PerformanceMetric {
}

' Relationships
ChannelPartner "1" -- "0..*" PartnerPerformanceScorecard : evaluated by >
PartnerPerformanceScorecard "1" -- "1..*" PerformanceMetric : includes >

@enduml

' Relationships to Related Objects
PartnerPerformanceScorecard "1" -- "*" Account : relates to
PartnerPerformanceScorecard "1" -- "*" AccountPenetration : relates to
PartnerPerformanceScorecard "1" -- "*" AccountPlan : relates to
PartnerPerformanceScorecard "1" -- "*" AccountRisk : relates to
PartnerPerformanceScorecard "1" -- "*" Assessment : relates to
PartnerPerformanceScorecard "1" -- "*" Call : relates to
PartnerPerformanceScorecard "1" -- "*" ChannelConflict : relates to
PartnerPerformanceScorecard "1" -- "*" ChannelDeal : relates to
PartnerPerformanceScorecard "1" -- "*" ChannelMarket : relates to
PartnerPerformanceScorecard "1" -- "*" ChannelPartner : relates to
PartnerPerformanceScorecard "1" -- "*" ChurnEvent : relates to
PartnerPerformanceScorecard "1" -- "*" Co-marketingCampaign : relates to
PartnerPerformanceScorecard "1" -- "*" CoachingSession : relates to
PartnerPerformanceScorecard "1" -- "*" CompetitiveAnalysis : relates to
PartnerPerformanceScorecard "1" -- "*" Contract : relates to
PartnerPerformanceScorecard "1" -- "*" Customer : relates to
PartnerPerformanceScorecard "1" -- "*" CustomerAdvocacyProgram : relates to
PartnerPerformanceScorecard "1" -- "*" CustomerCohort : relates to
PartnerPerformanceScorecard "1" -- "*" CustomerCommunity : relates to
PartnerPerformanceScorecard "1" -- "*" CustomerEducation : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "CHANNEL_PARTNER_PERFORMANCE_SCORECARD",
            "PARTNER_QUARTERLY_PERFORMANCE_TREND",
            "PARTNER_ECOSYSTEM_HEALTH"
        ],
        "key_attributes": [
            "scorecard_id",
            "partner_id",
            "period",
            "sales_score",
            "growth_score",
            "satisfaction_score",
            "compliance_score",
            "overall_score",
            "ranking"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education"]}
)
