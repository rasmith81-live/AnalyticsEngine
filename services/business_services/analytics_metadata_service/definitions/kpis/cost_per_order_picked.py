"""
Cost per Order Picked

The cost associated with picking each order.
"""

COST_PER_ORDER_PICKED = {
    "code": "COST_PER_ORDER_PICKED",
    "name": "Cost per Order Picked",
    "description": "The cost associated with picking each order.",
    "formula": "Total Picking Costs / Total Number of Orders Picked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Order Picked to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:32.730408"},
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
                        301,
                        286,
                        303,
                        306,
                        305,
                        286,
                        280,
                        272,
                        292,
                        263,
                        264,
                        269
                ],
                "unit": "count"
        },
        "current": {
                "value": 269,
                "unit": "count",
                "change": 5,
                "change_percent": 1.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 285.58,
                "min": 263,
                "max": 306,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 49.87,
                        "percentage": 18.5
                },
                {
                        "category": "Segment B",
                        "value": 68.89,
                        "percentage": 25.6
                },
                {
                        "category": "Segment C",
                        "value": 49.76,
                        "percentage": 18.5
                },
                {
                        "category": "Segment D",
                        "value": 29.27,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 71.21,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.543467",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Order Picked"
        }
    },
}
