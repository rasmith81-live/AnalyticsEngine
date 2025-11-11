"""
Shipping Accuracy

The percentage of shipments that are correct per the shipping documentation.
"""

SHIPPING_ACCURACY = {
    "code": "SHIPPING_ACCURACY",
    "name": "Shipping Accuracy",
    "description": "The percentage of shipments that are correct per the shipping documentation.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shipping Accuracy to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:43:24.765241"},
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
                        694.05,
                        606.28,
                        624.73,
                        719.51,
                        650.47,
                        674.88,
                        647.05,
                        681.93,
                        623.92,
                        649.1,
                        632.15,
                        671.61
                ],
                "unit": "units"
        },
        "current": {
                "value": 671.61,
                "unit": "units",
                "change": 39.46,
                "change_percent": 6.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 656.31,
                "min": 606.28,
                "max": 719.51,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 113.48,
                        "percentage": 16.9
                },
                {
                        "category": "Category B",
                        "value": 162.65,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 110.24,
                        "percentage": 16.4
                },
                {
                        "category": "Category D",
                        "value": 63.99,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 221.25,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.765241",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Shipping Accuracy"
        }
    },
}
