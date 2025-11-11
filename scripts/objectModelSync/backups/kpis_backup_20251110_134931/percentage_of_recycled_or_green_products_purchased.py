"""
Percentage of Recycled or Green Products Purchased

The proportion of total purchases that are made up of environmentally friendly or sustainable products.
"""

PERCENTAGE_OF_RECYCLED_OR_GREEN_PRODUCTS_PURCHASED = {
    "code": "PERCENTAGE_OF_RECYCLED_OR_GREEN_PRODUCTS_PURCHASED",
    "name": "Percentage of Recycled or Green Products Purchased",
    "description": "The proportion of total purchases that are made up of environmentally friendly or sustainable products.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Percentage of Recycled or Green Products Purchased to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.921863"},
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
                        44.4,
                        53.46,
                        37.88,
                        38.07,
                        49.21,
                        52.11,
                        49.9,
                        47.8,
                        48.29,
                        37.78,
                        44.03,
                        42.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 42.08,
                "unit": "%",
                "change": -1.95,
                "change_percent": -4.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 45.42,
                "min": 37.78,
                "max": 53.46,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.13,
                        "percentage": 28.8
                },
                {
                        "category": "Category B",
                        "value": 8.08,
                        "percentage": 19.2
                },
                {
                        "category": "Category C",
                        "value": 5.37,
                        "percentage": 12.8
                },
                {
                        "category": "Category D",
                        "value": 4.21,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 12.29,
                        "percentage": 29.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.921863",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Percentage of Recycled or Green Products Purchased"
        }
    },
}
