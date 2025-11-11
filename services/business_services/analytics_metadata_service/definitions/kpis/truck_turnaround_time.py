"""
Truck Turnaround Time

The total time from when a truck arrives at a facility until it departs.
"""

TRUCK_TURNAROUND_TIME = {
    "code": "TRUCK_TURNAROUND_TIME",
    "name": "Truck Turnaround Time",
    "description": "The total time from when a truck arrives at a facility until it departs.",
    "formula": "Average Time from Departure to Return for Each Truck",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Truck Turnaround Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Return"], "last_validated": "2025-11-10T13:49:33.759882"},
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
                        14.3,
                        14.7,
                        9.8,
                        11.0,
                        8.7,
                        11.7,
                        15.0,
                        11.8,
                        13.6,
                        10.8,
                        11.1,
                        14.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 14.3,
                "unit": "days",
                "change": 3.2,
                "change_percent": 28.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 12.23,
                "min": 8.7,
                "max": 15.0,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.62,
                        "percentage": 18.3
                },
                {
                        "category": "Segment B",
                        "value": 1.99,
                        "percentage": 13.9
                },
                {
                        "category": "Segment C",
                        "value": 3.31,
                        "percentage": 23.1
                },
                {
                        "category": "Segment D",
                        "value": 1.29,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 5.09,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.894563",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Truck Turnaround Time"
        }
    },
}
