"""
Freight Cost as a Percentage of Sales

The cost of transportation and logistics as a percentage of total sales, indicating the cost efficiency of logistics.
"""

FREIGHT_COST_AS_A_PERCENTAGE_OF_SALES = {
    "code": "FREIGHT_COST_AS_A_PERCENTAGE_OF_SALES",
    "name": "Freight Cost as a Percentage of Sales",
    "description": "The cost of transportation and logistics as a percentage of total sales, indicating the cost efficiency of logistics.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Freight Cost as a Percentage of Sales to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.502476"},
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
                        40.38,
                        36.18,
                        35.52,
                        36.62,
                        43.14,
                        51.11,
                        37.09,
                        43.98,
                        54.19,
                        49.41,
                        40.12,
                        39.07
                ],
                "unit": "%"
        },
        "current": {
                "value": 39.07,
                "unit": "%",
                "change": -1.05,
                "change_percent": -2.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 42.23,
                "min": 35.52,
                "max": 54.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 6.81,
                        "percentage": 17.4
                },
                {
                        "category": "Category B",
                        "value": 7.74,
                        "percentage": 19.8
                },
                {
                        "category": "Category C",
                        "value": 5.0,
                        "percentage": 12.8
                },
                {
                        "category": "Category D",
                        "value": 5.67,
                        "percentage": 14.5
                },
                {
                        "category": "Other",
                        "value": 13.85,
                        "percentage": 35.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.502476",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Freight Cost as a Percentage of Sales"
        }
    },
}
