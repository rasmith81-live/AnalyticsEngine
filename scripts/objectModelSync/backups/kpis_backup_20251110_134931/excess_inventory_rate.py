"""
Excess Inventory Rate

The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.
"""

EXCESS_INVENTORY_RATE = {
    "code": "EXCESS_INVENTORY_RATE",
    "name": "Excess Inventory Rate",
    "description": "The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Excess Inventory Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.479707"},
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
                        45.68,
                        49.26,
                        47.72,
                        41.06,
                        48.42,
                        53.83,
                        55.82,
                        56.48,
                        55.46,
                        47.8,
                        50.13,
                        39.6
                ],
                "unit": "%"
        },
        "current": {
                "value": 39.6,
                "unit": "%",
                "change": -10.53,
                "change_percent": -21.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 49.27,
                "min": 39.6,
                "max": 56.48,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11.44,
                        "percentage": 28.9
                },
                {
                        "category": "Category B",
                        "value": 8.61,
                        "percentage": 21.7
                },
                {
                        "category": "Category C",
                        "value": 3.59,
                        "percentage": 9.1
                },
                {
                        "category": "Category D",
                        "value": 2.35,
                        "percentage": 5.9
                },
                {
                        "category": "Other",
                        "value": 13.61,
                        "percentage": 34.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.479707",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Excess Inventory Rate"
        }
    },
}
