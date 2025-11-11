"""
Supply Chain Planning Cycle Time

The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.
"""

SUPPLY_CHAIN_PLANNING_CYCLE_TIME = {
    "code": "SUPPLY_CHAIN_PLANNING_CYCLE_TIME",
    "name": "Supply Chain Planning Cycle Time",
    "description": "The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.",
    "formula": "Total Planning Cycle Time",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supply Chain Planning Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.664594"},
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
                        17.7,
                        22.7,
                        19.8,
                        18.3,
                        22.1,
                        17.2,
                        16.6,
                        16.7,
                        18.0,
                        18.4,
                        22.4,
                        16.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 16.5,
                "unit": "days",
                "change": -5.9,
                "change_percent": -26.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 18.87,
                "min": 16.5,
                "max": 22.7,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.63,
                        "percentage": 15.9
                },
                {
                        "category": "Segment B",
                        "value": 4.69,
                        "percentage": 28.4
                },
                {
                        "category": "Segment C",
                        "value": 1.4,
                        "percentage": 8.5
                },
                {
                        "category": "Segment D",
                        "value": 2.06,
                        "percentage": 12.5
                },
                {
                        "category": "Other",
                        "value": 5.72,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.629302",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supply Chain Planning Cycle Time"
        }
    },
}
