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
                        497,
                        491,
                        465,
                        487,
                        478,
                        498,
                        470,
                        481,
                        456,
                        498,
                        497,
                        497
                ],
                "unit": "count"
        },
        "current": {
                "value": 497,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 484.58,
                "min": 456,
                "max": 498,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 146.18,
                        "percentage": 29.4
                },
                {
                        "category": "Category B",
                        "value": 89.83,
                        "percentage": 18.1
                },
                {
                        "category": "Category C",
                        "value": 45.59,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 31.07,
                        "percentage": 6.3
                },
                {
                        "category": "Other",
                        "value": 184.33,
                        "percentage": 37.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.612108",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Loading Efficiency"
        }
    },
}
