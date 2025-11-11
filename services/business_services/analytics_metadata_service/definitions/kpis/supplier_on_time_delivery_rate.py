"""
Supplier On-time Delivery Rate

The percentage of orders delivered by suppliers on or before the promised delivery date, indicating their reliability and efficiency.
"""

SUPPLIER_ON_TIME_DELIVERY_RATE = {
    "code": "SUPPLIER_ON_TIME_DELIVERY_RATE",
    "name": "Supplier On-time Delivery Rate",
    "description": "The percentage of orders delivered by suppliers on or before the promised delivery date, indicating their reliability and efficiency.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier On-time Delivery Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Delivery", "Order", "Supplier"], "last_validated": "2025-11-10T13:49:33.641965"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        64.46,
                        69.68,
                        63.24,
                        59.72,
                        68.4,
                        67.9,
                        55.54,
                        72.0,
                        60.17,
                        54.46,
                        67.94,
                        61.87
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.87,
                "unit": "%",
                "change": -6.07,
                "change_percent": -8.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 63.78,
                "min": 54.46,
                "max": 72.0,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 10.34,
                        "percentage": 16.7
                },
                {
                        "category": "Segment B",
                        "value": 16.63,
                        "percentage": 26.9
                },
                {
                        "category": "Segment C",
                        "value": 10.41,
                        "percentage": 16.8
                },
                {
                        "category": "Segment D",
                        "value": 5.04,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 19.45,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.576423",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier On-time Delivery Rate"
        }
    },
}
