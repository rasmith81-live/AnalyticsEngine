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
                        508.79,
                        512.6,
                        606.92,
                        573.2,
                        584.26,
                        599.56,
                        473.78,
                        582.71,
                        550.29,
                        471.27,
                        538.27,
                        463.66
                ],
                "unit": "units"
        },
        "current": {
                "value": 463.66,
                "unit": "units",
                "change": -74.61,
                "change_percent": -13.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 538.78,
                "min": 463.66,
                "max": 606.92,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 134.71,
                        "percentage": 29.1
                },
                {
                        "category": "Segment B",
                        "value": 56.56,
                        "percentage": 12.2
                },
                {
                        "category": "Segment C",
                        "value": 69.63,
                        "percentage": 15.0
                },
                {
                        "category": "Segment D",
                        "value": 21.73,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 181.03,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.405237",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Total Spend Under Management"
        }
    },
}
