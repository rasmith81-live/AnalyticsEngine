"""
Supplier Risk Assessment Rate

The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.
"""

SUPPLIER_RISK_ASSESSMENT_RATE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_RATE",
    "name": "Supplier Risk Assessment Rate",
    "description": "The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Risk Assessment Rate to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:24.889589"},
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
                        77.66,
                        65.81,
                        68.24,
                        60.24,
                        77.63,
                        70.06,
                        70.44,
                        61.66,
                        76.9,
                        64.65,
                        64.69,
                        68.4
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.4,
                "unit": "%",
                "change": 3.71,
                "change_percent": 5.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 68.86,
                "min": 60.24,
                "max": 77.66,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 14.88,
                        "percentage": 21.8
                },
                {
                        "category": "Category B",
                        "value": 10.09,
                        "percentage": 14.8
                },
                {
                        "category": "Category C",
                        "value": 9.4,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 9.5,
                        "percentage": 13.9
                },
                {
                        "category": "Other",
                        "value": 24.53,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.889589",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Risk Assessment Rate"
        }
    },
}
