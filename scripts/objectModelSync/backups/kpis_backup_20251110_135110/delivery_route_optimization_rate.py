"""
Delivery Route Optimization Rate

The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.
"""

DELIVERY_ROUTE_OPTIMIZATION_RATE = {
    "code": "DELIVERY_ROUTE_OPTIMIZATION_RATE",
    "name": "Delivery Route Optimization Rate",
    "description": "The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Delivery Route Optimization Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:49:32.919415"},
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
                        74.83,
                        76.84,
                        79.71,
                        78.85,
                        66.83,
                        74.71,
                        74.04,
                        79.01,
                        69.71,
                        70.22,
                        66.85,
                        77.53
                ],
                "unit": "%"
        },
        "current": {
                "value": 77.53,
                "unit": "%",
                "change": 10.68,
                "change_percent": 16.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 74.09,
                "min": 66.83,
                "max": 79.71,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.0,
                        "percentage": 29.7
                },
                {
                        "category": "Category B",
                        "value": 14.91,
                        "percentage": 19.2
                },
                {
                        "category": "Category C",
                        "value": 12.37,
                        "percentage": 16.0
                },
                {
                        "category": "Category D",
                        "value": 7.05,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 20.2,
                        "percentage": 26.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.426921",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Delivery Route Optimization Rate"
        }
    },
}
