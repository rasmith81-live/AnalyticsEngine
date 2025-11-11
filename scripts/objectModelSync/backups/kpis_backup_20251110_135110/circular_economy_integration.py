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
                        51.82,
                        48.35,
                        45.65,
                        44.1,
                        32.04,
                        41.47,
                        33.14,
                        32.13,
                        40.37,
                        45.36,
                        51.27,
                        33.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 33.71,
                "unit": "%",
                "change": -17.56,
                "change_percent": -34.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 41.62,
                "min": 32.04,
                "max": 51.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.79,
                        "percentage": 26.1
                },
                {
                        "category": "Category B",
                        "value": 4.15,
                        "percentage": 12.3
                },
                {
                        "category": "Category C",
                        "value": 6.17,
                        "percentage": 18.3
                },
                {
                        "category": "Category D",
                        "value": 1.92,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 12.68,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.109337",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Circular Economy Integration"
        }
    },
}
