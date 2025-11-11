"""
Ethical Sourcing Index

A measure of the extent to which sourcing policies and practices align with ethical standards, in accordance with ISO 20400.
"""

ETHICAL_SOURCING_INDEX = {
    "code": "ETHICAL_SOURCING_INDEX",
    "name": "Ethical Sourcing Index",
    "description": "A measure of the extent to which sourcing policies and practices align with ethical standards, in accordance with ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Ethical Sourcing Index to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:32.948062"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        87.8,
                        81.1,
                        91.0,
                        84.5,
                        92.0,
                        86.9,
                        93.4,
                        84.6,
                        81.5,
                        86.5,
                        84.8,
                        89.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 89.5,
                "unit": "score",
                "change": 4.7,
                "change_percent": 5.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 86.97,
                "min": 81.1,
                "max": 93.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.6,
                        "percentage": 20.8
                },
                {
                        "category": "Segment B",
                        "value": 23.04,
                        "percentage": 25.7
                },
                {
                        "category": "Segment C",
                        "value": 13.79,
                        "percentage": 15.4
                },
                {
                        "category": "Segment D",
                        "value": 3.44,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 30.63,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.973914",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Ethical Sourcing Index"
        }
    },
}
