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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:33.570052"},
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
                        21.0,
                        24.1,
                        25.7,
                        25.8,
                        24.4,
                        18.4,
                        19.6,
                        24.2,
                        25.8,
                        22.8,
                        25.4,
                        21.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 21.1,
                "unit": "days",
                "change": -4.3,
                "change_percent": -16.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 23.19,
                "min": 18.4,
                "max": 25.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 4.72,
                        "percentage": 22.4
                },
                {
                        "category": "Segment B",
                        "value": 5.42,
                        "percentage": 25.7
                },
                {
                        "category": "Segment C",
                        "value": 3.47,
                        "percentage": 16.4
                },
                {
                        "category": "Segment D",
                        "value": 1.69,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 5.8,
                        "percentage": 27.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.372890",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Shipment Lead Time"
        }
    },
}
