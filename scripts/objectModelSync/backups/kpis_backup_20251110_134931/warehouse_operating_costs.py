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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Warehouse"], "last_validated": "2025-11-10T13:43:25.257986"},
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
                        50732.3,
                        44582.82,
                        43785.58,
                        48235.65,
                        47332.83,
                        57269.28,
                        45114.09,
                        55115.47,
                        44698.06,
                        44283.35,
                        42474.78,
                        53527.91
                ],
                "unit": "$"
        },
        "current": {
                "value": 53527.91,
                "unit": "$",
                "change": 11053.13,
                "change_percent": 26.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 48096.01,
                "min": 42474.78,
                "max": 57269.28,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11882.81,
                        "percentage": 22.2
                },
                {
                        "category": "Category B",
                        "value": 11517.98,
                        "percentage": 21.5
                },
                {
                        "category": "Category C",
                        "value": 8589.9,
                        "percentage": 16.0
                },
                {
                        "category": "Category D",
                        "value": 5981.39,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 15555.83,
                        "percentage": 29.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.257986",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Warehouse Operating Costs"
        }
    },
}
