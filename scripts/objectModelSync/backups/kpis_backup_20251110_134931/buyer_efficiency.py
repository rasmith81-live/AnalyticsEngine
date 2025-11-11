"""
Buyer Efficiency

The number of purchase orders processed per buyer, indicating the efficiency of the
"""

BUYER_EFFICIENCY = {
    "code": "BUYER_EFFICIENCY",
    "name": "Buyer Efficiency",
    "description": "The number of purchase orders processed per buyer, indicating the efficiency of the",
    "formula": "Total Orders Processed or Cost Savings / Number of Buyers",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Buyer Efficiency to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Employee", "Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.063801"},
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
                        366,
                        372,
                        358,
                        361,
                        390,
                        355,
                        363,
                        396,
                        356,
                        386,
                        369,
                        387
                ],
                "unit": "count"
        },
        "current": {
                "value": 387,
                "unit": "count",
                "change": 18,
                "change_percent": 4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 371.58,
                "min": 355,
                "max": 396,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 95.34,
                        "percentage": 24.6
                },
                {
                        "category": "Category B",
                        "value": 65.25,
                        "percentage": 16.9
                },
                {
                        "category": "Category C",
                        "value": 71.13,
                        "percentage": 18.4
                },
                {
                        "category": "Category D",
                        "value": 38.64,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 116.64,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.063801",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Buyer Efficiency"
        }
    },
}
