"""
Supply Chain Training Investment

The amount invested in employee training to improve supply chain skills and knowledge, contributing to performance improvements.
"""

SUPPLY_CHAIN_TRAINING_INVESTMENT = {
    "code": "SUPPLY_CHAIN_TRAINING_INVESTMENT",
    "name": "Supply Chain Training Investment",
    "description": "The amount invested in employee training to improve supply chain skills and knowledge, contributing to performance improvements.",
    "formula": "Total Spend on Supply Chain Training",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Training Investment to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Employee"], "last_validated": "2025-11-10T13:49:33.683787"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        101.64,
                        163.46,
                        164.35,
                        101.95,
                        106.16,
                        204.74,
                        130.78,
                        105.35,
                        151.36,
                        212.38,
                        86.22,
                        143.17
                ],
                "unit": "units"
        },
        "current": {
                "value": 143.17,
                "unit": "units",
                "change": 56.95,
                "change_percent": 66.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 139.3,
                "min": 86.22,
                "max": 212.38,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.35,
                        "percentage": 16.3
                },
                {
                        "category": "Category B",
                        "value": 39.66,
                        "percentage": 27.7
                },
                {
                        "category": "Category C",
                        "value": 16.39,
                        "percentage": 11.4
                },
                {
                        "category": "Category D",
                        "value": 13.89,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 49.88,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.946541",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Training Investment"
        }
    },
}
