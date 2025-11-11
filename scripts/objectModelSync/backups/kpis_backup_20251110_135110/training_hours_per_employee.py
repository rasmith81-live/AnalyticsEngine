"""
Average Training Hours per Employee

The average number of training hours provided to each warehouse employee.
"""

TRAINING_HOURS_PER_EMPLOYEE = {
    "code": "TRAINING_HOURS_PER_EMPLOYEE",
    "name": "Average Training Hours per Employee",
    "description": "The average number of training hours provided to each warehouse employee.",
    "formula": "Total Training Hours / Total Number of Employees",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Training Hours per Employee to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Employee", "Warehouse"], "last_validated": "2025-11-10T13:49:33.741860"},
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
                        302,
                        325,
                        296,
                        318,
                        313,
                        304,
                        292,
                        323,
                        329,
                        319,
                        324
                ],
                "unit": "count"
        },
        "current": {
                "value": 324,
                "unit": "count",
                "change": 5,
                "change_percent": 1.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 314.58,
                "min": 292,
                "max": 330,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 91.96,
                        "percentage": 28.4
                },
                {
                        "category": "Category B",
                        "value": 56.96,
                        "percentage": 17.6
                },
                {
                        "category": "Category C",
                        "value": 36.12,
                        "percentage": 11.1
                },
                {
                        "category": "Category D",
                        "value": 25.54,
                        "percentage": 7.9
                },
                {
                        "category": "Other",
                        "value": 113.42,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.115346",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Training Hours per Employee"
        }
    },
}
