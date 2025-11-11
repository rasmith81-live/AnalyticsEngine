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
                        55.29,
                        58.99,
                        46.85,
                        59.78,
                        51.06,
                        61.37,
                        59.18,
                        51.14,
                        57.04,
                        53.24,
                        53.46,
                        48.23
                ],
                "unit": "%"
        },
        "current": {
                "value": 48.23,
                "unit": "%",
                "change": -5.23,
                "change_percent": -9.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 54.64,
                "min": 46.85,
                "max": 61.37,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.79,
                        "percentage": 26.5
                },
                {
                        "category": "Category B",
                        "value": 10.55,
                        "percentage": 21.9
                },
                {
                        "category": "Category C",
                        "value": 8.51,
                        "percentage": 17.6
                },
                {
                        "category": "Category D",
                        "value": 3.68,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 12.7,
                        "percentage": 26.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.836631",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Collaboration Index"
        }
    },
}
