"""
Transportation Cost per Unit Shipped

The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.
"""

TRANSPORTATION_COST_PER_UNIT_SHIPPED = {
    "code": "TRANSPORTATION_COST_PER_UNIT_SHIPPED",
    "name": "Transportation Cost per Unit Shipped",
    "description": "The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.",
    "formula": "Total Transportation Costs / Total Units Shipped",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Cost per Unit Shipped to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:25.144704"},
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
                        67238.6,
                        71699.91,
                        62684.96,
                        68298.87,
                        68055.13,
                        64758.48,
                        73247.25,
                        69510.69,
                        71664.22,
                        65188.77,
                        63475.64,
                        63893.36
                ],
                "unit": "$"
        },
        "current": {
                "value": 63893.36,
                "unit": "$",
                "change": 417.72,
                "change_percent": 0.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 67476.32,
                "min": 62684.96,
                "max": 73247.25,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12377.29,
                        "percentage": 19.4
                },
                {
                        "category": "Category B",
                        "value": 7904.47,
                        "percentage": 12.4
                },
                {
                        "category": "Category C",
                        "value": 15220.26,
                        "percentage": 23.8
                },
                {
                        "category": "Category D",
                        "value": 6025.19,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 22366.15,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.144704",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Transportation Cost per Unit Shipped"
        }
    },
}
