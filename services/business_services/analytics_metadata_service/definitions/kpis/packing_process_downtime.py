"""
Packing Process Downtime

The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.
"""

PACKING_PROCESS_DOWNTIME = {
    "code": "PACKING_PROCESS_DOWNTIME",
    "name": "Packing Process Downtime",
    "description": "The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.",
    "formula": "Total Downtime / Total Packing Time",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Process Downtime to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.169174"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        26.1,
                        26.9,
                        20.9,
                        24.7,
                        22.1,
                        21.9,
                        20.7,
                        23.9,
                        24.5,
                        23.9,
                        25.3,
                        22.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 22.6,
                "unit": "days",
                "change": -2.7,
                "change_percent": -10.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 23.63,
                "min": 20.7,
                "max": 26.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 3.4,
                        "percentage": 15.0
                },
                {
                        "category": "Segment B",
                        "value": 6.14,
                        "percentage": 27.2
                },
                {
                        "category": "Segment C",
                        "value": 4.25,
                        "percentage": 18.8
                },
                {
                        "category": "Segment D",
                        "value": 1.34,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 7.47,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.420375",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Packing Process Downtime"
        }
    },
}
