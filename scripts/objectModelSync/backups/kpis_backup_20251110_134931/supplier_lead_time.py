"""
Supplier Lead Time

The amount of time between when an order is placed with a supplier and when the order is received.
"""

SUPPLIER_LEAD_TIME = {
    "code": "SUPPLIER_LEAD_TIME",
    "name": "Supplier Lead Time",
    "description": "The amount of time between when an order is placed with a supplier and when the order is received.",
    "formula": "Average Time from Order Placement to Receipt",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Lead Time to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Lead", "Order", "Supplier"], "last_validated": "2025-11-10T13:43:24.866807"},
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
                        15.9,
                        21.1,
                        21.5,
                        20.7,
                        18.2,
                        21.7,
                        21.8,
                        16.8,
                        14.8,
                        18.7,
                        18.8,
                        15.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 15.5,
                "unit": "days",
                "change": -3.3,
                "change_percent": -17.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 18.79,
                "min": 14.8,
                "max": 21.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 4.4,
                        "percentage": 28.4
                },
                {
                        "category": "Category B",
                        "value": 2.13,
                        "percentage": 13.7
                },
                {
                        "category": "Category C",
                        "value": 2.99,
                        "percentage": 19.3
                },
                {
                        "category": "Category D",
                        "value": 1.77,
                        "percentage": 11.4
                },
                {
                        "category": "Other",
                        "value": 4.21,
                        "percentage": 27.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.866807",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supplier Lead Time"
        }
    },
}
