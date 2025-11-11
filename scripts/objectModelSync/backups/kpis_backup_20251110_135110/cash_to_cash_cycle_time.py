"""
Cash-to-Cash Cycle Time

The time between the outlay of cash for raw materials and receiving cash from customers for product sales, impacting liquidity and cash flow.
"""

CASH_TO_CASH_CYCLE_TIME = {
    "code": "CASH_TO_CASH_CYCLE_TIME",
    "name": "Cash-to-Cash Cycle Time",
    "description": "The time between the outlay of cash for raw materials and receiving cash from customers for product sales, impacting liquidity and cash flow.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cash-to-Cash Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Customer", "Inventory", "Product"], "last_validated": "2025-11-10T13:49:32.677265"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        22.4,
                        22.1,
                        25.6,
                        22.9,
                        25.0,
                        22.3,
                        23.6,
                        25.2,
                        23.1,
                        19.8,
                        19.6,
                        21.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 21.1,
                "unit": "days",
                "change": 1.5,
                "change_percent": 7.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 22.72,
                "min": 19.6,
                "max": 25.6,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 5.21,
                        "percentage": 24.7
                },
                {
                        "category": "Category B",
                        "value": 4.3,
                        "percentage": 20.4
                },
                {
                        "category": "Category C",
                        "value": 2.72,
                        "percentage": 12.9
                },
                {
                        "category": "Category D",
                        "value": 1.93,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 6.94,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.077531",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Cash-to-Cash Cycle Time"
        }
    },
}
