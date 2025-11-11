"""
Cost per Order

The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.
"""

COST_PER_ORDER = {
    "code": "COST_PER_ORDER",
    "name": "Cost per Order",
    "description": "The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.",
    "formula": "Total Cost of Procurement Operations / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Order to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.171688"},
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
                        416,
                        401,
                        435,
                        399,
                        433,
                        408,
                        391,
                        423,
                        410,
                        432,
                        404,
                        422
                ],
                "unit": "count"
        },
        "current": {
                "value": 422,
                "unit": "count",
                "change": 18,
                "change_percent": 4.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 414.5,
                "min": 391,
                "max": 435,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 126.31,
                        "percentage": 29.9
                },
                {
                        "category": "Category B",
                        "value": 71.64,
                        "percentage": 17.0
                },
                {
                        "category": "Category C",
                        "value": 59.98,
                        "percentage": 14.2
                },
                {
                        "category": "Category D",
                        "value": 42.77,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 121.3,
                        "percentage": 28.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.171688",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Order"
        }
    },
}
