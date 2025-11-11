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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.675210"},
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
                        75.4,
                        80.4,
                        73.4,
                        82.1,
                        80.1,
                        75.8,
                        72.0,
                        72.9,
                        84.6,
                        76.3,
                        77.9,
                        83.9
                ],
                "unit": "score"
        },
        "current": {
                "value": 83.9,
                "unit": "score",
                "change": 6.0,
                "change_percent": 7.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 77.9,
                "min": 72.0,
                "max": 84.6,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.54,
                        "percentage": 22.1
                },
                {
                        "category": "Segment B",
                        "value": 22.07,
                        "percentage": 26.3
                },
                {
                        "category": "Segment C",
                        "value": 11.78,
                        "percentage": 14.0
                },
                {
                        "category": "Segment D",
                        "value": 7.85,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 23.66,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.661783",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Supply Chain Security Culture Index"
        }
    },
}
