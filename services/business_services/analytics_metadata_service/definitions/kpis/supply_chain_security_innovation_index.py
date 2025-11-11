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
                        66.6,
                        72.2,
                        75.0,
                        64.7,
                        62.5,
                        67.0,
                        62.9,
                        69.0,
                        68.9,
                        68.8,
                        68.5,
                        63.2
                ],
                "unit": "score"
        },
        "current": {
                "value": 63.2,
                "unit": "score",
                "change": -5.3,
                "change_percent": -7.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.44,
                "min": 62.5,
                "max": 75.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.32,
                        "percentage": 30.6
                },
                {
                        "category": "Segment B",
                        "value": 9.85,
                        "percentage": 15.6
                },
                {
                        "category": "Segment C",
                        "value": 10.26,
                        "percentage": 16.2
                },
                {
                        "category": "Segment D",
                        "value": 2.4,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 21.37,
                        "percentage": 33.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.666802",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Security Innovation Index"
        }
    },
}
