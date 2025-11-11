"""
Purchase Order Accuracy

The degree to which purchase order information is accurate and free from errors.
"""

PURCHASE_ORDER_ACCURACY = {
    "code": "PURCHASE_ORDER_ACCURACY",
    "name": "Purchase Order Accuracy",
    "description": "The degree to which purchase order information is accurate and free from errors.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Purchase Order Accuracy to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.296017"},
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
                        378.6,
                        430.25,
                        517.36,
                        492.63,
                        420.05,
                        447.12,
                        505.33,
                        408.77,
                        431.31,
                        438.47,
                        381.81,
                        389.43
                ],
                "unit": "units"
        },
        "current": {
                "value": 389.43,
                "unit": "units",
                "change": 7.62,
                "change_percent": 2.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 436.76,
                "min": 378.6,
                "max": 517.36,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 80.04,
                        "percentage": 20.6
                },
                {
                        "category": "Segment B",
                        "value": 77.04,
                        "percentage": 19.8
                },
                {
                        "category": "Segment C",
                        "value": 43.58,
                        "percentage": 11.2
                },
                {
                        "category": "Segment D",
                        "value": 24.97,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 163.8,
                        "percentage": 42.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.696071",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Purchase Order Accuracy"
        }
    },
}
