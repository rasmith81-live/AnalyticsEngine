"""
Supplier Security Incident Rate

The frequency of security incidents originating from suppliers, indicating the security performance of upstream supply chain partners.
"""

SUPPLIER_SECURITY_INCIDENT_RATE = {
    "code": "SUPPLIER_SECURITY_INCIDENT_RATE",
    "name": "Supplier Security Incident Rate",
    "description": "The frequency of security incidents originating from suppliers, indicating the security performance of upstream supply chain partners.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Security Incident Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.655771"},
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
                        63.09,
                        58.34,
                        70.73,
                        58.49,
                        63.54,
                        72.39,
                        59.18,
                        68.1,
                        73.08,
                        58.44,
                        65.28,
                        69.6
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.6,
                "unit": "%",
                "change": 4.32,
                "change_percent": 6.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.02,
                "min": 58.34,
                "max": 73.08,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.55,
                        "percentage": 32.4
                },
                {
                        "category": "Category B",
                        "value": 10.16,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 7.25,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 4.56,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 25.08,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.894491",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Security Incident Rate"
        }
    },
}
