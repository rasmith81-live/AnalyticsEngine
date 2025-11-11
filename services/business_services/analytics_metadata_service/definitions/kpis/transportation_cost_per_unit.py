"""
Transportation Cost per Unit

The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.
"""

TRANSPORTATION_COST_PER_UNIT = {
    "code": "TRANSPORTATION_COST_PER_UNIT",
    "name": "Transportation Cost per Unit",
    "description": "The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.",
    "formula": "Total Transportation Costs / Total Number of Units Shipped",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Transportation Cost per Unit to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.753626"},
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
                        380,
                        349,
                        367,
                        351,
                        378,
                        336,
                        373,
                        348,
                        374,
                        337,
                        369,
                        380
                ],
                "unit": "count"
        },
        "current": {
                "value": 380,
                "unit": "count",
                "change": 11,
                "change_percent": 3.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 361.83,
                "min": 336,
                "max": 380,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 63.25,
                        "percentage": 16.6
                },
                {
                        "category": "Segment B",
                        "value": 95.43,
                        "percentage": 25.1
                },
                {
                        "category": "Segment C",
                        "value": 44.93,
                        "percentage": 11.8
                },
                {
                        "category": "Segment D",
                        "value": 36.22,
                        "percentage": 9.5
                },
                {
                        "category": "Other",
                        "value": 140.17,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.877463",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Transportation Cost per Unit"
        }
    },
}
