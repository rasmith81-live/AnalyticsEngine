"""
Picking Productivity

The rate at which items are picked and processed for orders.
"""

PICKING_PRODUCTIVITY = {
    "code": "PICKING_PRODUCTIVITY",
    "name": "Picking Productivity",
    "description": "The rate at which items are picked and processed for orders.",
    "formula": "Total Items Picked / Total Picking Hours",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Picking Productivity to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:49:33.236933"},
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
                        332.65,
                        436.04,
                        420.04,
                        308.81,
                        423.23,
                        397.24,
                        329.97,
                        410.75,
                        377.78,
                        387.1,
                        377.48,
                        410.23
                ],
                "unit": "units"
        },
        "current": {
                "value": 410.23,
                "unit": "units",
                "change": 32.75,
                "change_percent": 8.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 384.28,
                "min": 308.81,
                "max": 436.04,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 80.16,
                        "percentage": 19.5
                },
                {
                        "category": "Product Line B",
                        "value": 85.71,
                        "percentage": 20.9
                },
                {
                        "category": "Product Line C",
                        "value": 73.77,
                        "percentage": 18.0
                },
                {
                        "category": "Services",
                        "value": 21.82,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 148.77,
                        "percentage": 36.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.562044",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Picking Productivity"
        }
    },
}
