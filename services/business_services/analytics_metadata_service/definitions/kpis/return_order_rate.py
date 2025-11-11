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
                        74.94,
                        76.96,
                        80.58,
                        80.58,
                        78.76,
                        70.05,
                        78.13,
                        70.29,
                        79.48,
                        86.17,
                        68.46,
                        68.91
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.91,
                "unit": "%",
                "change": 0.45,
                "change_percent": 0.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 76.11,
                "min": 68.46,
                "max": 86.17,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.73,
                        "percentage": 19.9
                },
                {
                        "category": "Segment B",
                        "value": 11.13,
                        "percentage": 16.2
                },
                {
                        "category": "Segment C",
                        "value": 6.98,
                        "percentage": 10.1
                },
                {
                        "category": "Segment D",
                        "value": 8.84,
                        "percentage": 12.8
                },
                {
                        "category": "Other",
                        "value": 28.23,
                        "percentage": 41.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.821230",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Return Order Rate"
        }
    },
}
