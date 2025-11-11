"""
Supply Chain Visibility Index

The degree to which the organization has visibility over its entire supply chain, which is critical for identifying and mitigating security risks.
"""

SUPPLY_CHAIN_VISIBILITY_INDEX = {
    "code": "SUPPLY_CHAIN_VISIBILITY_INDEX",
    "name": "Supply Chain Visibility Index",
    "description": "The degree to which the organization has visibility over its entire supply chain, which is critical for identifying and mitigating security risks.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Visibility Index to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.688769"},
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
                        56.3,
                        68.3,
                        67.3,
                        67.7,
                        62.6,
                        64.8,
                        60.9,
                        65.6,
                        66.3,
                        58.7,
                        59.2,
                        68.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 68.6,
                "unit": "score",
                "change": 9.4,
                "change_percent": 15.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 63.86,
                "min": 56.3,
                "max": 68.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.55,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 10.97,
                        "percentage": 16.0
                },
                {
                        "category": "Category C",
                        "value": 9.31,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 7.5,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 21.27,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.956721",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Visibility Index"
        }
    },
}
