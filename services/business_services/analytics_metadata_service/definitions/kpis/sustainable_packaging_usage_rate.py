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
                        42.58,
                        51.11,
                        51.85,
                        47.61,
                        38.8,
                        51.15,
                        51.65,
                        41.47,
                        37.15,
                        54.25,
                        39.32,
                        41.54
                ],
                "unit": "%"
        },
        "current": {
                "value": 41.54,
                "unit": "%",
                "change": 2.22,
                "change_percent": 5.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 45.71,
                "min": 37.15,
                "max": 54.25,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.91,
                        "percentage": 28.7
                },
                {
                        "category": "Segment B",
                        "value": 8.2,
                        "percentage": 19.7
                },
                {
                        "category": "Segment C",
                        "value": 6.34,
                        "percentage": 15.3
                },
                {
                        "category": "Segment D",
                        "value": 2.72,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 12.37,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.718661",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sustainable Packaging Usage Rate"
        }
    },
}
