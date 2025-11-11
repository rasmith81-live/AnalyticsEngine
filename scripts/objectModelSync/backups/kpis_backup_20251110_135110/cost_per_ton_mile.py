"""
Cost per Ton-Mile

The cost to transport one ton of material one mile.
"""

COST_PER_TON_MILE = {
    "code": "COST_PER_TON_MILE",
    "name": "Cost per Ton-Mile",
    "description": "The cost to transport one ton of material one mile.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Ton-Mile to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:32.734430"},
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
                        54760.35,
                        51899.36,
                        50350.22,
                        54669.5,
                        56030.26,
                        47748.74,
                        53033.6,
                        45863.18,
                        52485.23,
                        48900.31,
                        55448.5,
                        53795.61
                ],
                "unit": "$"
        },
        "current": {
                "value": 53795.61,
                "unit": "$",
                "change": -1652.89,
                "change_percent": -3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 52082.07,
                "min": 45863.18,
                "max": 56030.26,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15546.81,
                        "percentage": 28.9
                },
                {
                        "category": "Category B",
                        "value": 12300.4,
                        "percentage": 22.9
                },
                {
                        "category": "Category C",
                        "value": 7200.66,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 2833.37,
                        "percentage": 5.3
                },
                {
                        "category": "Other",
                        "value": 15914.37,
                        "percentage": 29.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.180832",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost per Ton-Mile"
        }
    },
}
