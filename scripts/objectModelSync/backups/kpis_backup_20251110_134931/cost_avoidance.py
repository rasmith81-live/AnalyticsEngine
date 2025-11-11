"""
Cost Avoidance

The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.
"""

COST_AVOIDANCE = {
    "code": "COST_AVOIDANCE",
    "name": "Cost Avoidance",
    "description": "The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.",
    "formula": "Projected Cost without Procurement Intervention - Actual Cost Post-Intervention",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost Avoidance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.155290"},
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
                        109239.23,
                        104186.6,
                        105272.77,
                        99020.06,
                        96288.02,
                        104624.76,
                        96569.61,
                        100268.76,
                        108848.77,
                        105497.07,
                        104177.2,
                        99653.64
                ],
                "unit": "$"
        },
        "current": {
                "value": 99653.64,
                "unit": "$",
                "change": -4523.56,
                "change_percent": -4.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 102803.87,
                "min": 96288.02,
                "max": 109239.23,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16323.6,
                        "percentage": 16.4
                },
                {
                        "category": "Category B",
                        "value": 16933.24,
                        "percentage": 17.0
                },
                {
                        "category": "Category C",
                        "value": 13308.85,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 7687.69,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 45400.26,
                        "percentage": 45.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.155290",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost Avoidance"
        }
    },
}
