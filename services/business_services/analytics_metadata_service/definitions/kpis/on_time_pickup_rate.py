"""
On-time Pickup Rate

The percentage of pickups that occur at the scheduled time.
"""

ON_TIME_PICKUP_RATE = {
    "code": "ON_TIME_PICKUP_RATE",
    "name": "On-time Pickup Rate",
    "description": "The percentage of pickups that occur at the scheduled time.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for On-time Pickup Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.101390"},
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
                        40.12,
                        50.26,
                        35.46,
                        48.77,
                        48.41,
                        36.41,
                        39.91,
                        39.73,
                        47.45,
                        39.68,
                        48.53,
                        49.43
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.43,
                "unit": "%",
                "change": 0.9,
                "change_percent": 1.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 43.68,
                "min": 35.46,
                "max": 50.26,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.77,
                        "percentage": 23.8
                },
                {
                        "category": "Segment B",
                        "value": 9.69,
                        "percentage": 19.6
                },
                {
                        "category": "Segment C",
                        "value": 8.29,
                        "percentage": 16.8
                },
                {
                        "category": "Segment D",
                        "value": 3.47,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 16.21,
                        "percentage": 32.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.284617",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Pickup Rate"
        }
    },
}
