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
                        51.66,
                        57.25,
                        56.11,
                        44.77,
                        61.87,
                        52.84,
                        45.94,
                        44.17,
                        49.93,
                        54.38,
                        60.99,
                        57.51
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.51,
                "unit": "%",
                "change": -3.48,
                "change_percent": -5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.12,
                "min": 44.17,
                "max": 61.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.79,
                        "percentage": 15.3
                },
                {
                        "category": "Category B",
                        "value": 16.66,
                        "percentage": 29.0
                },
                {
                        "category": "Category C",
                        "value": 6.81,
                        "percentage": 11.8
                },
                {
                        "category": "Category D",
                        "value": 6.18,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 19.07,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.872630",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier On-time Delivery Rate"
        }
    },
}
