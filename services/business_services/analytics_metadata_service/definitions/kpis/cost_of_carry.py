"""
Cost of Carry

The cost associated with holding inventory, including storage, insurance, and taxes.
"""

COST_OF_CARRY = {
    "code": "COST_OF_CARRY",
    "name": "Cost of Carry",
    "description": "The cost associated with holding inventory, including storage, insurance, and taxes.",
    "formula": "Total Carrying Costs / Average Inventory Value",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost of Carry to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.723761"},
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
                        19381.44,
                        18608.49,
                        7395.45,
                        11097.17,
                        15440.3,
                        20396.98,
                        12378.78,
                        10266.16,
                        9576.91,
                        18826.77,
                        12803.66,
                        13259.84
                ],
                "unit": "$"
        },
        "current": {
                "value": 13259.84,
                "unit": "$",
                "change": 456.18,
                "change_percent": 3.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 14119.33,
                "min": 7395.45,
                "max": 20396.98,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 3863.16,
                        "percentage": 29.1
                },
                {
                        "category": "Segment B",
                        "value": 3016.87,
                        "percentage": 22.8
                },
                {
                        "category": "Segment C",
                        "value": 1677.58,
                        "percentage": 12.7
                },
                {
                        "category": "Segment D",
                        "value": 1075.72,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 3626.51,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.524981",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost of Carry"
        }
    },
}
