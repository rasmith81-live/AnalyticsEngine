"""
Time to Ship

The time it takes from receiving an order to shipping it out.
"""

TIME_TO_SHIP = {
    "code": "TIME_TO_SHIP",
    "name": "Time to Ship",
    "description": "The time it takes from receiving an order to shipping it out.",
    "formula": "Total Time Taken for Shipping / Total Number of Orders Shipped",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Ship to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.723833"},
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
                        97,
                        108,
                        89,
                        69,
                        99,
                        114,
                        114,
                        83,
                        77,
                        94,
                        88,
                        118
                ],
                "unit": "count"
        },
        "current": {
                "value": 118,
                "unit": "count",
                "change": 30,
                "change_percent": 34.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 95.83,
                "min": 69,
                "max": 118,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.37,
                        "percentage": 15.6
                },
                {
                        "category": "Segment B",
                        "value": 26.85,
                        "percentage": 22.8
                },
                {
                        "category": "Segment C",
                        "value": 20.15,
                        "percentage": 17.1
                },
                {
                        "category": "Segment D",
                        "value": 15.77,
                        "percentage": 13.4
                },
                {
                        "category": "Other",
                        "value": 36.86,
                        "percentage": 31.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.796706",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Ship"
        }
    },
}
