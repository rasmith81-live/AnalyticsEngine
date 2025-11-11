"""
Pickup and Delivery Productivity

The number of pickups and deliveries made in a given period relative to the resource used.
"""

PICKUP_AND_DELIVERY_PRODUCTIVITY = {
    "code": "PICKUP_AND_DELIVERY_PRODUCTIVITY",
    "name": "Pickup and Delivery Productivity",
    "description": "The number of pickups and deliveries made in a given period relative to the resource used.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pickup and Delivery Productivity to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """


* What factors are influencing this metric?
* Are there any anomalies in the data?
    
    
    """,
    "actionable_tips": """


* Monitor this KPI regularly
* Set appropriate targets and thresholds
    
    
    """,
    "visualization_suggestions": """


* Line chart for time series analysis
* Bar chart for comparisons
    
    
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Product"], "last_validated": "2025-11-10T13:49:33.237999"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        177.63,
                        106.63,
                        86.14,
                        192.39,
                        84.84,
                        85.46,
                        70.95,
                        105.14,
                        173.17,
                        126.97,
                        197.12,
                        104.08
                ],
                "unit": "units"
        },
        "current": {
                "value": 104.08,
                "unit": "units",
                "change": -93.04,
                "change_percent": -47.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 125.88,
                "min": 70.95,
                "max": 197.12,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 36.39,
                        "percentage": 35.0
                },
                {
                        "category": "Product Line B",
                        "value": 12.7,
                        "percentage": 12.2
                },
                {
                        "category": "Product Line C",
                        "value": 8.55,
                        "percentage": 8.2
                },
                {
                        "category": "Services",
                        "value": 8.72,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 37.72,
                        "percentage": 36.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.567155",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Pickup and Delivery Productivity"
        }
    },
}
