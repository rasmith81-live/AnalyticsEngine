"""
Empty Miles

The number of miles a vehicle travels empty without carrying any load.
"""

EMPTY_MILES = {
    "code": "EMPTY_MILES",
    "name": "Empty Miles",
    "description": "The number of miles a vehicle travels empty without carrying any load.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Empty Miles to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.944360"},
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
                        842.56,
                        839.18,
                        772.98,
                        895.16,
                        777.66,
                        801.46,
                        853.59,
                        785.33,
                        769.25,
                        913.09,
                        771.25,
                        783.11
                ],
                "unit": "units"
        },
        "current": {
                "value": 783.11,
                "unit": "units",
                "change": 11.86,
                "change_percent": 1.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 817.05,
                "min": 769.25,
                "max": 913.09,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 135.3,
                        "percentage": 17.3
                },
                {
                        "category": "Segment B",
                        "value": 114.41,
                        "percentage": 14.6
                },
                {
                        "category": "Segment C",
                        "value": 154.65,
                        "percentage": 19.7
                },
                {
                        "category": "Segment D",
                        "value": 43.23,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 335.52,
                        "percentage": 42.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.961588",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Empty Miles"
        }
    },
}
