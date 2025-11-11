"""
Loading Efficiency

The speed and accuracy with which goods are loaded into outbound vehicles.
"""

LOADING_EFFICIENCY = {
    "code": "LOADING_EFFICIENCY",
    "name": "Loading Efficiency",
    "description": "The speed and accuracy with which goods are loaded into outbound vehicles.",
    "formula": "Total Time Taken for Loading / Total Number of Shipments Loaded",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Loading Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Shipment"], "last_validated": "2025-11-10T13:49:33.022325"},
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
                        59,
                        53,
                        68,
                        37,
                        85,
                        47,
                        65,
                        40,
                        47,
                        75,
                        84,
                        58
                ],
                "unit": "count"
        },
        "current": {
                "value": 58,
                "unit": "count",
                "change": -26,
                "change_percent": -31.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 59.83,
                "min": 37,
                "max": 85,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.92,
                        "percentage": 20.6
                },
                {
                        "category": "Segment B",
                        "value": 14.87,
                        "percentage": 25.6
                },
                {
                        "category": "Segment C",
                        "value": 5.09,
                        "percentage": 8.8
                },
                {
                        "category": "Segment D",
                        "value": 6.37,
                        "percentage": 11.0
                },
                {
                        "category": "Other",
                        "value": 19.75,
                        "percentage": 34.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.152872",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Loading Efficiency"
        }
    },
}
