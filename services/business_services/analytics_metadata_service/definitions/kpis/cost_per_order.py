"""
Cost per Order

The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.
"""

COST_PER_ORDER = {
    "code": "COST_PER_ORDER",
    "name": "Cost per Order",
    "description": "The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.",
    "formula": "Total Cost of Procurement Operations / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Order to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.729473"},
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
                        319,
                        325,
                        351,
                        360,
                        335,
                        335,
                        349,
                        331,
                        318,
                        331,
                        362,
                        322
                ],
                "unit": "count"
        },
        "current": {
                "value": 322,
                "unit": "count",
                "change": -40,
                "change_percent": -11.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 336.5,
                "min": 318,
                "max": 362,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 61.01,
                        "percentage": 18.9
                },
                {
                        "category": "Segment B",
                        "value": 46.16,
                        "percentage": 14.3
                },
                {
                        "category": "Segment C",
                        "value": 55.35,
                        "percentage": 17.2
                },
                {
                        "category": "Segment D",
                        "value": 46.03,
                        "percentage": 14.3
                },
                {
                        "category": "Other",
                        "value": 113.45,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.537181",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Order"
        }
    },
}
