"""
Stock-out Rate

The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.
"""

STOCK_OUT_RATE = {
    "code": "STOCK_OUT_RATE",
    "name": "Stock-out Rate",
    "description": "The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stock-out Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Inventory", "Order", "Product", "Supplier"], "last_validated": "2025-11-10T13:43:24.791708"},
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
                        63.25,
                        80.76,
                        80.18,
                        71.88,
                        79.89,
                        77.88,
                        62.26,
                        70.4,
                        76.93,
                        66.54,
                        80.83,
                        79.38
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.38,
                "unit": "%",
                "change": -1.45,
                "change_percent": -1.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.18,
                "min": 62.26,
                "max": 80.83,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 27.16,
                        "percentage": 34.2
                },
                {
                        "category": "Category B",
                        "value": 13.81,
                        "percentage": 17.4
                },
                {
                        "category": "Category C",
                        "value": 10.59,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 6.41,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 21.41,
                        "percentage": 27.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.791708",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Stock-out Rate"
        }
    },
}
