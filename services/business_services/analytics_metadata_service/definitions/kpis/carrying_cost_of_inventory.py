"""
Carrying Cost of Inventory

The cost of storing and maintaining inventory, including warehousing, insurance, and depreciation. It helps identify opportunities to reduce inventory costs without sacrificing customer service levels.
"""

CARRYING_COST_OF_INVENTORY = {
    "code": "CARRYING_COST_OF_INVENTORY",
    "name": "Carrying Cost of Inventory",
    "description": "The cost of storing and maintaining inventory, including warehousing, insurance, and depreciation. It helps identify opportunities to reduce inventory costs without sacrificing customer service levels.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Carrying Cost of Inventory to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Inventory", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.676112"},
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
                        88942.62,
                        89738.5,
                        81248.48,
                        92776.79,
                        88708.84,
                        86043.91,
                        94287.31,
                        83434.38,
                        81278.93,
                        85149.07,
                        90716.74,
                        89742.72
                ],
                "unit": "$"
        },
        "current": {
                "value": 89742.72,
                "unit": "$",
                "change": -974.02,
                "change_percent": -1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 87672.36,
                "min": 81248.48,
                "max": 94287.31,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 22838.31,
                        "percentage": 25.4
                },
                {
                        "category": "Segment B",
                        "value": 21724.77,
                        "percentage": 24.2
                },
                {
                        "category": "Segment C",
                        "value": 7625.37,
                        "percentage": 8.5
                },
                {
                        "category": "Segment D",
                        "value": 6336.29,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 31217.98,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.424879",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Carrying Cost of Inventory"
        }
    },
}
