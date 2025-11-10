"""
Sales Process Workflow Object Model

Represents standardized sales process workflows.
"""

from analytics_models import ObjectModel

SALES_PROCESS_WORKFLOW = ObjectModel(
    name="Sales Process Workflow",
    code="SALES_PROCESS_WORKFLOW",
    description="Standardized sales process workflows and stages",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesProcessWorkflow {
}

class SalesOperationsTeam {
}

class SalesTeam {
}

class Stage {
}

class CRMSystem {
}

' Relationships
SalesOperationsTeam "1" -- "0..*" SalesProcessWorkflow : defines >
SalesTeam "0..*" -- "1" SalesProcessWorkflow : follows >
SalesProcessWorkflow "1" -- "1..*" Stage : has >
SalesProcessWorkflow "0..*" -- "1" CRMSystem : integrated with >

@enduml

' Relationships to Related Objects
SalesProcessWorkflow "1" -- "*" Account : relates to
SalesProcessWorkflow "1" -- "*" AccountPenetration : relates to
SalesProcessWorkflow "1" -- "*" AccountPlan : relates to
SalesProcessWorkflow "1" -- "*" AccountRisk : relates to
SalesProcessWorkflow "1" -- "*" Appointment : relates to
SalesProcessWorkflow "1" -- "*" Assessment : relates to
SalesProcessWorkflow "1" -- "*" Call : relates to
SalesProcessWorkflow "1" -- "*" Certification : relates to
SalesProcessWorkflow "1" -- "*" ChannelConflict : relates to
SalesProcessWorkflow "1" -- "*" ChannelDeal : relates to
SalesProcessWorkflow "1" -- "*" ChannelMarket : relates to
SalesProcessWorkflow "1" -- "*" ChannelPartner : relates to
SalesProcessWorkflow "1" -- "*" Co-marketingCampaign : relates to
SalesProcessWorkflow "1" -- "*" CoachingSession : relates to
SalesProcessWorkflow "1" -- "*" CompetitiveAnalysis : relates to
SalesProcessWorkflow "1" -- "*" Contract : relates to
SalesProcessWorkflow "1" -- "*" Customer : relates to
SalesProcessWorkflow "1" -- "*" CustomerAdvocacyProgram : relates to
SalesProcessWorkflow "1" -- "*" CustomerCohort : relates to
SalesProcessWorkflow "1" -- "*" CustomerCommunity : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_PROCESS_ADHERENCE_RATE",
            "SALES_CYCLE_LENGTH",
            "SALES_OPERATIONAL_EFFICIENCY"
        ],
        "key_attributes": [
            "workflow_id",
            "name",
            "stages",
            "adherence_rate",
            "cycle_time",
            "efficiency_score"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community"]}
)
