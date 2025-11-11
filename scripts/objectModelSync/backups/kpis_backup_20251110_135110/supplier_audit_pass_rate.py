"""
Supplier Audit Pass Rate

The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.
"""

SUPPLIER_AUDIT_PASS_RATE = {
    "code": "SUPPLIER_AUDIT_PASS_RATE",
    "name": "Supplier Audit Pass Rate",
    "description": "The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Audit Pass Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.614309"},
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
                        63.01,
                        69.89,
                        52.86,
                        70.11,
                        61.88,
                        62.57,
                        58.84,
                        64.63,
                        53.35,
                        58.39,
                        70.59,
                        67.45
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.45,
                "unit": "%",
                "change": -3.14,
                "change_percent": -4.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 62.8,
                "min": 52.86,
                "max": 70.59,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.5,
                        "percentage": 15.6
                },
                {
                        "category": "Category B",
                        "value": 12.09,
                        "percentage": 17.9
                },
                {
                        "category": "Category C",
                        "value": 11.57,
                        "percentage": 17.2
                },
                {
                        "category": "Category D",
                        "value": 5.75,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 27.54,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.830765",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Audit Pass Rate"
        }
    },
}
