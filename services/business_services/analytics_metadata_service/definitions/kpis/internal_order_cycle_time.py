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
                        252,
                        261,
                        230,
                        231,
                        237,
                        228,
                        250,
                        266,
                        241,
                        228,
                        239,
                        239
                ],
                "unit": "count"
        },
        "current": {
                "value": 239,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 241.83,
                "min": 228,
                "max": 266,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 41.35,
                        "percentage": 17.3
                },
                {
                        "category": "Segment B",
                        "value": 48.87,
                        "percentage": 20.4
                },
                {
                        "category": "Segment C",
                        "value": 46.33,
                        "percentage": 19.4
                },
                {
                        "category": "Segment D",
                        "value": 17.26,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 85.19,
                        "percentage": 35.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.049483",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Internal Order Cycle Time"
        }
    },
}
