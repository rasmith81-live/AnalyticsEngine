"""
Carrier Compliance Rate

The percentage of deliveries that comply with the carrier’s requirements and standards.
"""

CARRIER_COMPLIANCE_RATE = {
    "code": "CARRIER_COMPLIANCE_RATE",
    "name": "Carrier Compliance Rate",
    "description": "The percentage of deliveries that comply with the carrier\u2019s requirements and standards.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Carrier Compliance Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.674414"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        68.04,
                        79.8,
                        67.33,
                        69.87,
                        73.1,
                        81.01,
                        83.34,
                        73.51,
                        77.29,
                        81.7,
                        83.02,
                        84.95
                ],
                "unit": "%"
        },
        "current": {
                "value": 84.95,
                "unit": "%",
                "change": 1.93,
                "change_percent": 2.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 76.91,
                "min": 67.33,
                "max": 84.95,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.39,
                        "percentage": 24.0
                },
                {
                        "category": "Category B",
                        "value": 19.39,
                        "percentage": 22.8
                },
                {
                        "category": "Category C",
                        "value": 11.56,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 8.99,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 24.62,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.073122",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Carrier Compliance Rate"
        }
    },
}
