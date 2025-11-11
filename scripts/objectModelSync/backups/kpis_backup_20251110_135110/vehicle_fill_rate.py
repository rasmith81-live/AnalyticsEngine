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
                        60.02,
                        64.36,
                        66.34,
                        58.53,
                        54.96,
                        51.94,
                        61.64,
                        69.88,
                        68.6,
                        60.1,
                        52.99,
                        64.14
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.14,
                "unit": "%",
                "change": 11.15,
                "change_percent": 21.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 61.12,
                "min": 51.94,
                "max": 69.88,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.67,
                        "percentage": 18.2
                },
                {
                        "category": "Category B",
                        "value": 10.46,
                        "percentage": 16.3
                },
                {
                        "category": "Category C",
                        "value": 13.68,
                        "percentage": 21.3
                },
                {
                        "category": "Category D",
                        "value": 6.86,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 21.47,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.203607",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Vehicle Fill Rate"
        }
    },
}
