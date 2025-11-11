"""
Supply Chain Security Culture Index

A measure of how deeply security awareness and best practices are embedded within the organization
"""

SUPPLY_CHAIN_SECURITY_CULTURE_INDEX = {
    "code": "SUPPLY_CHAIN_SECURITY_CULTURE_INDEX",
    "name": "Supply Chain Security Culture Index",
    "description": "A measure of how deeply security awareness and best practices are embedded within the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Security Culture Index to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.930113"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        72.3,
                        66.1,
                        71.3,
                        72.2,
                        68.9,
                        70.1,
                        72.6,
                        67.1,
                        65.1,
                        66.7,
                        70.4,
                        71.1
                ],
                "unit": "score"
        },
        "current": {
                "value": 71.1,
                "unit": "score",
                "change": 0.7,
                "change_percent": 1.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.49,
                "min": 65.1,
                "max": 72.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.95,
                        "percentage": 25.2
                },
                {
                        "category": "Category B",
                        "value": 15.66,
                        "percentage": 22.0
                },
                {
                        "category": "Category C",
                        "value": 8.38,
                        "percentage": 11.8
                },
                {
                        "category": "Category D",
                        "value": 3.57,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 25.54,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.930113",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Security Culture Index"
        }
    },
}
