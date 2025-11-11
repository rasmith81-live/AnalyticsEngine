"""
Business Continuity Plan Effectiveness

The effectiveness of the business continuity plan as it relates to supply chain operations, which is essential for maintaining operations during and after security incidents.
"""

BUSINESS_CONTINUITY_PLAN_EFFECTIVENESS = {
    "code": "BUSINESS_CONTINUITY_PLAN_EFFECTIVENESS",
    "name": "Business Continuity Plan Effectiveness",
    "description": "The effectiveness of the business continuity plan as it relates to supply chain operations, which is essential for maintaining operations during and after security incidents.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Business Continuity Plan Effectiveness to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.668760"},
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
                        792.38,
                        854.03,
                        737.84,
                        864.25,
                        733.73,
                        741.87,
                        837.44,
                        788.96,
                        873.48,
                        759.75,
                        841.52,
                        749.67
                ],
                "unit": "units"
        },
        "current": {
                "value": 749.67,
                "unit": "units",
                "change": -91.85,
                "change_percent": -10.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 797.91,
                "min": 733.73,
                "max": 873.48,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 246.73,
                        "percentage": 32.9
                },
                {
                        "category": "Segment B",
                        "value": 111.66,
                        "percentage": 14.9
                },
                {
                        "category": "Segment C",
                        "value": 130.74,
                        "percentage": 17.4
                },
                {
                        "category": "Segment D",
                        "value": 65.31,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 195.23,
                        "percentage": 26.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.409713",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Business Continuity Plan Effectiveness"
        }
    },
}
