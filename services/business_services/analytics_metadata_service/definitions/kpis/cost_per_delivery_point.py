"""
Cost per Delivery Point

The cost incurred for delivering goods to each individual point.
"""

COST_PER_DELIVERY_POINT = {
    "code": "COST_PER_DELIVERY_POINT",
    "name": "Cost per Delivery Point",
    "description": "The cost incurred for delivering goods to each individual point.",
    "formula": "Total Delivery Costs / Total Number of Delivery Points",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Delivery Point to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.726817"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        109,
                        120,
                        96,
                        103,
                        110,
                        71,
                        107,
                        72,
                        106,
                        80,
                        88,
                        82
                ],
                "unit": "count"
        },
        "current": {
                "value": 82,
                "unit": "count",
                "change": -6,
                "change_percent": -6.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 95.33,
                "min": 71,
                "max": 120,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 20.26,
                        "percentage": 24.7
                },
                {
                        "category": "Segment B",
                        "value": 16.04,
                        "percentage": 19.6
                },
                {
                        "category": "Segment C",
                        "value": 13.49,
                        "percentage": 16.5
                },
                {
                        "category": "Segment D",
                        "value": 3.68,
                        "percentage": 4.5
                },
                {
                        "category": "Other",
                        "value": 28.53,
                        "percentage": 34.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.532597",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Delivery Point"
        }
    },
}
