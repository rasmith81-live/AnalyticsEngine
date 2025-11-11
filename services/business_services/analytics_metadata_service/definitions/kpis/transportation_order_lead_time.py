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
                        7.2,
                        7.8,
                        8.1,
                        6.3,
                        11.1,
                        8.4,
                        11.7,
                        11.4,
                        8.8,
                        6.8,
                        6.8,
                        11.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 11.6,
                "unit": "days",
                "change": 4.8,
                "change_percent": 70.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 8.83,
                "min": 6.3,
                "max": 11.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 1.76,
                        "percentage": 15.2
                },
                {
                        "category": "Segment B",
                        "value": 2.5,
                        "percentage": 21.6
                },
                {
                        "category": "Segment C",
                        "value": 1.51,
                        "percentage": 13.0
                },
                {
                        "category": "Segment D",
                        "value": 0.98,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 4.85,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.890369",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Transportation Order Lead Time"
        }
    },
}
