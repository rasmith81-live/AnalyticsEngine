"""
Linehaul Efficiency

The efficiency of transportation between two points excluding pickup and delivery operations.
"""

LINEHAUL_EFFICIENCY = {
    "code": "LINEHAUL_EFFICIENCY",
    "name": "Linehaul Efficiency",
    "description": "The efficiency of transportation between two points excluding pickup and delivery operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Linehaul Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.607406"},
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
                        285.75,
                        326.26,
                        328.62,
                        230.0,
                        279.24,
                        315.99,
                        289.78,
                        276.72,
                        190.55,
                        280.26,
                        260.72,
                        323.24
                ],
                "unit": "units"
        },
        "current": {
                "value": 323.24,
                "unit": "units",
                "change": 62.52,
                "change_percent": 24.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 282.26,
                "min": 190.55,
                "max": 328.62,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 57.48,
                        "percentage": 17.8
                },
                {
                        "category": "Category B",
                        "value": 57.32,
                        "percentage": 17.7
                },
                {
                        "category": "Category C",
                        "value": 34.53,
                        "percentage": 10.7
                },
                {
                        "category": "Category D",
                        "value": 24.57,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 149.34,
                        "percentage": 46.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.607406",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Linehaul Efficiency"
        }
    },
}
