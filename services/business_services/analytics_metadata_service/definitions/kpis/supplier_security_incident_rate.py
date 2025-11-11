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
                        77.95,
                        72.64,
                        71.82,
                        83.08,
                        65.99,
                        70.92,
                        66.3,
                        71.4,
                        65.97,
                        64.95,
                        69.61,
                        72.83
                ],
                "unit": "%"
        },
        "current": {
                "value": 72.83,
                "unit": "%",
                "change": 3.22,
                "change_percent": 4.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 71.12,
                "min": 64.95,
                "max": 83.08,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.41,
                        "percentage": 15.7
                },
                {
                        "category": "Segment B",
                        "value": 21.32,
                        "percentage": 29.3
                },
                {
                        "category": "Segment C",
                        "value": 12.47,
                        "percentage": 17.1
                },
                {
                        "category": "Segment D",
                        "value": 7.02,
                        "percentage": 9.6
                },
                {
                        "category": "Other",
                        "value": 20.61,
                        "percentage": 28.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.606376",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Security Incident Rate"
        }
    },
}
