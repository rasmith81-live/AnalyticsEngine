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
                        222,
                        240,
                        241,
                        215,
                        238,
                        211,
                        229,
                        250,
                        218,
                        211,
                        223,
                        228
                ],
                "unit": "count"
        },
        "current": {
                "value": 228,
                "unit": "count",
                "change": 5,
                "change_percent": 2.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 227.17,
                "min": 211,
                "max": 250,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 65.02,
                        "percentage": 28.5
                },
                {
                        "category": "Category B",
                        "value": 57.02,
                        "percentage": 25.0
                },
                {
                        "category": "Category C",
                        "value": 32.98,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 18.36,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 54.62,
                        "percentage": 24.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.441834",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Detention Time"
        }
    },
}
