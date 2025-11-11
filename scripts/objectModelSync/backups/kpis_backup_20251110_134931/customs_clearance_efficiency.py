"""
Customs Clearance Efficiency

The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.
"""

CUSTOMS_CLEARANCE_EFFICIENCY = {
    "code": "CUSTOMS_CLEARANCE_EFFICIENCY",
    "name": "Customs Clearance Efficiency",
    "description": "The average time it takes for goods to clear customs, reflecting the effectiveness of security procedures in international trade.",
    "formula": "Sum of Customs Clearance Times / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customs Clearance Efficiency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:43:23.391581"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        90,
                        114,
                        99,
                        81,
                        115,
                        79,
                        102,
                        96,
                        85,
                        85,
                        107,
                        83
                ],
                "unit": "count"
        },
        "current": {
                "value": 83,
                "unit": "count",
                "change": -24,
                "change_percent": -22.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 94.67,
                "min": 79,
                "max": 115,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.96,
                        "percentage": 28.9
                },
                {
                        "category": "Category B",
                        "value": 13.27,
                        "percentage": 16.0
                },
                {
                        "category": "Category C",
                        "value": 7.33,
                        "percentage": 8.8
                },
                {
                        "category": "Category D",
                        "value": 8.64,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 29.8,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.391581",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customs Clearance Efficiency"
        }
    },
}
