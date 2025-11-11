"""
Cost per Shipment

The total cost divided by the number of shipments.
"""

COST_PER_SHIPMENT = {
    "code": "COST_PER_SHIPMENT",
    "name": "Cost per Shipment",
    "description": "The total cost divided by the number of shipments.",
    "formula": "Total Shipping Costs / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Shipment to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:43:23.178622"},
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
                        445,
                        427,
                        430,
                        446,
                        431,
                        424,
                        442,
                        415,
                        450,
                        445,
                        434,
                        449
                ],
                "unit": "count"
        },
        "current": {
                "value": 449,
                "unit": "count",
                "change": 15,
                "change_percent": 3.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 436.5,
                "min": 415,
                "max": 450,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 137.11,
                        "percentage": 30.5
                },
                {
                        "category": "Category B",
                        "value": 91.03,
                        "percentage": 20.3
                },
                {
                        "category": "Category C",
                        "value": 47.36,
                        "percentage": 10.5
                },
                {
                        "category": "Category D",
                        "value": 38.98,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 134.52,
                        "percentage": 30.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.178622",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Shipment"
        }
    },
}
