"""
Container Security Device Utilization Rate

The percentage of containers equipped with security devices, indicating the level of technology adoption to enhance shipment security.
"""

CONTAINER_SECURITY_DEVICE_UTILIZATION_RATE = {
    "code": "CONTAINER_SECURITY_DEVICE_UTILIZATION_RATE",
    "name": "Container Security Device Utilization Rate",
    "description": "The percentage of containers equipped with security devices, indicating the level of technology adoption to enhance shipment security.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Container Security Device Utilization Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:43:23.139081"},
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
                        62.0,
                        50.65,
                        61.62,
                        67.75,
                        66.48,
                        58.51,
                        64.75,
                        65.8,
                        63.32,
                        64.2,
                        67.3,
                        67.63
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.63,
                "unit": "%",
                "change": 0.33,
                "change_percent": 0.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.33,
                "min": 50.65,
                "max": 67.75,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.78,
                        "percentage": 18.9
                },
                {
                        "category": "Category B",
                        "value": 15.57,
                        "percentage": 23.0
                },
                {
                        "category": "Category C",
                        "value": 8.91,
                        "percentage": 13.2
                },
                {
                        "category": "Category D",
                        "value": 6.06,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 24.31,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.139081",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Container Security Device Utilization Rate"
        }
    },
}
