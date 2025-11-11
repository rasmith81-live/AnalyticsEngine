"""
Internal Order Cycle Time

The time it takes for the internal warehouse process from order receipt to shipment.
"""

INTERNAL_ORDER_CYCLE_TIME = {
    "code": "INTERNAL_ORDER_CYCLE_TIME",
    "name": "Internal Order Cycle Time",
    "description": "The time it takes for the internal warehouse process from order receipt to shipment.",
    "formula": "Total Time for Internal Order Fulfillment / Total Number of Internal Orders",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Internal Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Shipment", "Warehouse"], "last_validated": "2025-11-10T13:49:32.979047"},
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
                        265,
                        272,
                        273,
                        278,
                        249,
                        286,
                        279,
                        284,
                        262,
                        258,
                        253,
                        285
                ],
                "unit": "count"
        },
        "current": {
                "value": 285,
                "unit": "count",
                "change": 32,
                "change_percent": 12.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 270.33,
                "min": 249,
                "max": 286,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 61.51,
                        "percentage": 21.6
                },
                {
                        "category": "Category B",
                        "value": 64.49,
                        "percentage": 22.6
                },
                {
                        "category": "Category C",
                        "value": 48.58,
                        "percentage": 17.0
                },
                {
                        "category": "Category D",
                        "value": 24.53,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 85.89,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.533270",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Internal Order Cycle Time"
        }
    },
}
