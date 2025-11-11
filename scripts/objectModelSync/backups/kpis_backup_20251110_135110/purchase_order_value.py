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
                        159,
                        148,
                        163,
                        167,
                        169,
                        181,
                        170,
                        174,
                        178,
                        197,
                        165,
                        186
                ],
                "unit": "count"
        },
        "current": {
                "value": 186,
                "unit": "count",
                "change": 21,
                "change_percent": 12.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 171.42,
                "min": 148,
                "max": 197,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 49.99,
                        "percentage": 26.9
                },
                {
                        "category": "Category B",
                        "value": 26.02,
                        "percentage": 14.0
                },
                {
                        "category": "Category C",
                        "value": 23.7,
                        "percentage": 12.7
                },
                {
                        "category": "Category D",
                        "value": 22.06,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 64.23,
                        "percentage": 34.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.016624",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Purchase Order Value"
        }
    },
}
