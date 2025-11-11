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
                        21584.44,
                        29238.34,
                        18707.48,
                        26048.34,
                        24054.7,
                        24761.51,
                        24218.77,
                        28013.19,
                        26033.45,
                        23189.03,
                        26244.82,
                        16853.36
                ],
                "unit": "$"
        },
        "current": {
                "value": 16853.36,
                "unit": "$",
                "change": -9391.46,
                "change_percent": -35.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 24078.95,
                "min": 16853.36,
                "max": 29238.34,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 5510.5,
                        "percentage": 32.7
                },
                {
                        "category": "Segment B",
                        "value": 1797.0,
                        "percentage": 10.7
                },
                {
                        "category": "Segment C",
                        "value": 2124.26,
                        "percentage": 12.6
                },
                {
                        "category": "Segment D",
                        "value": 1464.05,
                        "percentage": 8.7
                },
                {
                        "category": "Other",
                        "value": 5957.55,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.413622",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Material Cost Variability"
        }
    },
}
