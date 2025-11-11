"""
Fulfillment Cost per Order

The total cost to fulfill an average order, including labor, materials, and overhead.
"""

FULFILLMENT_COST_PER_ORDER = {
    "code": "FULFILLMENT_COST_PER_ORDER",
    "name": "Fulfillment Cost per Order",
    "description": "The total cost to fulfill an average order, including labor, materials, and overhead.",
    "formula": "Total Fulfillment Costs / Total Number of Orders Fulfilled",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Fulfillment Cost per Order to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:32.963577"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        500,
                        511,
                        482,
                        507,
                        478,
                        503,
                        494,
                        480,
                        498,
                        503,
                        495,
                        478
                ],
                "unit": "count"
        },
        "current": {
                "value": 478,
                "unit": "count",
                "change": -17,
                "change_percent": -3.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 494.08,
                "min": 478,
                "max": 511,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 167.3,
                        "percentage": 35.0
                },
                {
                        "category": "Segment B",
                        "value": 72.61,
                        "percentage": 15.2
                },
                {
                        "category": "Segment C",
                        "value": 46.25,
                        "percentage": 9.7
                },
                {
                        "category": "Segment D",
                        "value": 29.4,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 162.44,
                        "percentage": 34.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.011010",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Fulfillment Cost per Order"
        }
    },
}
