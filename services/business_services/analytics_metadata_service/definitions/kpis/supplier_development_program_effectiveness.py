"""
Supplier Development Program Effectiveness

The effectiveness of programs aimed at improving suppliers
"""

SUPPLIER_DEVELOPMENT_PROGRAM_EFFECTIVENESS = {
    "code": "SUPPLIER_DEVELOPMENT_PROGRAM_EFFECTIVENESS",
    "name": "Supplier Development Program Effectiveness",
    "description": "The effectiveness of programs aimed at improving suppliers",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Development Program Effectiveness to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.629166"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        707.94,
                        702.57,
                        756.75,
                        737.58,
                        761.03,
                        704.32,
                        781.79,
                        768.75,
                        752.47,
                        756.98,
                        666.63,
                        800.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 800.06,
                "unit": "units",
                "change": 133.43,
                "change_percent": 20.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 741.41,
                "min": 666.63,
                "max": 800.06,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 254.65,
                        "percentage": 31.8
                },
                {
                        "category": "Segment B",
                        "value": 140.39,
                        "percentage": 17.5
                },
                {
                        "category": "Segment C",
                        "value": 114.43,
                        "percentage": 14.3
                },
                {
                        "category": "Segment D",
                        "value": 58.21,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 232.38,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.530592",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Development Program Effectiveness"
        }
    },
}
