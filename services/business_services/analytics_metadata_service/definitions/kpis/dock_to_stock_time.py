"""
Dock to Stock Time

The time it takes for goods to move from the receiving dock to available inventory.
"""

DOCK_TO_STOCK_TIME = {
    "code": "DOCK_TO_STOCK_TIME",
    "name": "Dock to Stock Time",
    "description": "The time it takes for goods to move from the receiving dock to available inventory.",
    "formula": "Total Dock to Stock Time / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Dock to Stock Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Shipment"], "last_validated": "2025-11-10T13:49:32.934187"},
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
                        95,
                        80,
                        86,
                        101,
                        104,
                        83,
                        101,
                        69,
                        71,
                        85,
                        71,
                        115
                ],
                "unit": "count"
        },
        "current": {
                "value": 115,
                "unit": "count",
                "change": 44,
                "change_percent": 62.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 88.42,
                "min": 69,
                "max": 115,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 25.54,
                        "percentage": 22.2
                },
                {
                        "category": "Segment B",
                        "value": 23.39,
                        "percentage": 20.3
                },
                {
                        "category": "Segment C",
                        "value": 13.46,
                        "percentage": 11.7
                },
                {
                        "category": "Segment D",
                        "value": 6.32,
                        "percentage": 5.5
                },
                {
                        "category": "Other",
                        "value": 46.29,
                        "percentage": 40.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.937432",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Dock to Stock Time"
        }
    },
}
