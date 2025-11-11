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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.011924"},
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
                        422,
                        404,
                        399,
                        414,
                        417,
                        396,
                        382,
                        375,
                        377,
                        380,
                        418,
                        391
                ],
                "unit": "count"
        },
        "current": {
                "value": 391,
                "unit": "count",
                "change": -27,
                "change_percent": -6.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 397.92,
                "min": 375,
                "max": 422,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 132.97,
                        "percentage": 34.0
                },
                {
                        "category": "Category B",
                        "value": 44.43,
                        "percentage": 11.4
                },
                {
                        "category": "Category C",
                        "value": 48.86,
                        "percentage": 12.5
                },
                {
                        "category": "Category D",
                        "value": 26.54,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 138.2,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.011924",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Purchase Order Cycle Time"
        }
    },
}
