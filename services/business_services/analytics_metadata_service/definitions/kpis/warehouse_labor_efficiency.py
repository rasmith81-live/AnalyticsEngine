"""
Warehouse Labor Efficiency

The overall efficiency of warehouse staff based on output over input.
"""

WAREHOUSE_LABOR_EFFICIENCY = {
    "code": "WAREHOUSE_LABOR_EFFICIENCY",
    "name": "Warehouse Labor Efficiency",
    "description": "The overall efficiency of warehouse staff based on output over input.",
    "formula": "Total Number of Orders Fulfilled / Total Labor Hours",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Warehouse Labor Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Employee", "Order", "Warehouse"], "last_validated": "2025-11-10T13:49:33.802309"},
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
                        330,
                        343,
                        346,
                        346,
                        368,
                        332,
                        337,
                        352,
                        370,
                        374,
                        337,
                        344
                ],
                "unit": "count"
        },
        "current": {
                "value": 344,
                "unit": "count",
                "change": 7,
                "change_percent": 2.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 348.25,
                "min": 330,
                "max": 374,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 52.2,
                        "percentage": 15.2
                },
                {
                        "category": "Segment B",
                        "value": 50.35,
                        "percentage": 14.6
                },
                {
                        "category": "Segment C",
                        "value": 62.94,
                        "percentage": 18.3
                },
                {
                        "category": "Segment D",
                        "value": 29.66,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 148.85,
                        "percentage": 43.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.974723",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Warehouse Labor Efficiency"
        }
    },
}
