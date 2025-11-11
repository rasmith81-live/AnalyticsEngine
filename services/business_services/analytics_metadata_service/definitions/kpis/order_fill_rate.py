"""
Order Fill Rate

The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.
"""

ORDER_FILL_RATE = {
    "code": "ORDER_FILL_RATE",
    "name": "Order Fill Rate",
    "description": "The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Fill Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "Supplier"], "last_validated": "2025-11-10T13:49:33.118008"},
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
                        56.61,
                        39.4,
                        43.2,
                        52.02,
                        55.26,
                        50.87,
                        45.56,
                        54.27,
                        41.34,
                        39.11,
                        55.85,
                        49.47
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.47,
                "unit": "%",
                "change": -6.38,
                "change_percent": -11.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.58,
                "min": 39.11,
                "max": 56.61,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.21,
                        "percentage": 22.7
                },
                {
                        "category": "Segment B",
                        "value": 10.17,
                        "percentage": 20.6
                },
                {
                        "category": "Segment C",
                        "value": 5.45,
                        "percentage": 11.0
                },
                {
                        "category": "Segment D",
                        "value": 3.55,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 19.09,
                        "percentage": 38.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.309856",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Fill Rate"
        }
    },
}
