"""
Supply Chain Resilience Index

A measure of the supply chain
"""

SUPPLY_CHAIN_RESILIENCE_INDEX = {
    "code": "SUPPLY_CHAIN_RESILIENCE_INDEX",
    "name": "Supply Chain Resilience Index",
    "description": "A measure of the supply chain",
    "formula": "Supply Chain Resilience Score",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Resilience Index to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.668801"},
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
                        83.3,
                        90.5,
                        82.3,
                        79.7,
                        91.1,
                        89.6,
                        81.0,
                        84.3,
                        83.1,
                        80.1,
                        86.0,
                        88.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 88.5,
                "unit": "score",
                "change": 2.5,
                "change_percent": 2.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 84.96,
                "min": 79.7,
                "max": 91.1,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.24,
                        "percentage": 22.9
                },
                {
                        "category": "Segment B",
                        "value": 17.88,
                        "percentage": 20.2
                },
                {
                        "category": "Segment C",
                        "value": 8.72,
                        "percentage": 9.9
                },
                {
                        "category": "Segment D",
                        "value": 4.27,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 37.39,
                        "percentage": 42.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.638754",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Resilience Index"
        }
    },
}
