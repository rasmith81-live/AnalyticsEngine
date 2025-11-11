"""
Freight Bill Accuracy

The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.
"""

FREIGHT_BILL_ACCURACY = {
    "code": "FREIGHT_BILL_ACCURACY",
    "name": "Freight Bill Accuracy",
    "description": "The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Freight Bill Accuracy to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.499952"},
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
                        701.15,
                        675.52,
                        719.56,
                        750.56,
                        731.75,
                        648.67,
                        716.04,
                        733.89,
                        721.24,
                        670.44,
                        670.48,
                        637.17
                ],
                "unit": "units"
        },
        "current": {
                "value": 637.17,
                "unit": "units",
                "change": -33.31,
                "change_percent": -5.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 698.04,
                "min": 637.17,
                "max": 750.56,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 141.18,
                        "percentage": 22.2
                },
                {
                        "category": "Category B",
                        "value": 91.46,
                        "percentage": 14.4
                },
                {
                        "category": "Category C",
                        "value": 108.59,
                        "percentage": 17.0
                },
                {
                        "category": "Category D",
                        "value": 37.03,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 258.91,
                        "percentage": 40.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.499952",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Freight Bill Accuracy"
        }
    },
}
