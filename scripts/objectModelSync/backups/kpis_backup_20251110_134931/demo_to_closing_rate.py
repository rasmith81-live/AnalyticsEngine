"""
Demo-to-Closing Rate

The percentage of product or service demonstrations that result in a closed sale.
"""

DEMO_TO_CLOSING_RATE = {
    "code": "DEMO_TO_CLOSING_RATE",
    "name": "Demo-to-Closing Rate",
    "description": "The percentage of product or service demonstrations that result in a closed sale.",
    "formula": "(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
    "calculation_formula": "(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demo-to-Closing Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "Product"], "last_validated": "2025-11-10T13:43:23.436846"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        58.82,
                        67.26,
                        60.52,
                        58.4,
                        63.97,
                        68.77,
                        67.15,
                        63.48,
                        51.17,
                        52.04,
                        66.32,
                        53.28
                ],
                "unit": "%"
        },
        "current": {
                "value": 53.28,
                "unit": "%",
                "change": -13.04,
                "change_percent": -19.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 60.93,
                "min": 51.17,
                "max": 68.77,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.09,
                        "percentage": 15.2
                },
                {
                        "category": "Category B",
                        "value": 8.66,
                        "percentage": 16.3
                },
                {
                        "category": "Category C",
                        "value": 6.14,
                        "percentage": 11.5
                },
                {
                        "category": "Category D",
                        "value": 8.36,
                        "percentage": 15.7
                },
                {
                        "category": "Other",
                        "value": 22.03,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.436846",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Demo-to-Closing Rate"
        }
    },
}
