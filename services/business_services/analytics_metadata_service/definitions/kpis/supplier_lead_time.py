"""
Supplier Lead Time

The amount of time between when an order is placed with a supplier and when the order is received.
"""

SUPPLIER_LEAD_TIME = {
    "code": "SUPPLIER_LEAD_TIME",
    "name": "Supplier Lead Time",
    "description": "The amount of time between when an order is placed with a supplier and when the order is received.",
    "formula": "Average Time from Order Placement to Receipt",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Lead Time to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Lead", "Order", "Supplier"], "last_validated": "2025-11-10T13:49:33.638657"},
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
                        11.2,
                        11.9,
                        11.1,
                        12.4,
                        11.2,
                        9.2,
                        7.7,
                        9.5,
                        13.9,
                        8.7,
                        8.5,
                        10.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 10.6,
                "unit": "days",
                "change": 2.1,
                "change_percent": 24.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 10.49,
                "min": 7.7,
                "max": 13.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.78,
                        "percentage": 26.2
                },
                {
                        "category": "Segment B",
                        "value": 2.26,
                        "percentage": 21.3
                },
                {
                        "category": "Segment C",
                        "value": 1.82,
                        "percentage": 17.2
                },
                {
                        "category": "Segment D",
                        "value": 0.45,
                        "percentage": 4.2
                },
                {
                        "category": "Other",
                        "value": 3.29,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.564242",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Supplier Lead Time"
        }
    },
}
