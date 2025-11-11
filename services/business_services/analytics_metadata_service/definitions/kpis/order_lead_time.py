"""
Order Lead Time

The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.
"""

ORDER_LEAD_TIME = {
    "code": "ORDER_LEAD_TIME",
    "name": "Order Lead Time",
    "description": "The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.",
    "formula": "Total Time from Order Placement to Delivery / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Lead Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Delivery", "Inventory", "Lead", "Order"], "last_validated": "2025-11-10T13:49:33.120713"},
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
                        308,
                        301,
                        299,
                        322,
                        312,
                        311,
                        322,
                        303,
                        298,
                        314,
                        328,
                        286
                ],
                "unit": "count"
        },
        "current": {
                "value": 286,
                "unit": "count",
                "change": -42,
                "change_percent": -12.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 308.67,
                "min": 286,
                "max": 328,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 47.08,
                        "percentage": 16.5
                },
                {
                        "category": "Segment B",
                        "value": 76.38,
                        "percentage": 26.7
                },
                {
                        "category": "Segment C",
                        "value": 45.02,
                        "percentage": 15.7
                },
                {
                        "category": "Segment D",
                        "value": 31.58,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 85.94,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.315494",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Order Lead Time"
        }
    },
}
