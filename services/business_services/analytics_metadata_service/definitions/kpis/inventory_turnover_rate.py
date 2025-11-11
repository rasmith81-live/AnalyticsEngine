"""
Inventory Turnover Rate

How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.
"""

INVENTORY_TURNOVER_RATE = {
    "code": "INVENTORY_TURNOVER_RATE",
    "name": "Inventory Turnover Rate",
    "description": "How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.",
    "formula": "Cost of Goods Sold / Average Inventory Value",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Inventory Turnover Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Inventory"], "last_validated": "2025-11-10T13:49:32.982972"},
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
                        60.2,
                        61.85,
                        51.04,
                        58.51,
                        47.37,
                        57.28,
                        54.55,
                        51.32,
                        47.56,
                        56.96,
                        59.21,
                        64.8
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.8,
                "unit": "%",
                "change": 5.59,
                "change_percent": 9.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 55.89,
                "min": 47.37,
                "max": 64.8,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.51,
                        "percentage": 27.0
                },
                {
                        "category": "Segment B",
                        "value": 7.95,
                        "percentage": 12.3
                },
                {
                        "category": "Segment C",
                        "value": 9.16,
                        "percentage": 14.1
                },
                {
                        "category": "Segment D",
                        "value": 4.72,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 25.46,
                        "percentage": 39.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.071766",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Inventory Turnover Rate"
        }
    },
}
