"""
Supplier Quality Rating

The average score of suppliers
"""

SUPPLIER_QUALITY_RATING = {
    "code": "SUPPLIER_QUALITY_RATING",
    "name": "Supplier Quality Rating",
    "description": "The average score of suppliers",
    "formula": "Sum of Supplier Quality Scores / Number of Suppliers",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Quality Rating to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:49:33.645698"},
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
                        426,
                        426,
                        401,
                        414,
                        403,
                        420,
                        429,
                        415,
                        450,
                        447,
                        430,
                        438
                ],
                "unit": "count"
        },
        "current": {
                "value": 438,
                "unit": "count",
                "change": 8,
                "change_percent": 1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 424.92,
                "min": 401,
                "max": 450,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 90.08,
                        "percentage": 20.6
                },
                {
                        "category": "Segment B",
                        "value": 112.2,
                        "percentage": 25.6
                },
                {
                        "category": "Segment C",
                        "value": 39.31,
                        "percentage": 9.0
                },
                {
                        "category": "Segment D",
                        "value": 52.09,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 144.32,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.584713",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Supplier Quality Rating"
        }
    },
}
