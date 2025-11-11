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
                        420,
                        421,
                        450,
                        455,
                        458,
                        444,
                        421,
                        455,
                        464,
                        444,
                        462,
                        450
                ],
                "unit": "count"
        },
        "current": {
                "value": 450,
                "unit": "count",
                "change": -12,
                "change_percent": -2.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 445.33,
                "min": 420,
                "max": 464,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 92.74,
                        "percentage": 20.6
                },
                {
                        "category": "Segment B",
                        "value": 102.59,
                        "percentage": 22.8
                },
                {
                        "category": "Segment C",
                        "value": 53.62,
                        "percentage": 11.9
                },
                {
                        "category": "Segment D",
                        "value": 43.25,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 157.8,
                        "percentage": 35.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.403782",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Backorder Level"
        }
    },
}
