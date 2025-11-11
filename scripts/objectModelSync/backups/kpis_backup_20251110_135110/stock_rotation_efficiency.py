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
                        477.82,
                        354.01,
                        375.32,
                        462.52,
                        420.54,
                        360.09,
                        428.74,
                        395.68,
                        449.99,
                        443.42,
                        391.26,
                        381.39
                ],
                "unit": "units"
        },
        "current": {
                "value": 381.39,
                "unit": "units",
                "change": -9.87,
                "change_percent": -2.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 411.73,
                "min": 354.01,
                "max": 477.82,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 121.41,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 80.04,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 60.34,
                        "percentage": 15.8
                },
                {
                        "category": "Category D",
                        "value": 33.15,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 86.45,
                        "percentage": 22.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.795084",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Stock Rotation Efficiency"
        }
    },
}
