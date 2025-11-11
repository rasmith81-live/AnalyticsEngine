"""
Procurement Process Compliance

The adherence to established procurement policies and procedures.
"""

PROCUREMENT_PROCESS_COMPLIANCE = {
    "code": "PROCUREMENT_PROCESS_COMPLIANCE",
    "name": "Procurement Process Compliance",
    "description": "The adherence to established procurement policies and procedures.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Process Compliance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.956523"},
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
                        904.35,
                        790.2,
                        825.77,
                        909.95,
                        787.95,
                        869.66,
                        910.73,
                        869.33,
                        872.82,
                        863.76,
                        881.91,
                        865.28
                ],
                "unit": "units"
        },
        "current": {
                "value": 865.28,
                "unit": "units",
                "change": -16.63,
                "change_percent": -1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 862.64,
                "min": 787.95,
                "max": 910.73,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 206.46,
                        "percentage": 23.9
                },
                {
                        "category": "Category B",
                        "value": 138.04,
                        "percentage": 16.0
                },
                {
                        "category": "Category C",
                        "value": 106.94,
                        "percentage": 12.4
                },
                {
                        "category": "Category D",
                        "value": 56.37,
                        "percentage": 6.5
                },
                {
                        "category": "Other",
                        "value": 357.47,
                        "percentage": 41.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.956523",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Procurement Process Compliance"
        }
    },
}
