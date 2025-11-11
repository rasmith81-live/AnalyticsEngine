"""
Return Order Rate

The percentage of orders that are returned by customers.
"""

RETURN_ORDER_RATE = {
    "code": "RETURN_ORDER_RATE",
    "name": "Return Order Rate",
    "description": "The percentage of orders that are returned by customers.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Return Order Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Customer", "Order", "Return"], "last_validated": "2025-11-10T13:49:33.351613"},
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
                        57.44,
                        48.56,
                        45.0,
                        51.81,
                        58.88,
                        46.77,
                        49.03,
                        58.48,
                        58.83,
                        51.52,
                        46.37,
                        42.36
                ],
                "unit": "%"
        },
        "current": {
                "value": 42.36,
                "unit": "%",
                "change": -4.01,
                "change_percent": -8.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 51.25,
                "min": 42.36,
                "max": 58.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.92,
                        "percentage": 21.1
                },
                {
                        "category": "Category B",
                        "value": 7.88,
                        "percentage": 18.6
                },
                {
                        "category": "Category C",
                        "value": 8.82,
                        "percentage": 20.8
                },
                {
                        "category": "Category D",
                        "value": 2.89,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 13.85,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.097681",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Return Order Rate"
        }
    },
}
