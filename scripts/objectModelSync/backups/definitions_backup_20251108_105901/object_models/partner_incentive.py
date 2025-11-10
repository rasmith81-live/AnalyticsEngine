"""
Partner Incentive Object Model

Represents incentive programs and claims for channel partners.
"""

from analytics_models import ObjectModel

PARTNER_INCENTIVE = ObjectModel(
    name="Partner Incentive",
    code="PARTNER_INCENTIVE",
    description="Incentive programs for channel partner motivation",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class PartnerIncentive {
}

class ChannelPartner {
}

class IncentiveClaim {
}

' Relationships
PartnerIncentive "0..*" -- "0..*" ChannelPartner : available to >
PartnerIncentive "1" -- "0..*" IncentiveClaim : has >
IncentiveClaim "1" -- "1" ChannelPartner : claimed by >

@enduml

' Relationships to Related Objects
PartnerIncentive "1" -- "*" Account : relates to
PartnerIncentive "1" -- "*" AccountPenetration : relates to
PartnerIncentive "1" -- "*" AccountPlan : relates to
PartnerIncentive "1" -- "*" AccountRisk : relates to
PartnerIncentive "1" -- "*" Assessment : relates to
PartnerIncentive "1" -- "*" ChannelConflict : relates to
PartnerIncentive "1" -- "*" ChannelDeal : relates to
PartnerIncentive "1" -- "*" ChannelMarket : relates to
PartnerIncentive "1" -- "*" ChannelPartner : relates to
PartnerIncentive "1" -- "*" ChurnEvent : relates to
PartnerIncentive "1" -- "*" Co-marketingCampaign : relates to
PartnerIncentive "1" -- "*" CompetitiveAnalysis : relates to
PartnerIncentive "1" -- "*" Contract : relates to
PartnerIncentive "1" -- "*" Customer : relates to
PartnerIncentive "1" -- "*" CustomerAdvocacyProgram : relates to
PartnerIncentive "1" -- "*" CustomerCohort : relates to
PartnerIncentive "1" -- "*" CustomerCommunity : relates to
PartnerIncentive "1" -- "*" CustomerEducation : relates to
PartnerIncentive "1" -- "*" CustomerFeedback : relates to
PartnerIncentive "1" -- "*" CustomerGoal : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
        "related_kpis": [
            "PARTNER_INCENTIVE_UTILIZATION_RATE"
        ],
        "key_attributes": [
            "incentive_id",
            "incentive_name",
            "incentive_type",
            "value",
            "eligibility_criteria",
            "total_offered",
            "total_claimed",
            "utilization_rate"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}
)
