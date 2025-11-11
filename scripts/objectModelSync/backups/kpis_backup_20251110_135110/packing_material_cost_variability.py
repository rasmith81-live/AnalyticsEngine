"""
Packing Material Cost Variability

The fluctuation in the cost of packing materials over time, affecting budgeting and cost management.
"""

PACKING_MATERIAL_COST_VARIABILITY = {
    "code": "PACKING_MATERIAL_COST_VARIABILITY",
    "name": "Packing Material Cost Variability",
    "description": "The fluctuation in the cost of packing materials over time, affecting budgeting and cost management.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Material Cost Variability to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.165984"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        90248.54,
                        85932.44,
                        85070.42,
                        79601.8,
                        91955.29,
                        80026.68,
                        88314.82,
                        92114.98,
                        80377.29,
                        86401.82,
                        83718.63,
                        78977.44
                ],
                "unit": "$"
        },
        "current": {
                "value": 78977.44,
                "unit": "$",
                "change": -4741.19,
                "change_percent": -5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 85228.35,
                "min": 78977.44,
                "max": 92114.98,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13819.3,
                        "percentage": 17.5
                },
                {
                        "category": "Category B",
                        "value": 16004.38,
                        "percentage": 20.3
                },
                {
                        "category": "Category C",
                        "value": 8245.8,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 6116.49,
                        "percentage": 7.7
                },
                {
                        "category": "Other",
                        "value": 34791.47,
                        "percentage": 44.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.825673",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Material Cost Variability"
        }
    },
}
