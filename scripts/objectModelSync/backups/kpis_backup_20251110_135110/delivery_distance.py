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
                        127,
                        131,
                        123,
                        122,
                        129,
                        111,
                        108,
                        124,
                        117,
                        103,
                        131,
                        137
                ],
                "unit": "count"
        },
        "current": {
                "value": 137,
                "unit": "count",
                "change": 6,
                "change_percent": 4.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 121.92,
                "min": 103,
                "max": 137,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 28.59,
                        "percentage": 20.9
                },
                {
                        "category": "Category B",
                        "value": 25.08,
                        "percentage": 18.3
                },
                {
                        "category": "Category C",
                        "value": 21.89,
                        "percentage": 16.0
                },
                {
                        "category": "Category D",
                        "value": 9.94,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 51.5,
                        "percentage": 37.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.422101",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Delivery Distance"
        }
    },
}
