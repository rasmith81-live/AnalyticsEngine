"""
Strategic Sourcing Savings

The cost savings achieved through the strategic sourcing process by optimizing supplier selection and procurement practices.
"""

STRATEGIC_SOURCING_SAVINGS = {
    "code": "STRATEGIC_SOURCING_SAVINGS",
    "name": "Strategic Sourcing Savings",
    "description": "The cost savings achieved through the strategic sourcing process by optimizing supplier selection and procurement practices.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Sourcing Savings to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.612630"},
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
                        76.46,
                        88.4,
                        72.53,
                        71.58,
                        70.34,
                        85.38,
                        78.78,
                        88.47,
                        85.63,
                        83.51,
                        82.91,
                        71.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.89,
                "unit": "%",
                "change": -11.02,
                "change_percent": -13.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 79.66,
                "min": 70.34,
                "max": 88.47,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 23.59,
                        "percentage": 32.8
                },
                {
                        "category": "Category B",
                        "value": 8.12,
                        "percentage": 11.3
                },
                {
                        "category": "Category C",
                        "value": 6.82,
                        "percentage": 9.5
                },
                {
                        "category": "Category D",
                        "value": 6.35,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 27.01,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.827620",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Sourcing Savings"
        }
    },
}
