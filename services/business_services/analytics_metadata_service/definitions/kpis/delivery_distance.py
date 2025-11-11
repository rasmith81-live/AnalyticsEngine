"""
Average Delivery Distance

The average distance covered per delivery.
"""

DELIVERY_DISTANCE = {
    "code": "DELIVERY_DISTANCE",
    "name": "Average Delivery Distance",
    "description": "The average distance covered per delivery.",
    "formula": "Total Distance for All Deliveries / Number of Deliveries",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Delivery Distance to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:49:32.917392"},
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
                        246,
                        270,
                        261,
                        229,
                        261,
                        225,
                        273,
                        223,
                        267,
                        252,
                        239,
                        230
                ],
                "unit": "count"
        },
        "current": {
                "value": 230,
                "unit": "count",
                "change": -9,
                "change_percent": -3.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 248.0,
                "min": 223,
                "max": 273,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 73.67,
                        "percentage": 32.0
                },
                {
                        "category": "Segment B",
                        "value": 52.48,
                        "percentage": 22.8
                },
                {
                        "category": "Segment C",
                        "value": 16.07,
                        "percentage": 7.0
                },
                {
                        "category": "Segment D",
                        "value": 11.31,
                        "percentage": 4.9
                },
                {
                        "category": "Other",
                        "value": 76.47,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.899687",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Delivery Distance"
        }
    },
}
