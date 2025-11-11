"""
Requisition-to-Order Time

The time elapsed from when a purchase requisition is initiated to when the purchase order is created.
"""

REQUISITION_TO_ORDER_TIME = {
    "code": "REQUISITION_TO_ORDER_TIME",
    "name": "Requisition-to-Order Time",
    "description": "The time elapsed from when a purchase requisition is initiated to when the purchase order is created.",
    "formula": "Total Time from Requisition to Purchase Order / Number of Requisitions",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Requisition-to-Order Time to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.339196"},
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
                        152,
                        161,
                        165,
                        185,
                        181,
                        175,
                        187,
                        190,
                        181,
                        175,
                        161,
                        185
                ],
                "unit": "count"
        },
        "current": {
                "value": 185,
                "unit": "count",
                "change": 24,
                "change_percent": 14.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 174.83,
                "min": 152,
                "max": 190,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 59.72,
                        "percentage": 32.3
                },
                {
                        "category": "Category B",
                        "value": 23.78,
                        "percentage": 12.9
                },
                {
                        "category": "Category C",
                        "value": 20.92,
                        "percentage": 11.3
                },
                {
                        "category": "Category D",
                        "value": 12.28,
                        "percentage": 6.6
                },
                {
                        "category": "Other",
                        "value": 68.3,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.077637",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Requisition-to-Order Time"
        }
    },
}
