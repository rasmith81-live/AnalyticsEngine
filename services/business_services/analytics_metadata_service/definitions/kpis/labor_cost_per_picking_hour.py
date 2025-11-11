"""
Labor Cost per Picking Hour

The labor cost associated with one hour of picking orders.
"""

LABOR_COST_PER_PICKING_HOUR = {
    "code": "LABOR_COST_PER_PICKING_HOUR",
    "name": "Labor Cost per Picking Hour",
    "description": "The labor cost associated with one hour of picking orders.",
    "formula": "Total Labor Costs / Total Picking Hours",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Labor Cost per Picking Hour to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:32.996778"},
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
                        56842.62,
                        59089.28,
                        56336.07,
                        62946.83,
                        69877.34,
                        67084.92,
                        59153.91,
                        69448.68,
                        58760.53,
                        63219.83,
                        70269.17,
                        60769.34
                ],
                "unit": "$"
        },
        "current": {
                "value": 60769.34,
                "unit": "$",
                "change": -9499.83,
                "change_percent": -13.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 62816.54,
                "min": 56336.07,
                "max": 70269.17,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17806.52,
                        "percentage": 29.3
                },
                {
                        "category": "Segment B",
                        "value": 9927.69,
                        "percentage": 16.3
                },
                {
                        "category": "Segment C",
                        "value": 9071.16,
                        "percentage": 14.9
                },
                {
                        "category": "Segment D",
                        "value": 5481.79,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 18482.18,
                        "percentage": 30.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.093992",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Labor Cost per Picking Hour"
        }
    },
}
