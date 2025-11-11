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
                        82517.76,
                        77299.96,
                        82691.47,
                        76344.86,
                        82793.21,
                        76968.01,
                        73184.42,
                        84793.81,
                        81930.36,
                        70654.0,
                        73961.47,
                        75326.07
                ],
                "unit": "$"
        },
        "current": {
                "value": 75326.07,
                "unit": "$",
                "change": 1364.6,
                "change_percent": 1.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 78205.45,
                "min": 70654.0,
                "max": 84793.81,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12936.77,
                        "percentage": 17.2
                },
                {
                        "category": "Category B",
                        "value": 16361.3,
                        "percentage": 21.7
                },
                {
                        "category": "Category C",
                        "value": 10339.45,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 6914.8,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 28773.75,
                        "percentage": 38.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.574194",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Labor Cost per Picking Hour"
        }
    },
}
