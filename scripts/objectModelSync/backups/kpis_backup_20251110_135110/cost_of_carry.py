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
                        98509.43,
                        92161.69,
                        93809.53,
                        97507.24,
                        101624.7,
                        95291.6,
                        90240.92,
                        93261.49,
                        94738.27,
                        95640.37,
                        95338.29,
                        103999.15
                ],
                "unit": "$"
        },
        "current": {
                "value": 103999.15,
                "unit": "$",
                "change": 8660.86,
                "change_percent": 9.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 96010.22,
                "min": 90240.92,
                "max": 103999.15,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18532.33,
                        "percentage": 17.8
                },
                {
                        "category": "Category B",
                        "value": 29240.75,
                        "percentage": 28.1
                },
                {
                        "category": "Category C",
                        "value": 18368.95,
                        "percentage": 17.7
                },
                {
                        "category": "Category D",
                        "value": 7086.24,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 30770.88,
                        "percentage": 29.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.157797",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost of Carry"
        }
    },
}
