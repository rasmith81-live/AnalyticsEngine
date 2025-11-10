"""
Revenue Forecast Object Model

Represents projected revenue and forecasting data.
"""

REVENUE_FORECAST = {
    "code": "REVENUE_FORECAST",
    "name": "Revenue Forecast",
    "description": "Projected revenue forecasts and predictions",
    "table_schema": {"table_name": "revenue_forecast", "class_name": "Revenue Forecast", "columns": [{"name": "forecast_amount", "type": "Float"}, {"name": "forecast_date", "type": "DateTime", "index": True}, {"name": "period", "type": "String", "length": 255}, {"name": "actual_amount", "type": "Float"}, {"name": "variance", "type": "String", "length": 255}, {"name": "accuracy_percentage", "type": "Float"}, {"name": "confidence_level", "type": "String", "length": 50, "index": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_revenue_forecast_forecast_date", "columns": ["forecast_date"]}, {"name": "ix_revenue_forecast_confidence_level", "columns": ["confidence_level"]}]},
    "schema_definition": """
    @startuml
' Relationships
RevenueForecast "0..*" -- "1..*" Opportunity : based on >
SalesTeam "1" -- "0..*" RevenueForecast : creates >
RevenueForecast "0..*" -- "1" Period : for >
RevenueForecast "1" -- "0..1" ActualRevenue : compared to >
' Related Objects
' Relationships to Related Objects
RevenueForecast "1" -- "*" Customer : relates to
RevenueForecast "1" -- "*" Sale : relates to
RevenueForecast "1" -- "*" SalesTeam : relates to
@enduml
    """,
    "metadata_": {"modules": ["BUS_DEV"], "related_kpis": ["REVENUE_FORECAST_ACCURACY"], "key_attributes": ["forecast_amount", "forecast_date", "period", "actual_amount", "variance", "accuracy_percentage", "confidence_level"], "related_objects": ["Customer", "Sale", "Sales Team"]},
}
