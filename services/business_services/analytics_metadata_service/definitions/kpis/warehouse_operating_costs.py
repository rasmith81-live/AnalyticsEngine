"""
Warehouse Operating Costs

The total operating costs of running a warehouse.
"""

WAREHOUSE_OPERATING_COSTS = {
    "code": "WAREHOUSE_OPERATING_COSTS",
    "name": "Warehouse Operating Costs",
    "description": "The total operating costs of running a warehouse.",
    "formula": "Sum of all Warehouse Operating Costs",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Operating Costs to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:49:33.803968"},
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
                        106438.39,
                        104463.2,
                        98954.38,
                        95284.06,
                        103770.36,
                        95103.98,
                        96516.52,
                        109734.49,
                        97768.77,
                        99097.65,
                        106939.26,
                        106635.53
                ],
                "unit": "$"
        },
        "current": {
                "value": 106635.53,
                "unit": "$",
                "change": -303.73,
                "change_percent": -0.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 101725.55,
                "min": 95103.98,
                "max": 109734.49,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19975.43,
                        "percentage": 18.7
                },
                {
                        "category": "Segment B",
                        "value": 23915.34,
                        "percentage": 22.4
                },
                {
                        "category": "Segment C",
                        "value": 15639.74,
                        "percentage": 14.7
                },
                {
                        "category": "Segment D",
                        "value": 7804.65,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 39300.37,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.977893",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Warehouse Operating Costs"
        }
    },
}
