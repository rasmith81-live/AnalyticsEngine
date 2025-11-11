"""
Back Order Rate

The percentage of orders that cannot be filled at the time of customer order.
"""

BACK_ORDER_RATE = {
    "code": "BACK_ORDER_RATE",
    "name": "Back Order Rate",
    "description": "The percentage of orders that cannot be filled at the time of customer order.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Back Order Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Customer", "Order", "Product"], "last_validated": "2025-11-10T13:49:32.663471"},
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
                        59.28,
                        54.69,
                        60.69,
                        66.0,
                        69.82,
                        64.01,
                        57.06,
                        64.91,
                        55.43,
                        65.69,
                        66.3,
                        69.02
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.02,
                "unit": "%",
                "change": 2.72,
                "change_percent": 4.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 62.74,
                "min": 54.69,
                "max": 69.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.25,
                        "percentage": 16.3
                },
                {
                        "category": "Category B",
                        "value": 19.04,
                        "percentage": 27.6
                },
                {
                        "category": "Category C",
                        "value": 11.55,
                        "percentage": 16.7
                },
                {
                        "category": "Category D",
                        "value": 7.83,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 19.35,
                        "percentage": 28.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.051623",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Back Order Rate"
        }
    },
}
