"""
Receiving Efficiency

The speed and accuracy of processing incoming goods into the warehouse.
"""

RECEIVING_EFFICIENCY = {
    "code": "RECEIVING_EFFICIENCY",
    "name": "Receiving Efficiency",
    "description": "The speed and accuracy of processing incoming goods into the warehouse.",
    "formula": "Total Time Taken for Receiving / Total Number of Shipments Received",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Receiving Efficiency to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Shipment", "Warehouse"], "last_validated": "2025-11-10T13:49:33.318987"},
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
                        336,
                        367,
                        333,
                        351,
                        368,
                        364,
                        375,
                        358,
                        369,
                        374,
                        361,
                        340
                ],
                "unit": "count"
        },
        "current": {
                "value": 340,
                "unit": "count",
                "change": -21,
                "change_percent": -5.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 358.0,
                "min": 333,
                "max": 375,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 61.74,
                        "percentage": 18.2
                },
                {
                        "category": "Segment B",
                        "value": 50.38,
                        "percentage": 14.8
                },
                {
                        "category": "Segment C",
                        "value": 39.98,
                        "percentage": 11.8
                },
                {
                        "category": "Segment D",
                        "value": 55.26,
                        "percentage": 16.3
                },
                {
                        "category": "Other",
                        "value": 132.64,
                        "percentage": 39.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.750821",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Receiving Efficiency"
        }
    },
}
