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
                        16.5,
                        19.0,
                        22.7,
                        18.6,
                        18.6,
                        21.1,
                        18.8,
                        18.4,
                        20.4,
                        21.6,
                        19.2,
                        20.8
                ],
                "unit": "days"
        },
        "current": {
                "value": 20.8,
                "unit": "days",
                "change": 1.6,
                "change_percent": 8.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 19.64,
                "min": 16.5,
                "max": 22.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 3.69,
                        "percentage": 17.7
                },
                {
                        "category": "Segment B",
                        "value": 3.52,
                        "percentage": 16.9
                },
                {
                        "category": "Segment C",
                        "value": 3.0,
                        "percentage": 14.4
                },
                {
                        "category": "Segment D",
                        "value": 1.51,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 9.08,
                        "percentage": 43.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.427718",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Cash-to-Cash Cycle Time"
        }
    },
}
