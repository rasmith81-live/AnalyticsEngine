"""
Backorder Level

The amount of orders that cannot be filled from current inventory.
"""

BACKORDER_LEVEL = {
    "code": "BACKORDER_LEVEL",
    "name": "Backorder Level",
    "description": "The amount of orders that cannot be filled from current inventory.",
    "formula": "Total Number of Backordered Items",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Backorder Level to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Order", "Product"], "last_validated": "2025-11-10T13:49:32.664237"},
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
                        118,
                        112,
                        117,
                        125,
                        121,
                        106,
                        112,
                        101,
                        135,
                        129,
                        88,
                        131
                ],
                "unit": "count"
        },
        "current": {
                "value": 131,
                "unit": "count",
                "change": 43,
                "change_percent": 48.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 116.25,
                "min": 88,
                "max": 135,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 32.77,
                        "percentage": 25.0
                },
                {
                        "category": "Category B",
                        "value": 32.99,
                        "percentage": 25.2
                },
                {
                        "category": "Category C",
                        "value": 19.82,
                        "percentage": 15.1
                },
                {
                        "category": "Category D",
                        "value": 12.07,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 33.35,
                        "percentage": 25.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.054229",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Backorder Level"
        }
    },
}
