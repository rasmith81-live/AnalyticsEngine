"""
Average Purchase Order Value

The average value of purchase orders over a specific period, indicating purchasing patterns or trends.
"""

PURCHASE_ORDER_VALUE = {
    "code": "PURCHASE_ORDER_VALUE",
    "name": "Average Purchase Order Value",
    "description": "The average value of purchase orders over a specific period, indicating purchasing patterns or trends.",
    "formula": "Total Spend / Total Number of Purchase Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Purchase Order Value to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.301439"},
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
                        397,
                        393,
                        362,
                        383,
                        385,
                        400,
                        363,
                        395,
                        376,
                        394,
                        380,
                        397
                ],
                "unit": "count"
        },
        "current": {
                "value": 397,
                "unit": "count",
                "change": 17,
                "change_percent": 4.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 385.42,
                "min": 362,
                "max": 400,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 59.82,
                        "percentage": 15.1
                },
                {
                        "category": "Segment B",
                        "value": 70.08,
                        "percentage": 17.7
                },
                {
                        "category": "Segment C",
                        "value": 73.28,
                        "percentage": 18.5
                },
                {
                        "category": "Segment D",
                        "value": 45.63,
                        "percentage": 11.5
                },
                {
                        "category": "Other",
                        "value": 148.19,
                        "percentage": 37.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.707897",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Purchase Order Value"
        }
    },
}
