"""
Cost per Shipment

The total cost divided by the number of shipments.
"""

COST_PER_SHIPMENT = {
    "code": "COST_PER_SHIPMENT",
    "name": "Cost per Shipment",
    "description": "The total cost divided by the number of shipments.",
    "formula": "Total Shipping Costs / Total Number of Shipments",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost per Shipment to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:32.733409"},
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
                        174,
                        173,
                        169,
                        168,
                        169,
                        175,
                        155,
                        189,
                        178,
                        187,
                        199,
                        187
                ],
                "unit": "count"
        },
        "current": {
                "value": 187,
                "unit": "count",
                "change": -12,
                "change_percent": -6.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 176.92,
                "min": 155,
                "max": 199,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 35.55,
                        "percentage": 19.0
                },
                {
                        "category": "Segment B",
                        "value": 47.87,
                        "percentage": 25.6
                },
                {
                        "category": "Segment C",
                        "value": 30.27,
                        "percentage": 16.2
                },
                {
                        "category": "Segment D",
                        "value": 19.1,
                        "percentage": 10.2
                },
                {
                        "category": "Other",
                        "value": 54.21,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.549294",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost per Shipment"
        }
    },
}
