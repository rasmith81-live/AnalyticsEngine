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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.659446"},
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
                        27726.05,
                        28841.77,
                        17284.88,
                        30206.91,
                        30883.12,
                        21516.44,
                        21178.09,
                        20118.43,
                        27656.51,
                        19993.38,
                        18511.48,
                        26353.54
                ],
                "unit": "$"
        },
        "current": {
                "value": 26353.54,
                "unit": "$",
                "change": 7842.06,
                "change_percent": 42.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 24189.22,
                "min": 17284.88,
                "max": 30883.12,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 6520.53,
                        "percentage": 24.7
                },
                {
                        "category": "Segment B",
                        "value": 6150.46,
                        "percentage": 23.3
                },
                {
                        "category": "Segment C",
                        "value": 4444.08,
                        "percentage": 16.9
                },
                {
                        "category": "Segment D",
                        "value": 1055.39,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 8183.08,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.615065",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Supply Chain Cost Reduction"
        }
    },
}
