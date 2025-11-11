"""
On-time Shipment Rate

The percentage of orders shipped on or before the requested ship date.
"""

ON_TIME_SHIPMENT_RATE = {
    "code": "ON_TIME_SHIPMENT_RATE",
    "name": "On-time Shipment Rate",
    "description": "The percentage of orders shipped on or before the requested ship date.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for On-time Shipment Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Shipment"], "last_validated": "2025-11-10T13:49:33.103028"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        70.4,
                        59.96,
                        60.52,
                        76.71,
                        69.09,
                        67.23,
                        66.37,
                        77.45,
                        76.72,
                        59.91,
                        76.14,
                        64.59
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.59,
                "unit": "%",
                "change": -11.55,
                "change_percent": -15.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.76,
                "min": 59.91,
                "max": 77.45,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22.4,
                        "percentage": 34.7
                },
                {
                        "category": "Segment B",
                        "value": 8.58,
                        "percentage": 13.3
                },
                {
                        "category": "Segment C",
                        "value": 6.82,
                        "percentage": 10.6
                },
                {
                        "category": "Segment D",
                        "value": 7.27,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 19.52,
                        "percentage": 30.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.287210",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Shipment Rate"
        }
    },
}
