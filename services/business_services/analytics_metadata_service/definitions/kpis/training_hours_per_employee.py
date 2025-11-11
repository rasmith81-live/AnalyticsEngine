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
                        239,
                        208,
                        234,
                        242,
                        205,
                        244,
                        206,
                        205,
                        245,
                        235,
                        226,
                        206
                ],
                "unit": "count"
        },
        "current": {
                "value": 206,
                "unit": "count",
                "change": -20,
                "change_percent": -8.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 224.58,
                "min": 205,
                "max": 245,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 54.08,
                        "percentage": 26.3
                },
                {
                        "category": "Segment B",
                        "value": 38.5,
                        "percentage": 18.7
                },
                {
                        "category": "Segment C",
                        "value": 22.79,
                        "percentage": 11.1
                },
                {
                        "category": "Segment D",
                        "value": 27.05,
                        "percentage": 13.1
                },
                {
                        "category": "Other",
                        "value": 63.58,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.851698",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Training Hours per Employee"
        }
    },
}
