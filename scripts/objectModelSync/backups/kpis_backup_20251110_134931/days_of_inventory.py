"""
Days of Inventory

How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.
"""

DAYS_OF_INVENTORY = {
    "code": "DAYS_OF_INVENTORY",
    "name": "Days of Inventory",
    "description": "How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Days of Inventory to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.398694"},
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
                        26.6,
                        29.7,
                        26.1,
                        31.5,
                        28.3,
                        33.2,
                        30.9,
                        28.7,
                        32.0,
                        28.0,
                        26.6,
                        26.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 26.1,
                "unit": "days",
                "change": -0.5,
                "change_percent": -1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 28.98,
                "min": 26.1,
                "max": 33.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.74,
                        "percentage": 29.7
                },
                {
                        "category": "Category B",
                        "value": 3.43,
                        "percentage": 13.1
                },
                {
                        "category": "Category C",
                        "value": 2.97,
                        "percentage": 11.4
                },
                {
                        "category": "Category D",
                        "value": 1.46,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 10.5,
                        "percentage": 40.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.398694",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Days of Inventory"
        }
    },
}
