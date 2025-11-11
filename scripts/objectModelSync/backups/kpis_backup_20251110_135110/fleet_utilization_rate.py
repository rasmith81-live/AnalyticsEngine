"""
Fleet Utilization Rate

The percentage of time a fleet is used compared to its availability for use.
"""

FLEET_UTILIZATION_RATE = {
    "code": "FLEET_UTILIZATION_RATE",
    "name": "Fleet Utilization Rate",
    "description": "The percentage of time a fleet is used compared to its availability for use.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Fleet Utilization Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.957758"},
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
                        38.52,
                        35.04,
                        33.05,
                        45.15,
                        44.21,
                        48.35,
                        36.23,
                        36.25,
                        38.9,
                        34.74,
                        42.82,
                        34.34
                ],
                "unit": "%"
        },
        "current": {
                "value": 34.34,
                "unit": "%",
                "change": -8.48,
                "change_percent": -19.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 38.97,
                "min": 33.05,
                "max": 48.35,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.13,
                        "percentage": 29.5
                },
                {
                        "category": "Category B",
                        "value": 6.05,
                        "percentage": 17.6
                },
                {
                        "category": "Category C",
                        "value": 3.68,
                        "percentage": 10.7
                },
                {
                        "category": "Category D",
                        "value": 3.98,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 10.5,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.492682",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Fleet Utilization Rate"
        }
    },
}
