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
                        26299.18,
                        26605.03,
                        28760.65,
                        35611.15,
                        30814.78,
                        29018.24,
                        25338.38,
                        36142.92,
                        22873.31,
                        23712.36,
                        33639.31,
                        33853.58
                ],
                "unit": "$"
        },
        "current": {
                "value": 33853.58,
                "unit": "$",
                "change": 214.27,
                "change_percent": 0.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 29389.07,
                "min": 22873.31,
                "max": 36142.92,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7832.16,
                        "percentage": 23.1
                },
                {
                        "category": "Category B",
                        "value": 8879.58,
                        "percentage": 26.2
                },
                {
                        "category": "Category C",
                        "value": 5237.92,
                        "percentage": 15.5
                },
                {
                        "category": "Category D",
                        "value": 1928.96,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 9974.96,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.074697",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Carrying Cost of Inventory"
        }
    },
}
