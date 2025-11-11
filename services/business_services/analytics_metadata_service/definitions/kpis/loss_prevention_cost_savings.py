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
                        69280.9,
                        67362.31,
                        65243.66,
                        72399.31,
                        70291.01,
                        77680.21,
                        70918.34,
                        71109.95,
                        64071.27,
                        74880.82,
                        75187.93,
                        77208.36
                ],
                "unit": "$"
        },
        "current": {
                "value": 77208.36,
                "unit": "$",
                "change": 2020.43,
                "change_percent": 2.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 71302.84,
                "min": 64071.27,
                "max": 77680.21,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20619.9,
                        "percentage": 26.7
                },
                {
                        "category": "Segment B",
                        "value": 15620.58,
                        "percentage": 20.2
                },
                {
                        "category": "Segment C",
                        "value": 9542.22,
                        "percentage": 12.4
                },
                {
                        "category": "Segment D",
                        "value": 6921.92,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 24503.74,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.163396",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Loss Prevention Cost Savings"
        }
    },
}
