"""
Inventory to Sales Ratio

The ratio of inventory on hand to the number of sales orders fulfilled.
"""

INVENTORY_TO_SALES_RATIO = {
    "code": "INVENTORY_TO_SALES_RATIO",
    "name": "Inventory to Sales Ratio",
    "description": "The ratio of inventory on hand to the number of sales orders fulfilled.",
    "formula": "Average Inventory Value / Total Sales",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory to Sales Ratio to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory", "Order"], "last_validated": "2025-11-10T13:49:32.982972"},
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
                        64.63,
                        67.32,
                        78.19,
                        72.61,
                        72.44,
                        74.46,
                        74.02,
                        78.18,
                        71.35,
                        66.02,
                        60.85,
                        73.98
                ],
                "unit": "%"
        },
        "current": {
                "value": 73.98,
                "unit": "%",
                "change": 13.13,
                "change_percent": 21.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 71.17,
                "min": 60.85,
                "max": 78.19,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 14.61,
                        "percentage": 19.7
                },
                {
                        "category": "Channel Sales",
                        "value": 9.63,
                        "percentage": 13.0
                },
                {
                        "category": "Online Sales",
                        "value": 13.33,
                        "percentage": 18.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 10.56,
                        "percentage": 14.3
                },
                {
                        "category": "Other",
                        "value": 25.85,
                        "percentage": 34.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.069074",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory to Sales Ratio"
        }
    },
}
