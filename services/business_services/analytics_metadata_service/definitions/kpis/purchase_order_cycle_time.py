"""
Purchase Order Cycle Time

The total time taken from the creation of a purchase order to the receipt of the goods or services ordered.
"""

PURCHASE_ORDER_CYCLE_TIME = {
    "code": "PURCHASE_ORDER_CYCLE_TIME",
    "name": "Purchase Order Cycle Time",
    "description": "The total time taken from the creation of a purchase order to the receipt of the goods or services ordered.",
    "formula": "Total Time for All Purchase Orders / Number of Purchase Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Purchase Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.297909"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        229,
                        210,
                        240,
                        210,
                        228,
                        231,
                        221,
                        246,
                        216,
                        255,
                        254,
                        252
                ],
                "unit": "count"
        },
        "current": {
                "value": 252,
                "unit": "count",
                "change": -2,
                "change_percent": -0.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 232.67,
                "min": 210,
                "max": 255,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 49.33,
                        "percentage": 19.6
                },
                {
                        "category": "Segment B",
                        "value": 40.66,
                        "percentage": 16.1
                },
                {
                        "category": "Segment C",
                        "value": 24.87,
                        "percentage": 9.9
                },
                {
                        "category": "Segment D",
                        "value": 39.71,
                        "percentage": 15.8
                },
                {
                        "category": "Other",
                        "value": 97.43,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.699806",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Purchase Order Cycle Time"
        }
    },
}
