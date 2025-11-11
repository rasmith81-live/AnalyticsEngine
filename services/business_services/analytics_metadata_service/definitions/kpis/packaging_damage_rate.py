"""
Packaging Damage Rate

The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.
"""

PACKAGING_DAMAGE_RATE = {
    "code": "PACKAGING_DAMAGE_RATE",
    "name": "Packaging Damage Rate",
    "description": "The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packaging Damage Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.142301"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        54.2,
                        47.17,
                        40.78,
                        41.54,
                        48.75,
                        46.34,
                        44.97,
                        41.88,
                        52.95,
                        47.75,
                        44.44,
                        41.31
                ],
                "unit": "%"
        },
        "current": {
                "value": 41.31,
                "unit": "%",
                "change": -3.13,
                "change_percent": -7.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 46.01,
                "min": 40.78,
                "max": 54.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 6.96,
                        "percentage": 16.8
                },
                {
                        "category": "Segment B",
                        "value": 9.45,
                        "percentage": 22.9
                },
                {
                        "category": "Segment C",
                        "value": 6.75,
                        "percentage": 16.3
                },
                {
                        "category": "Segment D",
                        "value": 3.86,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 14.29,
                        "percentage": 34.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.368095",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packaging Damage Rate"
        }
    },
}
