"""
Loss Prevention Cost Savings

The cost savings realized from loss prevention strategies and security measures within the supply chain.
"""

LOSS_PREVENTION_COST_SAVINGS = {
    "code": "LOSS_PREVENTION_COST_SAVINGS",
    "name": "Loss Prevention Cost Savings",
    "description": "The cost savings realized from loss prevention strategies and security measures within the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Loss Prevention Cost Savings to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.028803"},
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
                        10750.09,
                        12046.54,
                        10032.3,
                        17259.72,
                        22357.65,
                        23397.11,
                        19433.85,
                        9593.45,
                        21492.03,
                        19015.65,
                        10330.87,
                        17348.47
                ],
                "unit": "$"
        },
        "current": {
                "value": 17348.47,
                "unit": "$",
                "change": 7017.6,
                "change_percent": 67.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 16088.14,
                "min": 9593.45,
                "max": 23397.11,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 5242.17,
                        "percentage": 30.2
                },
                {
                        "category": "Category B",
                        "value": 4183.09,
                        "percentage": 24.1
                },
                {
                        "category": "Category C",
                        "value": 1877.88,
                        "percentage": 10.8
                },
                {
                        "category": "Category D",
                        "value": 1339.59,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 4705.74,
                        "percentage": 27.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.619530",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Loss Prevention Cost Savings"
        }
    },
}
