"""
Sustainable Packaging Usage Rate

The percentage of packaging materials that are recyclable, reusable, or biodegradable, in line with ISO 20400.
"""

SUSTAINABLE_PACKAGING_USAGE_RATE = {
    "code": "SUSTAINABLE_PACKAGING_USAGE_RATE",
    "name": "Sustainable Packaging Usage Rate",
    "description": "The percentage of packaging materials that are recyclable, reusable, or biodegradable, in line with ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sustainable Packaging Usage Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.695441"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        57.48,
                        56.4,
                        66.98,
                        54.62,
                        64.4,
                        59.14,
                        58.92,
                        63.04,
                        60.34,
                        52.19,
                        61.08,
                        49.79
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.79,
                "unit": "%",
                "change": -11.29,
                "change_percent": -18.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 58.7,
                "min": 49.79,
                "max": 66.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.33,
                        "percentage": 32.8
                },
                {
                        "category": "Category B",
                        "value": 7.37,
                        "percentage": 14.8
                },
                {
                        "category": "Category C",
                        "value": 7.84,
                        "percentage": 15.7
                },
                {
                        "category": "Category D",
                        "value": 2.98,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 15.27,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.972788",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sustainable Packaging Usage Rate"
        }
    },
}
