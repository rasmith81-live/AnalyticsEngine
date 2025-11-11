"""
Time to Receive

The time it takes to accept, process, and store incoming goods.
"""

TIME_TO_RECEIVE = {
    "code": "TIME_TO_RECEIVE",
    "name": "Time to Receive",
    "description": "The time it takes to accept, process, and store incoming goods.",
    "formula": "Total Time Taken for Receiving / Total Number of Deliveries",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Receive to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.721071"},
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
                        412,
                        406,
                        402,
                        398,
                        425,
                        418,
                        385,
                        376,
                        398,
                        406,
                        400,
                        415
                ],
                "unit": "count"
        },
        "current": {
                "value": 415,
                "unit": "count",
                "change": 15,
                "change_percent": 3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 403.42,
                "min": 376,
                "max": 425,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 94.04,
                        "percentage": 22.7
                },
                {
                        "category": "Segment B",
                        "value": 83.8,
                        "percentage": 20.2
                },
                {
                        "category": "Segment C",
                        "value": 46.6,
                        "percentage": 11.2
                },
                {
                        "category": "Segment D",
                        "value": 45.21,
                        "percentage": 10.9
                },
                {
                        "category": "Other",
                        "value": 145.35,
                        "percentage": 35.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.786876",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Receive"
        }
    },
}
