"""
Local Sourcing Percentage

The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.
"""

LOCAL_SOURCING_PERCENTAGE = {
    "code": "LOCAL_SOURCING_PERCENTAGE",
    "name": "Local Sourcing Percentage",
    "description": "The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Local Sourcing Percentage to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.025789"},
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
                        72.28,
                        63.29,
                        72.36,
                        73.08,
                        77.42,
                        70.64,
                        78.31,
                        77.77,
                        75.63,
                        67.52,
                        78.87,
                        67.45
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.45,
                "unit": "%",
                "change": -11.42,
                "change_percent": -14.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 72.89,
                "min": 63.29,
                "max": 78.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.89,
                        "percentage": 29.5
                },
                {
                        "category": "Segment B",
                        "value": 12.71,
                        "percentage": 18.8
                },
                {
                        "category": "Segment C",
                        "value": 9.74,
                        "percentage": 14.4
                },
                {
                        "category": "Segment D",
                        "value": 6.73,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 18.38,
                        "percentage": 27.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.157556",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Local Sourcing Percentage"
        }
    },
}
