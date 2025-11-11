"""
Cross-docking Efficiency

The effectiveness of moving incoming goods directly to outbound shipping with no storage time.
"""

CROSS_DOCKING_EFFICIENCY = {
    "code": "CROSS_DOCKING_EFFICIENCY",
    "name": "Cross-docking Efficiency",
    "description": "The effectiveness of moving incoming goods directly to outbound shipping with no storage time.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cross-docking Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Product"], "last_validated": "2025-11-10T13:49:32.786368"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        322.34,
                        363.02,
                        241.4,
                        334.88,
                        335.41,
                        365.24,
                        322.7,
                        360.69,
                        319.08,
                        330.03,
                        257.47,
                        341.72
                ],
                "unit": "units"
        },
        "current": {
                "value": 341.72,
                "unit": "units",
                "change": 84.25,
                "change_percent": 32.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 324.5,
                "min": 241.4,
                "max": 365.24,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 92.6,
                        "percentage": 27.1
                },
                {
                        "category": "Segment B",
                        "value": 52.76,
                        "percentage": 15.4
                },
                {
                        "category": "Segment C",
                        "value": 61.67,
                        "percentage": 18.0
                },
                {
                        "category": "Segment D",
                        "value": 26.8,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 107.89,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.577149",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Cross-docking Efficiency"
        }
    },
}
