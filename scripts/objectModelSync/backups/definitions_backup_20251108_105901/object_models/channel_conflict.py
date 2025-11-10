"""
Channel Conflict Object Model

Represents conflicts between channel partners or with direct sales.
"""

from analytics_models import ObjectModel

CHANNEL_CONFLICT = ObjectModel(
    name="Channel Conflict",
    code="CHANNEL_CONFLICT",
    description="Conflicts in the channel ecosystem",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class ChannelConflict {
}

class ChannelPartner {
}

class ChannelDeal {
}

class Resolution {
}

' Relationships
ChannelConflict "0..*" -- "1..*" ChannelPartner : involves >
ChannelConflict "1" -- "1" ChannelDeal : related to >
ChannelConflict "1" -- "0..1" Resolution : has >

@enduml

' Relationships to Related Objects
ChannelConflict "1" -- "*" Account : relates to
ChannelConflict "1" -- "*" AccountPenetration : relates to
ChannelConflict "1" -- "*" AccountPlan : relates to
ChannelConflict "1" -- "*" AccountRisk : relates to
ChannelConflict "1" -- "*" Assessment : relates to
ChannelConflict "1" -- "*" ChannelDeal : relates to
ChannelConflict "1" -- "*" ChannelMarket : relates to
ChannelConflict "1" -- "*" ChannelPartner : relates to
ChannelConflict "1" -- "*" ChurnEvent : relates to
ChannelConflict "1" -- "*" Co-marketingCampaign : relates to
ChannelConflict "1" -- "*" CompetitiveAnalysis : relates to
ChannelConflict "1" -- "*" Contract : relates to
ChannelConflict "1" -- "*" Customer : relates to
ChannelConflict "1" -- "*" CustomerAdvocacyProgram : relates to
ChannelConflict "1" -- "*" CustomerCohort : relates to
ChannelConflict "1" -- "*" CustomerCommunity : relates to
ChannelConflict "1" -- "*" CustomerEducation : relates to
ChannelConflict "1" -- "*" CustomerFeedback : relates to
ChannelConflict "1" -- "*" CustomerGoal : relates to
ChannelConflict "1" -- "*" CustomerHealthRecord : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "related_kpis": [
            "CHANNEL_CONFLICT_RATE"
        ],
        "key_attributes": [
            "conflict_id",
            "conflict_type",
            "parties_involved",
            "deal_id",
            "reported_date",
            "resolution_date",
            "resolution_outcome",
            "status"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Assessment", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record"]}
)
