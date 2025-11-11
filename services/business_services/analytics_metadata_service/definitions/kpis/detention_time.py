"""
Detention Time

The time a vehicle spends waiting at a facility beyond the expected loading or unloading time.
"""

DETENTION_TIME = {
    "code": "DETENTION_TIME",
    "name": "Detention Time",
    "description": "The time a vehicle spends waiting at a facility beyond the expected loading or unloading time.",
    "formula": "Total Detention Time / Number of Deliveries",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Detention Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.929470"},
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
                        360,
                        375,
                        381,
                        378,
                        391,
                        388,
                        357,
                        355,
                        358,
                        386,
                        345,
                        368
                ],
                "unit": "count"
        },
        "current": {
                "value": 368,
                "unit": "count",
                "change": 23,
                "change_percent": 6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 370.17,
                "min": 345,
                "max": 391,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 118.48,
                        "percentage": 32.2
                },
                {
                        "category": "Segment B",
                        "value": 85.75,
                        "percentage": 23.3
                },
                {
                        "category": "Segment C",
                        "value": 54.07,
                        "percentage": 14.7
                },
                {
                        "category": "Segment D",
                        "value": 18.24,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 91.46,
                        "percentage": 24.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.925781",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Detention Time"
        }
    },
}
