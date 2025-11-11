"""
Supply Chain Cost Reduction

The amount of cost savings achieved through efficiency improvements in the supply chain operations.
"""

SUPPLY_CHAIN_COST_REDUCTION = {
    "code": "SUPPLY_CHAIN_COST_REDUCTION",
    "name": "Supply Chain Cost Reduction",
    "description": "The amount of cost savings achieved through efficiency improvements in the supply chain operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Cost Reduction to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.900262"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        17613.26,
                        23160.78,
                        12196.41,
                        13839.67,
                        21165.95,
                        17314.38,
                        26052.87,
                        21437.59,
                        24685.72,
                        14616.61,
                        25377.11,
                        18573.45
                ],
                "unit": "$"
        },
        "current": {
                "value": 18573.45,
                "unit": "$",
                "change": -6803.66,
                "change_percent": -26.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 19669.48,
                "min": 12196.41,
                "max": 26052.87,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 4851.95,
                        "percentage": 26.1
                },
                {
                        "category": "Category B",
                        "value": 3474.97,
                        "percentage": 18.7
                },
                {
                        "category": "Category C",
                        "value": 2400.43,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 1220.77,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 6625.33,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.900262",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Supply Chain Cost Reduction"
        }
    },
}
