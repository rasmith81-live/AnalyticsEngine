"""
Claims Percentage

The percentage of shipments that result in claims for loss or damage.
"""

CLAIMS_PERCENTAGE = {
    "code": "CLAIMS_PERCENTAGE",
    "name": "Claims Percentage",
    "description": "The percentage of shipments that result in claims for loss or damage.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Claims Percentage to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:43:23.112696"},
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
                        66.9,
                        58.93,
                        60.2,
                        73.24,
                        60.12,
                        69.94,
                        66.72,
                        59.14,
                        74.15,
                        69.16,
                        66.44,
                        74.61
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.61,
                "unit": "%",
                "change": 8.17,
                "change_percent": 12.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 66.63,
                "min": 58.93,
                "max": 74.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.19,
                        "percentage": 17.7
                },
                {
                        "category": "Category B",
                        "value": 15.39,
                        "percentage": 20.6
                },
                {
                        "category": "Category C",
                        "value": 8.01,
                        "percentage": 10.7
                },
                {
                        "category": "Category D",
                        "value": 6.33,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 31.69,
                        "percentage": 42.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.112696",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Claims Percentage"
        }
    },
}
