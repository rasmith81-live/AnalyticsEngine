"""
Cost Savings

The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.
"""

COST_SAVINGS = {
    "code": "COST_SAVINGS",
    "name": "Cost Savings",
    "description": "The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.",
    "formula": "Baseline Spend - Current Spend",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost Savings to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.183063"},
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
                        31052.39,
                        31344.59,
                        27436.96,
                        31678.66,
                        27550.41,
                        40800.27,
                        35981.32,
                        41456.49,
                        41245.87,
                        36719.48,
                        28140.5,
                        30508.71
                ],
                "unit": "$"
        },
        "current": {
                "value": 30508.71,
                "unit": "$",
                "change": 2368.21,
                "change_percent": 8.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 33659.64,
                "min": 27436.96,
                "max": 41456.49,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9106.54,
                        "percentage": 29.8
                },
                {
                        "category": "Category B",
                        "value": 4240.88,
                        "percentage": 13.9
                },
                {
                        "category": "Category C",
                        "value": 4999.37,
                        "percentage": 16.4
                },
                {
                        "category": "Category D",
                        "value": 1406.81,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 10755.11,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.183063",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost Savings"
        }
    },
}
