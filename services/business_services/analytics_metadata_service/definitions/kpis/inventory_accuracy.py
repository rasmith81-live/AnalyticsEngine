"""
Inventory Accuracy

How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.
"""

INVENTORY_ACCURACY = {
    "code": "INVENTORY_ACCURACY",
    "name": "Inventory Accuracy",
    "description": "How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Accuracy to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Product"], "last_validated": "2025-11-10T13:49:32.979047"},
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
                        699.09,
                        692.89,
                        655.57,
                        620.71,
                        634.34,
                        664.76,
                        597.4,
                        687.76,
                        607.65,
                        661.99,
                        686.91,
                        581.56
                ],
                "unit": "units"
        },
        "current": {
                "value": 581.56,
                "unit": "units",
                "change": -105.35,
                "change_percent": -15.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 649.22,
                "min": 581.56,
                "max": 699.09,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 170.62,
                        "percentage": 29.3
                },
                {
                        "category": "Segment B",
                        "value": 137.97,
                        "percentage": 23.7
                },
                {
                        "category": "Segment C",
                        "value": 84.33,
                        "percentage": 14.5
                },
                {
                        "category": "Segment D",
                        "value": 56.51,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 132.13,
                        "percentage": 22.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.052489",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Inventory Accuracy"
        }
    },
}
