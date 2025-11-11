"""
Supplier Collaboration Index

A measure of the quality and depth of collaborative efforts between the organization and its suppliers, impacting innovation and performance.
"""

SUPPLIER_COLLABORATION_INDEX = {
    "code": "SUPPLIER_COLLABORATION_INDEX",
    "name": "Supplier Collaboration Index",
    "description": "A measure of the quality and depth of collaborative efforts between the organization and its suppliers, impacting innovation and performance.",
    "formula": "Sum of collaboration scores / Number of Suppliers",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Collaboration Index to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:49:33.619630"},
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
                        70.66,
                        66.83,
                        70.35,
                        72.05,
                        55.46,
                        64.19,
                        63.9,
                        56.54,
                        67.78,
                        52.7,
                        63.64,
                        59.9
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.9,
                "unit": "%",
                "change": -3.74,
                "change_percent": -5.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 63.67,
                "min": 52.7,
                "max": 72.05,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 13.63,
                        "percentage": 22.8
                },
                {
                        "category": "Segment B",
                        "value": 14.68,
                        "percentage": 24.5
                },
                {
                        "category": "Segment C",
                        "value": 5.89,
                        "percentage": 9.8
                },
                {
                        "category": "Segment D",
                        "value": 7.15,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 18.55,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.502640",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Collaboration Index"
        }
    },
}
