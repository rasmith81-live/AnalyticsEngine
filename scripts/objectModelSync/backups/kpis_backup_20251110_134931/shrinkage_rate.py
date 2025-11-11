"""
Shrinkage Rate

The percentage of inventory loss between manufacture and point of sale.
"""

SHRINKAGE_RATE = {
    "code": "SHRINKAGE_RATE",
    "name": "Shrinkage Rate",
    "description": "The percentage of inventory loss between manufacture and point of sale.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shrinkage Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.767668"},
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
                        46.77,
                        45.73,
                        52.99,
                        43.45,
                        41.87,
                        38.32,
                        48.14,
                        36.59,
                        49.18,
                        47.52,
                        44.49,
                        38.06
                ],
                "unit": "%"
        },
        "current": {
                "value": 38.06,
                "unit": "%",
                "change": -6.43,
                "change_percent": -14.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 44.43,
                "min": 36.59,
                "max": 52.99,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.89,
                        "percentage": 33.9
                },
                {
                        "category": "Category B",
                        "value": 8.35,
                        "percentage": 21.9
                },
                {
                        "category": "Category C",
                        "value": 2.79,
                        "percentage": 7.3
                },
                {
                        "category": "Category D",
                        "value": 3.72,
                        "percentage": 9.8
                },
                {
                        "category": "Other",
                        "value": 10.31,
                        "percentage": 27.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.767668",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Shrinkage Rate"
        }
    },
}
