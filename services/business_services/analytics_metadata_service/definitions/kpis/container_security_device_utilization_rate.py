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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.710661"},
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
                        60.74,
                        77.2,
                        64.29,
                        67.7,
                        67.17,
                        73.34,
                        66.01,
                        73.99,
                        75.83,
                        76.18,
                        64.93,
                        69.61
                ],
                "unit": "%"
        },
        "current": {
                "value": 69.61,
                "unit": "%",
                "change": 4.68,
                "change_percent": 7.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.75,
                "min": 60.74,
                "max": 77.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.45,
                        "percentage": 30.8
                },
                {
                        "category": "Segment B",
                        "value": 14.47,
                        "percentage": 20.8
                },
                {
                        "category": "Segment C",
                        "value": 8.49,
                        "percentage": 12.2
                },
                {
                        "category": "Segment D",
                        "value": 5.64,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 19.56,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.504162",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Container Security Device Utilization Rate"
        }
    },
}
