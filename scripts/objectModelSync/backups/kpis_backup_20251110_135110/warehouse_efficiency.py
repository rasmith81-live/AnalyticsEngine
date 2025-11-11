"""
Average Warehouse Efficiency

The overall efficiency of warehouse operations based on output over input.
"""

WAREHOUSE_EFFICIENCY = {
    "code": "WAREHOUSE_EFFICIENCY",
    "name": "Average Warehouse Efficiency",
    "description": "The overall efficiency of warehouse operations based on output over input.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Warehouse Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Order", "Warehouse"], "last_validated": "2025-11-10T13:49:33.797103"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        383.03,
                        418.87,
                        419.19,
                        389.17,
                        378.17,
                        362.96,
                        339.43,
                        326.64,
                        305.02,
                        408.62,
                        407.49,
                        329.81
                ],
                "unit": "units"
        },
        "current": {
                "value": 329.81,
                "unit": "units",
                "change": -77.68,
                "change_percent": -19.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 372.37,
                "min": 305.02,
                "max": 419.19,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 72.35,
                        "percentage": 21.9
                },
                {
                        "category": "Category B",
                        "value": 89.14,
                        "percentage": 27.0
                },
                {
                        "category": "Category C",
                        "value": 47.99,
                        "percentage": 14.6
                },
                {
                        "category": "Category D",
                        "value": 35.81,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 84.52,
                        "percentage": 25.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.243665",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Warehouse Efficiency"
        }
    },
}
