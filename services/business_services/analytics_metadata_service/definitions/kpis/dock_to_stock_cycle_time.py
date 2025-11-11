"""
Dock-to-stock Cycle Time

The time taken to move goods from the receiving dock to the storage area.
"""

DOCK_TO_STOCK_CYCLE_TIME = {
    "code": "DOCK_TO_STOCK_CYCLE_TIME",
    "name": "Dock-to-stock Cycle Time",
    "description": "The time taken to move goods from the receiving dock to the storage area.",
    "formula": "Average Time from Goods Receipt to Warehouse Stocking",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Dock-to-stock Cycle Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Inventory", "Warehouse"], "last_validated": "2025-11-10T13:49:32.932543"},
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
                        15.4,
                        13.7,
                        15.4,
                        8.1,
                        8.4,
                        10.3,
                        10.2,
                        15.5,
                        8.4,
                        12.7,
                        8.7,
                        11.7
                ],
                "unit": "days"
        },
        "current": {
                "value": 11.7,
                "unit": "days",
                "change": 3.0,
                "change_percent": 34.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 11.54,
                "min": 8.1,
                "max": 15.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.54,
                        "percentage": 21.7
                },
                {
                        "category": "Segment B",
                        "value": 1.86,
                        "percentage": 15.9
                },
                {
                        "category": "Segment C",
                        "value": 1.52,
                        "percentage": 13.0
                },
                {
                        "category": "Segment D",
                        "value": 1.27,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 4.51,
                        "percentage": 38.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.934249",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Dock-to-stock Cycle Time"
        }
    },
}
