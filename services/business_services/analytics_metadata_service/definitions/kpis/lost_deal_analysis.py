"""
Lost Deal Analysis

The systematic examination of lost deals to understand why they were not won and to implement improvements.
"""

LOST_DEAL_ANALYSIS = {
    "code": "LOST_DEAL_ANALYSIS",
    "name": "Lost Deal Analysis",
    "description": "The systematic examination of lost deals to understand why they were not won and to implement improvements.",
    "formula": "(Qualitative analysis based on deal feedback and data)",
    "calculation_formula": "(Qualitative analysis based on deal feedback and data)",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lost Deal Analysis to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:33.029804"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        504.51,
                        586.67,
                        597.25,
                        585.49,
                        592.25,
                        557.3,
                        617.66,
                        519.74,
                        601.08,
                        560.12,
                        582.55,
                        608.14
                ],
                "unit": "units"
        },
        "current": {
                "value": 608.14,
                "unit": "units",
                "change": 25.59,
                "change_percent": 4.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 576.06,
                "min": 504.51,
                "max": 617.66,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 181.44,
                        "percentage": 29.8
                },
                {
                        "category": "Segment B",
                        "value": 109.62,
                        "percentage": 18.0
                },
                {
                        "category": "Segment C",
                        "value": 110.32,
                        "percentage": 18.1
                },
                {
                        "category": "Segment D",
                        "value": 21.19,
                        "percentage": 3.5
                },
                {
                        "category": "Other",
                        "value": 185.57,
                        "percentage": 30.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.163979",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Deal Analysis"
        }
    },
}
