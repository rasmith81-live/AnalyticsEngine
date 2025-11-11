"""
Vehicle Fill Rate

The percentage of a vehicle’s capacity that is filled with cargo.
"""

VEHICLE_FILL_RATE = {
    "code": "VEHICLE_FILL_RATE",
    "name": "Vehicle Fill Rate",
    "description": "The percentage of a vehicle\u2019s capacity that is filled with cargo.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Vehicle Fill Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.778069"},
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
                        43.61,
                        33.07,
                        41.87,
                        37.32,
                        31.66,
                        47.3,
                        40.44,
                        37.5,
                        38.03,
                        32.59,
                        42.06,
                        31.49
                ],
                "unit": "%"
        },
        "current": {
                "value": 31.49,
                "unit": "%",
                "change": -10.57,
                "change_percent": -25.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 38.08,
                "min": 31.49,
                "max": 47.3,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 5.95,
                        "percentage": 18.9
                },
                {
                        "category": "Segment B",
                        "value": 7.15,
                        "percentage": 22.7
                },
                {
                        "category": "Segment C",
                        "value": 3.95,
                        "percentage": 12.5
                },
                {
                        "category": "Segment D",
                        "value": 2.95,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 11.49,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.933920",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Vehicle Fill Rate"
        }
    },
}
