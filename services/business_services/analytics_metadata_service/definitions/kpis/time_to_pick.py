"""
Time to Pick

The time it takes to collect items for an order from the warehouse.
"""

TIME_TO_PICK = {
    "code": "TIME_TO_PICK",
    "name": "Time to Pick",
    "description": "The time it takes to collect items for an order from the warehouse.",
    "formula": "Total Time Taken for Picking / Total Number of Orders Picked",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Pick to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product", "Warehouse"], "last_validated": "2025-11-10T13:49:33.718316"},
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
                        342,
                        309,
                        317,
                        318,
                        311,
                        303,
                        308,
                        323,
                        330,
                        338,
                        300,
                        348
                ],
                "unit": "count"
        },
        "current": {
                "value": 348,
                "unit": "count",
                "change": 48,
                "change_percent": 16.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 320.58,
                "min": 300,
                "max": 348,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 86.92,
                        "percentage": 25.0
                },
                {
                        "category": "Segment B",
                        "value": 64.29,
                        "percentage": 18.5
                },
                {
                        "category": "Segment C",
                        "value": 34.34,
                        "percentage": 9.9
                },
                {
                        "category": "Segment D",
                        "value": 48.21,
                        "percentage": 13.9
                },
                {
                        "category": "Other",
                        "value": 114.24,
                        "percentage": 32.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.778270",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Pick"
        }
    },
}
