"""
Delivery Trip Standard Deviation

The variability in delivery trip duration.
"""

DELIVERY_TRIP_STANDARD_DEVIATION = {
    "code": "DELIVERY_TRIP_STANDARD_DEVIATION",
    "name": "Delivery Trip Standard Deviation",
    "description": "The variability in delivery trip duration.",
    "formula": "Standard Deviation of Delivery Trip Distances or Times",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Delivery Trip Standard Deviation to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:49:32.922132"},
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
                        986.07,
                        897.53,
                        932.52,
                        841.5,
                        985.29,
                        946.98,
                        868.18,
                        965.06,
                        852.45,
                        975.34,
                        900.82,
                        935.02
                ],
                "unit": "units"
        },
        "current": {
                "value": 935.02,
                "unit": "units",
                "change": 34.2,
                "change_percent": 3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 923.9,
                "min": 841.5,
                "max": 986.07,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 295.53,
                        "percentage": 31.6
                },
                {
                        "category": "Segment B",
                        "value": 163.79,
                        "percentage": 17.5
                },
                {
                        "category": "Segment C",
                        "value": 101.83,
                        "percentage": 10.9
                },
                {
                        "category": "Segment D",
                        "value": 51.88,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 321.99,
                        "percentage": 34.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.908071",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Delivery Trip Standard Deviation"
        }
    },
}
