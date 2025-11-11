"""
Shipping Accuracy

The percentage of shipments that are correct per the shipping documentation.
"""

SHIPPING_ACCURACY = {
    "code": "SHIPPING_ACCURACY",
    "name": "Shipping Accuracy",
    "description": "The percentage of shipments that are correct per the shipping documentation.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shipping Accuracy to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:33.571633"},
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
                        745.55,
                        744.75,
                        689.76,
                        658.88,
                        679.68,
                        672.24,
                        691.07,
                        679.93,
                        723.63,
                        639.16,
                        743.63,
                        704.49
                ],
                "unit": "units"
        },
        "current": {
                "value": 704.49,
                "unit": "units",
                "change": -39.14,
                "change_percent": -5.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 697.73,
                "min": 639.16,
                "max": 745.55,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 226.96,
                        "percentage": 32.2
                },
                {
                        "category": "Segment B",
                        "value": 133.5,
                        "percentage": 18.9
                },
                {
                        "category": "Segment C",
                        "value": 113.25,
                        "percentage": 16.1
                },
                {
                        "category": "Segment D",
                        "value": 65.86,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 164.92,
                        "percentage": 23.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.376780",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Shipping Accuracy"
        }
    },
}
