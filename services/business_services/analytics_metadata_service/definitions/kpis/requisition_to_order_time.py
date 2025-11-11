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
                        215,
                        242,
                        224,
                        251,
                        245,
                        244,
                        216,
                        241,
                        211,
                        204,
                        226,
                        215
                ],
                "unit": "count"
        },
        "current": {
                "value": 215,
                "unit": "count",
                "change": -11,
                "change_percent": -4.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 227.83,
                "min": 204,
                "max": 251,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 61.14,
                        "percentage": 28.4
                },
                {
                        "category": "Segment B",
                        "value": 47.86,
                        "percentage": 22.3
                },
                {
                        "category": "Segment C",
                        "value": 28.13,
                        "percentage": 13.1
                },
                {
                        "category": "Segment D",
                        "value": 20.91,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 56.96,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.795893",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Requisition-to-Order Time"
        }
    },
}
