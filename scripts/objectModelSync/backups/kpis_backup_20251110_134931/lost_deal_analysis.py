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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:43:23.622144"},
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
                        572.52,
                        573.0,
                        554.9,
                        630.13,
                        613.11,
                        630.65,
                        617.66,
                        579.14,
                        692.6,
                        671.86,
                        601.85,
                        618.76
                ],
                "unit": "units"
        },
        "current": {
                "value": 618.76,
                "unit": "units",
                "change": 16.91,
                "change_percent": 2.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 613.02,
                "min": 554.9,
                "max": 692.6,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 132.06,
                        "percentage": 21.3
                },
                {
                        "category": "Category B",
                        "value": 91.97,
                        "percentage": 14.9
                },
                {
                        "category": "Category C",
                        "value": 101.59,
                        "percentage": 16.4
                },
                {
                        "category": "Category D",
                        "value": 35.3,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 257.84,
                        "percentage": 41.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.622144",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Deal Analysis"
        }
    },
}
