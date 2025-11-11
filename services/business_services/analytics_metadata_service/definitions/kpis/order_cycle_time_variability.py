"""
Order Cycle Time Variability

The variation in the time it takes to complete different orders, indicating the consistency of the buying process.
"""

ORDER_CYCLE_TIME_VARIABILITY = {
    "code": "ORDER_CYCLE_TIME_VARIABILITY",
    "name": "Order Cycle Time Variability",
    "description": "The variation in the time it takes to complete different orders, indicating the consistency of the buying process.",
    "formula": "Standard Deviation of Order Cycle Time / Average Order Cycle Time",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Cycle Time Variability to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.115870"},
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
                        3.5,
                        3.8,
                        6.9,
                        3.8,
                        2.5,
                        10.1,
                        6.3,
                        4.1,
                        4.4,
                        4.6,
                        8.9,
                        7.9
                ],
                "unit": "days"
        },
        "current": {
                "value": 7.9,
                "unit": "days",
                "change": -1.0,
                "change_percent": -11.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 5.57,
                "min": 2.5,
                "max": 10.1,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 1.89,
                        "percentage": 23.9
                },
                {
                        "category": "Segment B",
                        "value": 0.99,
                        "percentage": 12.5
                },
                {
                        "category": "Segment C",
                        "value": 0.87,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 0.94,
                        "percentage": 11.9
                },
                {
                        "category": "Other",
                        "value": 3.21,
                        "percentage": 40.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.307266",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Order Cycle Time Variability"
        }
    },
}
