"""
Total Spend Under Management

The total value of expenditures that are actively managed by the procurement team.
"""

SPEND_UNDER_MANAGEMENT = {
    "code": "SPEND_UNDER_MANAGEMENT",
    "name": "Total Spend Under Management",
    "description": "The total value of expenditures that are actively managed by the procurement team.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Total Spend Under Management to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.583594"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        936.71,
                        966.53,
                        972.76,
                        915.45,
                        897.36,
                        851.76,
                        910.06,
                        896.82,
                        970.46,
                        857.24,
                        908.24,
                        977.15
                ],
                "unit": "units"
        },
        "current": {
                "value": 977.15,
                "unit": "units",
                "change": 68.91,
                "change_percent": 7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 921.71,
                "min": 851.76,
                "max": 977.15,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 195.35,
                        "percentage": 20.0
                },
                {
                        "category": "Category B",
                        "value": 195.41,
                        "percentage": 20.0
                },
                {
                        "category": "Category C",
                        "value": 106.51,
                        "percentage": 10.9
                },
                {
                        "category": "Category D",
                        "value": 102.36,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 377.52,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.781352",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Total Spend Under Management"
        }
    },
}
