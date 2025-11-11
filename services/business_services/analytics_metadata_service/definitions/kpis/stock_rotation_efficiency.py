"""
Stock Rotation Efficiency

The effectiveness of inventory management practices in rotating stock before it becomes outdated or expires.
"""

STOCK_ROTATION_EFFICIENCY = {
    "code": "STOCK_ROTATION_EFFICIENCY",
    "name": "Stock Rotation Efficiency",
    "description": "The effectiveness of inventory management practices in rotating stock before it becomes outdated or expires.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stock Rotation Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:33.590627"},
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
                        992.46,
                        858.97,
                        914.85,
                        859.64,
                        915.54,
                        951.46,
                        969.99,
                        1004.26,
                        968.84,
                        975.67,
                        917.44,
                        961.95
                ],
                "unit": "units"
        },
        "current": {
                "value": 961.95,
                "unit": "units",
                "change": 44.51,
                "change_percent": 4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 940.92,
                "min": 858.97,
                "max": 1004.26,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 328.32,
                        "percentage": 34.1
                },
                {
                        "category": "Segment B",
                        "value": 116.62,
                        "percentage": 12.1
                },
                {
                        "category": "Segment C",
                        "value": 114.69,
                        "percentage": 11.9
                },
                {
                        "category": "Segment D",
                        "value": 68.04,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 334.28,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.430206",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Stock Rotation Efficiency"
        }
    },
}
