"""
Lost Sale Object Model

Represents lost sales opportunities and analysis.
"""

from analytics_models import ObjectModel

LOST_SALE = ObjectModel(
    name="Lost Sale",
    code="LOST_SALE",
    description="Lost sales opportunities and competitive analysis",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class LostSale {
}

class Opportunity {
}

class Competitor {
}

class LossReason {
}

' Relationships
Opportunity "1" -- "0..1" LostSale : may result in >
LostSale "0..*" -- "0..1" Competitor : lost to >
LostSale "1" -- "1..*" LossReason : has >

@enduml

' Relationships to Related Objects
LostSale "1" -- "*" Account : relates to
LostSale "1" -- "*" AccountPenetration : relates to
LostSale "1" -- "*" AccountPlan : relates to
LostSale "1" -- "*" AccountRisk : relates to
LostSale "1" -- "*" Appointment : relates to
LostSale "1" -- "*" Assessment : relates to
LostSale "1" -- "*" Call : relates to
LostSale "1" -- "*" ChannelConflict : relates to
LostSale "1" -- "*" ChannelDeal : relates to
LostSale "1" -- "*" ChannelMarket : relates to
LostSale "1" -- "*" ChannelPartner : relates to
LostSale "1" -- "*" ChurnEvent : relates to
LostSale "1" -- "*" CompetitiveAnalysis : relates to
LostSale "1" -- "*" Customer : relates to
LostSale "1" -- "*" CustomerAdvocacyProgram : relates to
LostSale "1" -- "*" CustomerCohort : relates to
LostSale "1" -- "*" CustomerCommunity : relates to
LostSale "1" -- "*" CustomerEducation : relates to
LostSale "1" -- "*" CustomerFeedback : relates to
LostSale "1" -- "*" CustomerGoal : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "LOST_SALE_ANALYSIS"
        ],
        "key_attributes": [
            "lost_sale_id",
            "opportunity_id",
            "loss_date",
            "reason",
            "competitor",
            "value_lost",
            "stage_lost",
            "lessons_learned"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal"]}
)
