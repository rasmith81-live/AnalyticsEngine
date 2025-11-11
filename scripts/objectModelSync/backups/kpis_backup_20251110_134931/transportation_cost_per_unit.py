"""
Transportation Cost per Unit

The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.
"""

TRANSPORTATION_COST_PER_UNIT = {
    "code": "TRANSPORTATION_COST_PER_UNIT",
    "name": "Transportation Cost per Unit",
    "description": "The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.",
    "formula": "Total Transportation Costs / Total Number of Units Shipped",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Cost per Unit to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:25.139624"},
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
                        511,
                        489,
                        490,
                        508,
                        493,
                        498,
                        523,
                        489,
                        512,
                        484,
                        500,
                        525
                ],
                "unit": "count"
        },
        "current": {
                "value": 525,
                "unit": "count",
                "change": 25,
                "change_percent": 5.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 501.83,
                "min": 484,
                "max": 525,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 114.41,
                        "percentage": 21.8
                },
                {
                        "category": "Category B",
                        "value": 122.93,
                        "percentage": 23.4
                },
                {
                        "category": "Category C",
                        "value": 49.85,
                        "percentage": 9.5
                },
                {
                        "category": "Category D",
                        "value": 55.1,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 182.71,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.139624",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Transportation Cost per Unit"
        }
    },
}
