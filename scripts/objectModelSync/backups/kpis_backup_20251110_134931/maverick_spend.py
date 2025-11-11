"""
Maverick Spend

The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.
"""

MAVERICK_SPEND = {
    "code": "MAVERICK_SPEND",
    "name": "Maverick Spend",
    "description": "The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.",
    "formula": "Total Maverick Spend / Total Spend",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Maverick Spend to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Contract", "Supplier"], "last_validated": "2025-11-10T13:43:23.651166"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        918.25,
                        838.7,
                        802.92,
                        875.28,
                        873.77,
                        878.37,
                        851.3,
                        838.53,
                        829.03,
                        826.54,
                        893.76,
                        846.94
                ],
                "unit": "units"
        },
        "current": {
                "value": 846.94,
                "unit": "units",
                "change": -46.82,
                "change_percent": -5.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 856.12,
                "min": 802.92,
                "max": 918.25,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 286.84,
                        "percentage": 33.9
                },
                {
                        "category": "Category B",
                        "value": 129.17,
                        "percentage": 15.3
                },
                {
                        "category": "Category C",
                        "value": 82.73,
                        "percentage": 9.8
                },
                {
                        "category": "Category D",
                        "value": 41.2,
                        "percentage": 4.9
                },
                {
                        "category": "Other",
                        "value": 307.0,
                        "percentage": 36.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.651166",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Maverick Spend"
        }
    },
}
