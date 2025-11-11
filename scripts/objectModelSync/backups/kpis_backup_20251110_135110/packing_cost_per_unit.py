"""
Packing Cost per Unit

The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.
"""

PACKING_COST_PER_UNIT = {
    "code": "PACKING_COST_PER_UNIT",
    "name": "Packing Cost per Unit",
    "description": "The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.",
    "formula": "Total Packing Costs / Total Units Packed",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Cost per Unit to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.151458"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        22145.09,
                        27599.8,
                        23962.88,
                        20447.81,
                        31163.18,
                        27274.06,
                        30099.2,
                        25965.23,
                        29528.7,
                        31874.69,
                        30948.78,
                        27285.71
                ],
                "unit": "$"
        },
        "current": {
                "value": 27285.71,
                "unit": "$",
                "change": -3663.07,
                "change_percent": -11.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 27357.93,
                "min": 20447.81,
                "max": 31874.69,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8125.11,
                        "percentage": 29.8
                },
                {
                        "category": "Category B",
                        "value": 4133.0,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 3201.18,
                        "percentage": 11.7
                },
                {
                        "category": "Category D",
                        "value": 2081.13,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 9745.29,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.800271",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Packing Cost per Unit"
        }
    },
}
