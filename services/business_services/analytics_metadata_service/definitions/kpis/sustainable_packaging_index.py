"""
Sustainable Packaging Index

A measure of the percentage of packaging materials that are recyclable or biodegradable, reflecting environmentally friendly practices.
"""

SUSTAINABLE_PACKAGING_INDEX = {
    "code": "SUSTAINABLE_PACKAGING_INDEX",
    "name": "Sustainable Packaging Index",
    "description": "A measure of the percentage of packaging materials that are recyclable or biodegradable, reflecting environmentally friendly practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sustainable Packaging Index to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.693147"},
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
                        64.9,
                        63.7,
                        70.6,
                        68.1,
                        72.2,
                        72.4,
                        63.7,
                        71.4,
                        61.1,
                        67.2,
                        66.2,
                        68.9
                ],
                "unit": "score"
        },
        "current": {
                "value": 68.9,
                "unit": "score",
                "change": 2.7,
                "change_percent": 4.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.53,
                "min": 61.1,
                "max": 72.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.1,
                        "percentage": 29.2
                },
                {
                        "category": "Segment B",
                        "value": 7.85,
                        "percentage": 11.4
                },
                {
                        "category": "Segment C",
                        "value": 10.25,
                        "percentage": 14.9
                },
                {
                        "category": "Segment D",
                        "value": 3.14,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 27.56,
                        "percentage": 40.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.714471",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sustainable Packaging Index"
        }
    },
}
