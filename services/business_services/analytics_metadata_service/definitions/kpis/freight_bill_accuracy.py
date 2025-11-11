"""
Freight Bill Accuracy

The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.
"""

FREIGHT_BILL_ACCURACY = {
    "code": "FREIGHT_BILL_ACCURACY",
    "name": "Freight Bill Accuracy",
    "description": "The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Freight Bill Accuracy to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.961317"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        179.61,
                        185.33,
                        162.5,
                        156.64,
                        215.97,
                        147.39,
                        202.81,
                        250.59,
                        266.03,
                        253.81,
                        248.52,
                        233.98
                ],
                "unit": "units"
        },
        "current": {
                "value": 233.98,
                "unit": "units",
                "change": -14.54,
                "change_percent": -5.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 208.6,
                "min": 147.39,
                "max": 266.03,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 52.0,
                        "percentage": 22.2
                },
                {
                        "category": "Segment B",
                        "value": 61.28,
                        "percentage": 26.2
                },
                {
                        "category": "Segment C",
                        "value": 36.28,
                        "percentage": 15.5
                },
                {
                        "category": "Segment D",
                        "value": 20.52,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 63.9,
                        "percentage": 27.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.003684",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Freight Bill Accuracy"
        }
    },
}
