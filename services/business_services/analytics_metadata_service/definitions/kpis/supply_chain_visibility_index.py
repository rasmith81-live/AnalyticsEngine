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
                        68.7,
                        64.7,
                        68.0,
                        70.1,
                        74.1,
                        69.6,
                        66.6,
                        71.2,
                        67.5,
                        69.7,
                        62.3,
                        71.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 71.7,
                "unit": "score",
                "change": 9.4,
                "change_percent": 15.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.68,
                "min": 62.3,
                "max": 74.1,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 24.68,
                        "percentage": 34.4
                },
                {
                        "category": "Segment B",
                        "value": 16.22,
                        "percentage": 22.6
                },
                {
                        "category": "Segment C",
                        "value": 8.67,
                        "percentage": 12.1
                },
                {
                        "category": "Segment D",
                        "value": 4.29,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 17.84,
                        "percentage": 24.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.700807",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Visibility Index"
        }
    },
}
