"""
Shrinkage Rate

The percentage of inventory loss between manufacture and point of sale.
"""

SHRINKAGE_RATE = {
    "code": "SHRINKAGE_RATE",
    "name": "Shrinkage Rate",
    "description": "The percentage of inventory loss between manufacture and point of sale.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Shrinkage Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.573235"},
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
                        75.93,
                        58.7,
                        60.4,
                        63.76,
                        61.25,
                        59.07,
                        67.94,
                        68.05,
                        72.45,
                        60.05,
                        68.6,
                        62.86
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.86,
                "unit": "%",
                "change": -5.74,
                "change_percent": -8.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 64.92,
                "min": 58.7,
                "max": 75.93,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.06,
                        "percentage": 30.3
                },
                {
                        "category": "Segment B",
                        "value": 10.83,
                        "percentage": 17.2
                },
                {
                        "category": "Segment C",
                        "value": 7.38,
                        "percentage": 11.7
                },
                {
                        "category": "Segment D",
                        "value": 2.67,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 22.92,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.381764",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Shrinkage Rate"
        }
    },
}
