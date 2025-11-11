"""
Supplier Compliance Rate

The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.
"""

SUPPLIER_COMPLIANCE_RATE = {
    "code": "SUPPLIER_COMPLIANCE_RATE",
    "name": "Supplier Compliance Rate",
    "description": "The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Compliance Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:43:24.843115"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        49.06,
                        39.06,
                        47.2,
                        39.51,
                        39.57,
                        46.63,
                        31.89,
                        43.94,
                        45.3,
                        39.36,
                        39.35,
                        50.22
                ],
                "unit": "%"
        },
        "current": {
                "value": 50.22,
                "unit": "%",
                "change": 10.87,
                "change_percent": 27.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 42.59,
                "min": 31.89,
                "max": 50.22,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.32,
                        "percentage": 30.5
                },
                {
                        "category": "Category B",
                        "value": 10.93,
                        "percentage": 21.8
                },
                {
                        "category": "Category C",
                        "value": 4.85,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 3.68,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 15.44,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.843115",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Compliance Rate"
        }
    },
}
