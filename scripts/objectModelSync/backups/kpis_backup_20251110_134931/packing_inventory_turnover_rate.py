"""
Packing Inventory Turnover Rate

The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.
"""

PACKING_INVENTORY_TURNOVER_RATE = {
    "code": "PACKING_INVENTORY_TURNOVER_RATE",
    "name": "Packing Inventory Turnover Rate",
    "description": "The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.",
    "formula": "Total Packing Materials Used / Average Packing Inventory",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Inventory Turnover Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:43:23.817056"},
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
                        44.11,
                        55.54,
                        54.23,
                        61.42,
                        44.88,
                        57.74,
                        43.16,
                        55.33,
                        60.65,
                        48.14,
                        53.15,
                        47.12
                ],
                "unit": "%"
        },
        "current": {
                "value": 47.12,
                "unit": "%",
                "change": -6.03,
                "change_percent": -11.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.12,
                "min": 43.16,
                "max": 61.42,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.25,
                        "percentage": 26.0
                },
                {
                        "category": "Category B",
                        "value": 7.63,
                        "percentage": 16.2
                },
                {
                        "category": "Category C",
                        "value": 4.88,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 6.22,
                        "percentage": 13.2
                },
                {
                        "category": "Other",
                        "value": 16.14,
                        "percentage": 34.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.817056",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Packing Inventory Turnover Rate"
        }
    },
}
