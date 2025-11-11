"""
Fill Rate

The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.
"""

FILL_RATE = {
    "code": "FILL_RATE",
    "name": "Fill Rate",
    "description": "The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Fill Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Order", "Product"], "last_validated": "2025-11-10T13:43:23.484086"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        54.5,
                        56.93,
                        60.55,
                        52.78,
                        55.1,
                        56.49,
                        52.91,
                        55.72,
                        45.8,
                        50.7,
                        44.14,
                        43.88
                ],
                "unit": "%"
        },
        "current": {
                "value": 43.88,
                "unit": "%",
                "change": -0.26,
                "change_percent": -0.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 52.46,
                "min": 43.88,
                "max": 60.55,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.81,
                        "percentage": 33.8
                },
                {
                        "category": "Category B",
                        "value": 9.41,
                        "percentage": 21.4
                },
                {
                        "category": "Category C",
                        "value": 4.48,
                        "percentage": 10.2
                },
                {
                        "category": "Category D",
                        "value": 3.19,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 11.99,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.484086",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Fill Rate"
        }
    },
}
