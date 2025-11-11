"""
Lead Time Variability

The consistency of lead times provided by suppliers, with lower variability indicating more reliable delivery.
"""

LEAD_TIME_VARIABILITY = {
    "code": "LEAD_TIME_VARIABILITY",
    "name": "Lead Time Variability",
    "description": "The consistency of lead times provided by suppliers, with lower variability indicating more reliable delivery.",
    "formula": "Standard Deviation of Lead Times / Average Lead Time",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Time Variability to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Delivery", "Lead", "Supplier"], "last_validated": "2025-11-10T13:43:23.599643"},
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
                        25.4,
                        22.5,
                        22.0,
                        23.3,
                        22.3,
                        19.7,
                        20.1,
                        22.1,
                        21.8,
                        26.3,
                        26.8,
                        21.2
                ],
                "unit": "days"
        },
        "current": {
                "value": 21.2,
                "unit": "days",
                "change": -5.6,
                "change_percent": -20.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 22.79,
                "min": 19.7,
                "max": 26.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.11,
                        "percentage": 33.5
                },
                {
                        "category": "Category B",
                        "value": 4.13,
                        "percentage": 19.5
                },
                {
                        "category": "Category C",
                        "value": 3.42,
                        "percentage": 16.1
                },
                {
                        "category": "Category D",
                        "value": 1.07,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 5.47,
                        "percentage": 25.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.599643",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Lead Time Variability"
        }
    },
}
