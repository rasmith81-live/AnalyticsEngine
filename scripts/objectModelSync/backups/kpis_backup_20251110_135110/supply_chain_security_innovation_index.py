"""
Supply Chain Security Innovation Index

A measure of the organization
"""

SUPPLY_CHAIN_SECURITY_INNOVATION_INDEX = {
    "code": "SUPPLY_CHAIN_SECURITY_INNOVATION_INDEX",
    "name": "Supply Chain Security Innovation Index",
    "description": "A measure of the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Security Innovation Index to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.676989"},
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
                        86.6,
                        81.1,
                        82.1,
                        81.5,
                        82.0,
                        87.4,
                        81.2,
                        87.3,
                        81.0,
                        90.7,
                        79.7,
                        86.0
                ],
                "unit": "score"
        },
        "current": {
                "value": 86.0,
                "unit": "score",
                "change": 6.3,
                "change_percent": 7.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 83.88,
                "min": 79.7,
                "max": 90.7,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.85,
                        "percentage": 27.7
                },
                {
                        "category": "Category B",
                        "value": 13.18,
                        "percentage": 15.3
                },
                {
                        "category": "Category C",
                        "value": 14.77,
                        "percentage": 17.2
                },
                {
                        "category": "Category D",
                        "value": 7.75,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 26.45,
                        "percentage": 30.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.932755",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Security Innovation Index"
        }
    },
}
