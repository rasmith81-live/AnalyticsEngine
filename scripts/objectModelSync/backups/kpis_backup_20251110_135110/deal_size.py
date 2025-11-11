"""
Deal Size

The average value of closed deals.
"""

DEAL_SIZE = {
    "code": "DEAL_SIZE",
    "name": "Deal Size",
    "description": "The average value of closed deals.",
    "formula": "Total Revenue from Closed Deals / Number of Closed Deals",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Deal Size to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:32.911021"},
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
                        104,
                        70,
                        77,
                        103,
                        92,
                        63,
                        97,
                        112,
                        89,
                        107,
                        95,
                        67
                ],
                "unit": "count"
        },
        "current": {
                "value": 67,
                "unit": "count",
                "change": -28,
                "change_percent": -29.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 89.67,
                "min": 63,
                "max": 112,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.61,
                        "percentage": 33.7
                },
                {
                        "category": "Category B",
                        "value": 7.08,
                        "percentage": 10.6
                },
                {
                        "category": "Category C",
                        "value": 8.84,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 4.81,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 23.66,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.411195",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Deal Size"
        }
    },
}
