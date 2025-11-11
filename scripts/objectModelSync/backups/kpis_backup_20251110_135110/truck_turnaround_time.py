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
                        16.9,
                        15.1,
                        13.3,
                        15.9,
                        16.0,
                        11.9,
                        14.0,
                        17.1,
                        10.9,
                        14.4,
                        13.7,
                        13.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 13.6,
                "unit": "days",
                "change": -0.1,
                "change_percent": -0.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 14.4,
                "min": 10.9,
                "max": 17.1,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.68,
                        "percentage": 27.1
                },
                {
                        "category": "Category B",
                        "value": 2.19,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 1.85,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 1.03,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 4.85,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.158044",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Truck Turnaround Time"
        }
    },
}
