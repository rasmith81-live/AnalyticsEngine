"""
Delivery Route Optimization Rate

The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.
"""

DELIVERY_ROUTE_OPTIMIZATION_RATE = {
    "code": "DELIVERY_ROUTE_OPTIMIZATION_RATE",
    "name": "Delivery Route Optimization Rate",
    "description": "The percentage of delivery routes that are optimized for cost, time, and fuel efficiency.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Delivery Route Optimization Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery"], "last_validated": "2025-11-10T13:49:32.919415"},
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
                        60.18,
                        63.45,
                        56.88,
                        67.64,
                        67.69,
                        56.39,
                        53.17,
                        52.43,
                        52.41,
                        64.24,
                        61.36,
                        49.56
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.56,
                "unit": "%",
                "change": -11.8,
                "change_percent": -19.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 58.78,
                "min": 49.56,
                "max": 67.69,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 8.48,
                        "percentage": 17.1
                },
                {
                        "category": "Segment B",
                        "value": 12.41,
                        "percentage": 25.0
                },
                {
                        "category": "Segment C",
                        "value": 7.79,
                        "percentage": 15.7
                },
                {
                        "category": "Segment D",
                        "value": 5.11,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 15.77,
                        "percentage": 31.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.904898",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Delivery Route Optimization Rate"
        }
    },
}
