"""
Backorder Rate

The percentage of orders that cannot be filled immediately and are placed on backorder.
"""

BACKORDER_RATE = {
    "code": "BACKORDER_RATE",
    "name": "Backorder Rate",
    "description": "The percentage of orders that cannot be filled immediately and are placed on backorder.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Backorder Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Inventory", "Order", "Product"], "last_validated": "2025-11-10T13:43:23.056330"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        55.05,
                        58.83,
                        53.14,
                        44.67,
                        50.78,
                        56.29,
                        54.55,
                        57.96,
                        58.9,
                        52.95,
                        53.86,
                        51.25
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.25,
                "unit": "%",
                "change": -2.61,
                "change_percent": -4.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 54.02,
                "min": 44.67,
                "max": 58.9,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.31,
                        "percentage": 18.2
                },
                {
                        "category": "Category B",
                        "value": 10.45,
                        "percentage": 20.4
                },
                {
                        "category": "Category C",
                        "value": 10.46,
                        "percentage": 20.4
                },
                {
                        "category": "Category D",
                        "value": 3.02,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 18.01,
                        "percentage": 35.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.056330",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Backorder Rate"
        }
    },
}
