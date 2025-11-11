"""
Total Order Cycle Time

The total time from when an order is placed until it
"""

ORDER_CYCLE_TIME = {
    "code": "ORDER_CYCLE_TIME",
    "name": "Total Order Cycle Time",
    "description": "The total time from when an order is placed until it",
    "formula": "Sum of Time from Order Placement to Order Delivery / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Total Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Delivery", "Order"], "last_validated": "2025-11-10T13:49:33.114134"},
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
                        310,
                        305,
                        289,
                        270,
                        274,
                        306,
                        297,
                        273,
                        294,
                        306,
                        269,
                        267
                ],
                "unit": "count"
        },
        "current": {
                "value": 267,
                "unit": "count",
                "change": -2,
                "change_percent": -0.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 288.33,
                "min": 267,
                "max": 310,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 66.72,
                        "percentage": 25.0
                },
                {
                        "category": "Segment B",
                        "value": 30.88,
                        "percentage": 11.6
                },
                {
                        "category": "Segment C",
                        "value": 56.0,
                        "percentage": 21.0
                },
                {
                        "category": "Segment D",
                        "value": 13.95,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 99.45,
                        "percentage": 37.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.304684",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Total Order Cycle Time"
        }
    },
}
