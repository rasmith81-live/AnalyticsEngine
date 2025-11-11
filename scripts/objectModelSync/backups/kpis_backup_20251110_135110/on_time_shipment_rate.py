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
                        57.17,
                        67.82,
                        58.54,
                        69.33,
                        72.12,
                        57.68,
                        55.56,
                        62.61,
                        57.26,
                        72.75,
                        64.36,
                        68.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.89,
                "unit": "%",
                "change": 4.53,
                "change_percent": 7.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 63.67,
                "min": 55.56,
                "max": 72.75,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.52,
                        "percentage": 25.4
                },
                {
                        "category": "Category B",
                        "value": 13.84,
                        "percentage": 20.1
                },
                {
                        "category": "Category C",
                        "value": 8.51,
                        "percentage": 12.4
                },
                {
                        "category": "Category D",
                        "value": 4.8,
                        "percentage": 7.0
                },
                {
                        "category": "Other",
                        "value": 24.22,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.725451",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Shipment Rate"
        }
    },
}
