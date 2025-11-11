"""
Shipment Lead Time

The time it takes for a shipment to be delivered from the time it is ordered. A shorter lead time indicates more efficient transportation operations.
"""

SHIPMENT_LEAD_TIME = {
    "code": "SHIPMENT_LEAD_TIME",
    "name": "Shipment Lead Time",
    "description": "The time it takes for a shipment to be delivered from the time it is ordered. A shorter lead time indicates more efficient transportation operations.",
    "formula": "Average Time from Shipment Ready to Delivery",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shipment Lead Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:43:24.761871"},
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
                        8.2,
                        7.4,
                        11.4,
                        12.5,
                        8.8,
                        6.8,
                        11.1,
                        5.9,
                        8.3,
                        5.9,
                        9.3,
                        13.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 13.0,
                "unit": "days",
                "change": 3.7,
                "change_percent": 39.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 9.05,
                "min": 5.9,
                "max": 13.0,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.41,
                        "percentage": 26.2
                },
                {
                        "category": "Category B",
                        "value": 2.54,
                        "percentage": 19.5
                },
                {
                        "category": "Category C",
                        "value": 1.88,
                        "percentage": 14.5
                },
                {
                        "category": "Category D",
                        "value": 0.97,
                        "percentage": 7.5
                },
                {
                        "category": "Other",
                        "value": 4.2,
                        "percentage": 32.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.761871",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Shipment Lead Time"
        }
    },
}
