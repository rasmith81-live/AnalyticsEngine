"""
Purchase Order Processing Cost

The total cost associated with processing each purchase order, including labor, overhead, and technology.
"""

PURCHASE_ORDER_PROCESSING_COST = {
    "code": "PURCHASE_ORDER_PROCESSING_COST",
    "name": "Purchase Order Processing Cost",
    "description": "The total cost associated with processing each purchase order, including labor, overhead, and technology.",
    "formula": "Total Cost of Processing Purchase Orders / Total Number of Purchase Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Purchase Order Processing Cost to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.300397"},
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
                        394,
                        401,
                        414,
                        399,
                        422,
                        410,
                        430,
                        421,
                        403,
                        423,
                        437,
                        407
                ],
                "unit": "count"
        },
        "current": {
                "value": 407,
                "unit": "count",
                "change": -30,
                "change_percent": -6.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 413.42,
                "min": 394,
                "max": 437,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 117.76,
                        "percentage": 28.9
                },
                {
                        "category": "Segment B",
                        "value": 79.69,
                        "percentage": 19.6
                },
                {
                        "category": "Segment C",
                        "value": 67.9,
                        "percentage": 16.7
                },
                {
                        "category": "Segment D",
                        "value": 21.36,
                        "percentage": 5.2
                },
                {
                        "category": "Other",
                        "value": 120.29,
                        "percentage": 29.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.704083",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Purchase Order Processing Cost"
        }
    },
}
