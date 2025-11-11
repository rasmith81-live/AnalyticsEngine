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
                        49.44,
                        43.17,
                        48.91,
                        43.95,
                        52.99,
                        37.77,
                        49.05,
                        44.37,
                        38.13,
                        53.34,
                        38.83,
                        50.1
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.1,
                "unit": "%",
                "change": 11.27,
                "change_percent": 29.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 45.84,
                "min": 37.77,
                "max": 53.34,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.81,
                        "percentage": 29.6
                },
                {
                        "category": "Segment B",
                        "value": 6.29,
                        "percentage": 12.6
                },
                {
                        "category": "Segment C",
                        "value": 5.73,
                        "percentage": 11.4
                },
                {
                        "category": "Segment D",
                        "value": 5.36,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 17.91,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.400081",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Back Order Rate"
        }
    },
}
