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
                        520.68,
                        448.44,
                        430.97,
                        449.44,
                        437.15,
                        556.72,
                        512.85,
                        467.87,
                        494.85,
                        455.02,
                        441.31,
                        420.62
                ],
                "unit": "units"
        },
        "current": {
                "value": 420.62,
                "unit": "units",
                "change": -20.69,
                "change_percent": -4.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 469.66,
                "min": 420.62,
                "max": 556.72,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 67.69,
                        "percentage": 16.1
                },
                {
                        "category": "Segment B",
                        "value": 72.41,
                        "percentage": 17.2
                },
                {
                        "category": "Segment C",
                        "value": 57.05,
                        "percentage": 13.6
                },
                {
                        "category": "Segment D",
                        "value": 34.92,
                        "percentage": 8.3
                },
                {
                        "category": "Other",
                        "value": 188.55,
                        "percentage": 44.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.403461",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Packing Flexibility"
        }
    },
}
