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
                        27466.74,
                        21775.5,
                        22235.46,
                        22143.75,
                        29175.09,
                        23893.12,
                        17988.13,
                        25447.49,
                        23716.2,
                        31994.62,
                        20117.43,
                        30100.66
                ],
                "unit": "$"
        },
        "current": {
                "value": 30100.66,
                "unit": "$",
                "change": 9983.23,
                "change_percent": 49.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 24671.18,
                "min": 17988.13,
                "max": 31994.62,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 6093.68,
                        "percentage": 20.2
                },
                {
                        "category": "Segment B",
                        "value": 4477.03,
                        "percentage": 14.9
                },
                {
                        "category": "Segment C",
                        "value": 4994.19,
                        "percentage": 16.6
                },
                {
                        "category": "Segment D",
                        "value": 2388.34,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 12147.42,
                        "percentage": 40.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.553294",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Cost per Ton-Mile"
        }
    },
}
