"""
Material Utilization Rate

The percentage of packaging materials that are optimally used without excess waste, reflecting sustainable packaging practices.
"""

MATERIAL_UTILIZATION_RATE = {
    "code": "MATERIAL_UTILIZATION_RATE",
    "name": "Material Utilization Rate",
    "description": "The percentage of packaging materials that are optimally used without excess waste, reflecting sustainable packaging practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Material Utilization Rate to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.049436"},
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
                        81.86,
                        74.56,
                        72.0,
                        78.96,
                        70.69,
                        82.11,
                        84.1,
                        72.46,
                        68.43,
                        69.77,
                        77.21,
                        79.62
                ],
                "unit": "%"
        },
        "current": {
                "value": 79.62,
                "unit": "%",
                "change": 2.41,
                "change_percent": 3.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 75.98,
                "min": 68.43,
                "max": 84.1,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 21.92,
                        "percentage": 27.5
                },
                {
                        "category": "Segment B",
                        "value": 10.44,
                        "percentage": 13.1
                },
                {
                        "category": "Segment C",
                        "value": 15.13,
                        "percentage": 19.0
                },
                {
                        "category": "Segment D",
                        "value": 4.02,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 28.11,
                        "percentage": 35.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.202123",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Material Utilization Rate"
        }
    },
}
