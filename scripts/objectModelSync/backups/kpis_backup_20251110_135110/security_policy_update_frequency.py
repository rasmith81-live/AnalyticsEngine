"""
Security Policy Update Frequency

The frequency with which security policies are reviewed and updated, showing the organization
"""

SECURITY_POLICY_UPDATE_FREQUENCY = {
    "code": "SECURITY_POLICY_UPDATE_FREQUENCY",
    "name": "Security Policy Update Frequency",
    "description": "The frequency with which security policies are reviewed and updated, showing the organization",
    "formula": "Total Number of Security Policy Updates / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Policy Update Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.557536"},
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
                        84,
                        71,
                        53,
                        82,
                        45,
                        65,
                        52,
                        42,
                        68,
                        43,
                        42,
                        78
                ],
                "unit": "count"
        },
        "current": {
                "value": 78,
                "unit": "count",
                "change": 36,
                "change_percent": 85.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 60.42,
                "min": 42,
                "max": 84,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.26,
                        "percentage": 15.7
                },
                {
                        "category": "Category B",
                        "value": 12.29,
                        "percentage": 15.8
                },
                {
                        "category": "Category C",
                        "value": 10.71,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 5.92,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 36.82,
                        "percentage": 47.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.727866",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Security Policy Update Frequency"
        }
    },
}
