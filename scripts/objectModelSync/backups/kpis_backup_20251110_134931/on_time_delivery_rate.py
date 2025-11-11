"""
On-time Delivery Rate

The percentage of shipments that are delivered on time. A higher rate indicates more efficient and reliable transportation operations.
"""

ON_TIME_DELIVERY_RATE = {
    "code": "ON_TIME_DELIVERY_RATE",
    "name": "On-time Delivery Rate",
    "description": "The percentage of shipments that are delivered on time. A higher rate indicates more efficient and reliable transportation operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for On-time Delivery Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:43:23.720532"},
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
                        51.99,
                        51.47,
                        45.43,
                        64.7,
                        64.09,
                        46.37,
                        48.75,
                        47.64,
                        49.53,
                        51.71,
                        61.57,
                        51.44
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.44,
                "unit": "%",
                "change": -10.13,
                "change_percent": -16.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 52.89,
                "min": 45.43,
                "max": 64.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.16,
                        "percentage": 15.9
                },
                {
                        "category": "Category B",
                        "value": 14.4,
                        "percentage": 28.0
                },
                {
                        "category": "Category C",
                        "value": 9.7,
                        "percentage": 18.9
                },
                {
                        "category": "Category D",
                        "value": 3.18,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 16.0,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.720532",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Delivery Rate"
        }
    },
}
