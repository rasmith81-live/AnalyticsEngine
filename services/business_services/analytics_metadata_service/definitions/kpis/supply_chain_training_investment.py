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
                        390.83,
                        344.49,
                        426.39,
                        317.56,
                        401.81,
                        358.22,
                        383.54,
                        404.63,
                        409.68,
                        401.57,
                        389.82,
                        405.68
                ],
                "unit": "units"
        },
        "current": {
                "value": 405.68,
                "unit": "units",
                "change": 15.86,
                "change_percent": 4.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 386.19,
                "min": 317.56,
                "max": 426.39,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 125.9,
                        "percentage": 31.0
                },
                {
                        "category": "Segment B",
                        "value": 96.27,
                        "percentage": 23.7
                },
                {
                        "category": "Segment C",
                        "value": 47.89,
                        "percentage": 11.8
                },
                {
                        "category": "Segment D",
                        "value": 16.92,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 118.7,
                        "percentage": 29.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.686741",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supply Chain Training Investment"
        }
    },
}
