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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "PurchaseOrder", "Shipment"], "last_validated": "2025-11-10T13:49:33.099218"},
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
                        50.17,
                        55.64,
                        46.35,
                        47.91,
                        45.65,
                        39.57,
                        54.0,
                        48.98,
                        54.63,
                        46.73,
                        40.55,
                        44.54
                ],
                "unit": "%"
        },
        "current": {
                "value": 44.54,
                "unit": "%",
                "change": 3.99,
                "change_percent": 9.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 47.89,
                "min": 39.57,
                "max": 55.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.0,
                        "percentage": 29.2
                },
                {
                        "category": "Segment B",
                        "value": 8.86,
                        "percentage": 19.9
                },
                {
                        "category": "Segment C",
                        "value": 5.29,
                        "percentage": 11.9
                },
                {
                        "category": "Segment D",
                        "value": 3.31,
                        "percentage": 7.4
                },
                {
                        "category": "Other",
                        "value": 14.08,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.281395",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Delivery Rate"
        }
    },
}
