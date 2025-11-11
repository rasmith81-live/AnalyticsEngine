"""
Lead Time Reduction

The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.
"""

LEAD_TIME_REDUCTION = {
    "code": "LEAD_TIME_REDUCTION",
    "name": "Lead Time Reduction",
    "description": "The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Time Reduction to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.597899"},
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
                        23.6,
                        21.8,
                        20.0,
                        19.1,
                        24.4,
                        21.2,
                        20.3,
                        20.7,
                        18.8,
                        20.6,
                        22.1,
                        17.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 17.5,
                "unit": "days",
                "change": -4.6,
                "change_percent": -20.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 20.84,
                "min": 17.5,
                "max": 24.4,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 5.73,
                        "percentage": 32.7
                },
                {
                        "category": "Category B",
                        "value": 2.24,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 2.56,
                        "percentage": 14.6
                },
                {
                        "category": "Category D",
                        "value": 2.04,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 4.93,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.597899",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Lead Time Reduction"
        }
    },
}
