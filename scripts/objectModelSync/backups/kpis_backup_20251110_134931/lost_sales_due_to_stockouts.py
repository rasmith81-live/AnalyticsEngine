"""
Lost Sales Due to Stockouts

The estimated sales lost due to items being out of stock.
"""

LOST_SALES_DUE_TO_STOCKOUTS = {
    "code": "LOST_SALES_DUE_TO_STOCKOUTS",
    "name": "Lost Sales Due to Stockouts",
    "description": "The estimated sales lost due to items being out of stock.",
    "formula": "Estimated Sales Value of Stockout Items",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lost Sales Due to Stockouts to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:43:23.629025"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        211.4,
                        291.12,
                        240.39,
                        189.92,
                        220.15,
                        222.5,
                        187.41,
                        317.89,
                        203.73,
                        298.19,
                        215.56,
                        281.11
                ],
                "unit": "units"
        },
        "current": {
                "value": 281.11,
                "unit": "units",
                "change": 65.55,
                "change_percent": 30.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 239.95,
                "min": 187.41,
                "max": 317.89,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 56.36,
                        "percentage": 20.0
                },
                {
                        "category": "Category B",
                        "value": 35.62,
                        "percentage": 12.7
                },
                {
                        "category": "Category C",
                        "value": 60.91,
                        "percentage": 21.7
                },
                {
                        "category": "Category D",
                        "value": 25.49,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 102.73,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.629025",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Lost Sales Due to Stockouts"
        }
    },
}
