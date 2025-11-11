"""
Load Factor

The percentage of a transport vehicle’s available capacity that is being used.
"""

LOAD_FACTOR = {
    "code": "LOAD_FACTOR",
    "name": "Load Factor",
    "description": "The percentage of a transport vehicle\u2019s available capacity that is being used.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Load Factor to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:43:23.609485"},
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
                        313.57,
                        174.26,
                        248.69,
                        215.73,
                        237.07,
                        237.0,
                        218.56,
                        189.82,
                        200.29,
                        313.81,
                        291.63,
                        211.71
                ],
                "unit": "units"
        },
        "current": {
                "value": 211.71,
                "unit": "units",
                "change": -79.92,
                "change_percent": -27.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 237.68,
                "min": 174.26,
                "max": 313.81,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 68.79,
                        "percentage": 32.5
                },
                {
                        "category": "Category B",
                        "value": 29.9,
                        "percentage": 14.1
                },
                {
                        "category": "Category C",
                        "value": 37.4,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 15.59,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 60.03,
                        "percentage": 28.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.609485",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Load Factor"
        }
    },
}
