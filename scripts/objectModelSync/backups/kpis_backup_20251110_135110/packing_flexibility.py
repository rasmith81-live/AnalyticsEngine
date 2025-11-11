"""
Packing Flexibility

A measure of the ability to adapt packing operations to changes in demand or product types, indicating operational agility.
"""

PACKING_FLEXIBILITY = {
    "code": "PACKING_FLEXIBILITY",
    "name": "Packing Flexibility",
    "description": "A measure of the ability to adapt packing operations to changes in demand or product types, indicating operational agility.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Flexibility to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order", "Product"], "last_validated": "2025-11-10T13:49:33.159513"},
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
                        783.2,
                        758.49,
                        861.37,
                        849.06,
                        784.93,
                        741.13,
                        849.19,
                        780.07,
                        846.78,
                        830.49,
                        752.7,
                        749.1
                ],
                "unit": "units"
        },
        "current": {
                "value": 749.1,
                "unit": "units",
                "change": -3.6,
                "change_percent": -0.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 798.88,
                "min": 741.13,
                "max": 861.37,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 187.45,
                        "percentage": 25.0
                },
                {
                        "category": "Category B",
                        "value": 176.26,
                        "percentage": 23.5
                },
                {
                        "category": "Category C",
                        "value": 120.18,
                        "percentage": 16.0
                },
                {
                        "category": "Category D",
                        "value": 54.34,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 210.87,
                        "percentage": 28.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.815447",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Flexibility"
        }
    },
}
