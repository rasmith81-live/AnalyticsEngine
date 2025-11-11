"""
Transportation Order Lead Time

The time from placing a transport order to the execution of the shipment.
"""

TRANSPORTATION_ORDER_LEAD_TIME = {
    "code": "TRANSPORTATION_ORDER_LEAD_TIME",
    "name": "Transportation Order Lead Time",
    "description": "The time from placing a transport order to the execution of the shipment.",
    "formula": "Average Time from Transportation Order Placement to Shipment Movement",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Order Lead Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Lead", "Order", "PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:33.758256"},
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
                        30.3,
                        25.0,
                        32.7,
                        31.3,
                        29.0,
                        29.3,
                        32.7,
                        26.2,
                        31.9,
                        31.1,
                        28.9,
                        26.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 26.3,
                "unit": "days",
                "change": -2.6,
                "change_percent": -9.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 29.56,
                "min": 25.0,
                "max": 32.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.78,
                        "percentage": 29.6
                },
                {
                        "category": "Category B",
                        "value": 6.36,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 2.9,
                        "percentage": 11.0
                },
                {
                        "category": "Category D",
                        "value": 1.87,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 7.39,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.152838",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Transportation Order Lead Time"
        }
    },
}
