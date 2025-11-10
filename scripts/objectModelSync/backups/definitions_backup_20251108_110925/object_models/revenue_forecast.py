"""
Revenue Forecast Object Model

Represents projected revenue and forecasting data.
"""

from analytics_models import ObjectModel

REVENUE_FORECAST = ObjectModel(
    name="Revenue Forecast",
    code="REVENUE_FORECAST",
    description="Projected revenue forecasts and predictions",
    
    # UML Class Diagram - Entity Level Only
    schema_definition="""
@startuml
class RevenueForecast {
}

class Opportunity {
}

class SalesTeam {
}

class Period {
}

class ActualRevenue {
}

' Relationships
RevenueForecast "0..*" -- "1..*" Opportunity : based on >
SalesTeam "1" -- "0..*" RevenueForecast : creates >
RevenueForecast "0..*" -- "1" Period : for >
RevenueForecast "1" -- "0..1" ActualRevenue : compared to >

@enduml

' Related Objects

class Customer {
}

' Relationships to Related Objects
RevenueForecast "1" -- "*" Customer : relates to
RevenueForecast "1" -- "*" Sale : relates to
RevenueForecast "1" -- "*" SalesTeam : relates to
""",
    
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "related_kpis": [
            "REVENUE_FORECAST_ACCURACY"
        ],
        "key_attributes": [
            "forecast_amount",
            "forecast_date",
            "period",
            "actual_amount",
            "variance",
            "accuracy_percentage",
            "confidence_level"
        ],
        "related_objects": ["Customer", "Sale", "Sales Team"]}
)
