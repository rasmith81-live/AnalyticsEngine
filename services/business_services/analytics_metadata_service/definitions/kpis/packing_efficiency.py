"""
Packing Efficiency

The speed and accuracy with which items are packed for shipment.
"""

PACKING_EFFICIENCY = {
    "code": "PACKING_EFFICIENCY",
    "name": "Packing Efficiency",
    "description": "The speed and accuracy with which items are packed for shipment.",
    "formula": "Total Time Taken for Packing / Total Number of Orders Packed",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order", "Product", "Shipment"], "last_validated": "2025-11-10T13:49:33.153569"},
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
                        511,
                        487,
                        502,
                        506,
                        492,
                        475,
                        488,
                        470,
                        472,
                        471,
                        505,
                        484
                ],
                "unit": "count"
        },
        "current": {
                "value": 484,
                "unit": "count",
                "change": -21,
                "change_percent": -4.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 488.58,
                "min": 470,
                "max": 511,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 163.41,
                        "percentage": 33.8
                },
                {
                        "category": "Segment B",
                        "value": 106.8,
                        "percentage": 22.1
                },
                {
                        "category": "Segment C",
                        "value": 43.98,
                        "percentage": 9.1
                },
                {
                        "category": "Segment D",
                        "value": 45.01,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 124.8,
                        "percentage": 25.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.392858",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Packing Efficiency"
        }
    },
}
