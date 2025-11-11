"""
Supplier Quality Index

A composite score reflecting the quality of products or services provided by suppliers.
"""

SUPPLIER_QUALITY_INDEX = {
    "code": "SUPPLIER_QUALITY_INDEX",
    "name": "Supplier Quality Index",
    "description": "A composite score reflecting the quality of products or services provided by suppliers.",
    "formula": "Sum of Weighted Quality Metrics / Total Number of Quality Metrics",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Quality Index to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Product", "PurchaseOrder", "QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:49:33.644114"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        353,
                        370,
                        382,
                        346,
                        394,
                        355,
                        365,
                        375,
                        356,
                        377,
                        372,
                        354
                ],
                "unit": "count"
        },
        "current": {
                "value": 354,
                "unit": "count",
                "change": -18,
                "change_percent": -4.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 366.58,
                "min": 346,
                "max": 394,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 72.52,
                        "percentage": 20.5
                },
                {
                        "category": "Segment B",
                        "value": 44.88,
                        "percentage": 12.7
                },
                {
                        "category": "Segment C",
                        "value": 63.14,
                        "percentage": 17.8
                },
                {
                        "category": "Segment D",
                        "value": 42.8,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 130.66,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.580208",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Supplier Quality Index"
        }
    },
}
