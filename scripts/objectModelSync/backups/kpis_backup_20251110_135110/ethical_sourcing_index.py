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
                        65.3,
                        65.2,
                        70.6,
                        68.6,
                        62.2,
                        63.0,
                        62.1,
                        71.0,
                        64.9,
                        59.9,
                        69.1,
                        65.7
                ],
                "unit": "score"
        },
        "current": {
                "value": 65.7,
                "unit": "score",
                "change": -3.4,
                "change_percent": -4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 65.63,
                "min": 59.9,
                "max": 71.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.45,
                        "percentage": 32.6
                },
                {
                        "category": "Category B",
                        "value": 11.46,
                        "percentage": 17.4
                },
                {
                        "category": "Category C",
                        "value": 8.75,
                        "percentage": 13.3
                },
                {
                        "category": "Category D",
                        "value": 6.59,
                        "percentage": 10.0
                },
                {
                        "category": "Other",
                        "value": 17.45,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.477042",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Ethical Sourcing Index"
        }
    },
}
