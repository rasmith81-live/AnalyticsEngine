"""
Sales Forecast Object Model

Represents sales forecasts and accuracy tracking.
"""

from analytics_models import ObjectModel

SALES_FORECAST = ObjectModel(
    name="Sales Forecast",
    code="SALES_FORECAST",
    description="Sales forecasts and accuracy tracking",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class SalesForecast {
}

class SalesRepresentative {
}

class SalesTeam {
}

class Opportunity {
}

class ActualRevenue {
}

' Sales Operations Specific
class SalesOperationsTeam {
}

class Pipeline {
}

class SalesLeadership {
}

' Relationships - Core
SalesRepresentative "1" -- "0..*" SalesForecast : creates >
SalesTeam "1" -- "0..*" SalesForecast : creates >
SalesForecast "1" -- "0..*" Opportunity : based on >
SalesForecast "1" -- "0..1" ActualRevenue : compared to >

' Relationships - Sales Operations
SalesOperationsTeam "1" -- "0..*" SalesForecast : generates >
SalesForecast "1" -- "1" Pipeline : based on >
SalesLeadership "0..*" -- "0..*" SalesForecast : reviews >

@enduml

' Relationships to Related Objects
SalesForecast "1" -- "*" Account : relates to
SalesForecast "1" -- "*" AccountPenetration : relates to
SalesForecast "1" -- "*" AccountPlan : relates to
SalesForecast "1" -- "*" AccountRisk : relates to
SalesForecast "1" -- "*" Appointment : relates to
SalesForecast "1" -- "*" Assessment : relates to
SalesForecast "1" -- "*" Call : relates to
SalesForecast "1" -- "*" Certification : relates to
SalesForecast "1" -- "*" ChannelConflict : relates to
SalesForecast "1" -- "*" ChannelDeal : relates to
SalesForecast "1" -- "*" ChannelMarket : relates to
SalesForecast "1" -- "*" ChannelPartner : relates to
SalesForecast "1" -- "*" ChurnEvent : relates to
SalesForecast "1" -- "*" Co-marketingCampaign : relates to
SalesForecast "1" -- "*" CoachingSession : relates to
SalesForecast "1" -- "*" CompetitiveAnalysis : relates to
SalesForecast "1" -- "*" Contract : relates to
SalesForecast "1" -- "*" Customer : relates to
SalesForecast "1" -- "*" CustomerAdvocacyProgram : relates to
SalesForecast "1" -- "*" CustomerCohort : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "CHANNEL_SALES", "CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "related_kpis": [
            "SALES_FORECAST_ACCURACY"
        ],
        "key_attributes": [
            "forecast_id",
            "period",
            "forecasted_revenue",
            "actual_revenue",
            "accuracy_percentage",
            "rep_id",
            "team_id",
            "forecast_date"
        ],
        "related_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Appointment", "Assessment", "Call", "Certification", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Churn Event", "Co-Marketing Campaign", "Coaching Session", "Competitive Analysis", "Contract", "Customer", "Customer Advocacy Program", "Customer Cohort"]}
)
