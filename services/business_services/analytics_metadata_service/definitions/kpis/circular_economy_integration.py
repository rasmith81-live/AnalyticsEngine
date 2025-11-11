"""
Circular Economy Integration

The degree to which circular economy principles are integrated into procurement practices, as per ISO 20400.
"""

CIRCULAR_ECONOMY_INTEGRATION = {
    "code": "CIRCULAR_ECONOMY_INTEGRATION",
    "name": "Circular Economy Integration",
    "description": "The degree to which circular economy principles are integrated into procurement practices, as per ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Circular Economy Integration to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.696454"},
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
                        62.84,
                        60.36,
                        58.03,
                        60.63,
                        50.28,
                        54.11,
                        49.16,
                        51.5,
                        58.19,
                        46.6,
                        62.83,
                        46.43
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.43,
                "unit": "%",
                "change": -16.4,
                "change_percent": -26.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 55.08,
                "min": 46.43,
                "max": 62.84,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.41,
                        "percentage": 22.4
                },
                {
                        "category": "Segment B",
                        "value": 10.44,
                        "percentage": 22.5
                },
                {
                        "category": "Segment C",
                        "value": 8.39,
                        "percentage": 18.1
                },
                {
                        "category": "Segment D",
                        "value": 4.88,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 12.31,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.468386",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Circular Economy Integration"
        }
    },
}
