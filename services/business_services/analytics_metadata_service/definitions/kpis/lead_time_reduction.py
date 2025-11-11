"""
Lead Time Reduction

The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.
"""

LEAD_TIME_REDUCTION = {
    "code": "LEAD_TIME_REDUCTION",
    "name": "Lead Time Reduction",
    "description": "The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Time Reduction to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.014589"},
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
                        16.8,
                        14.7,
                        10.4,
                        9.0,
                        11.3,
                        9.2,
                        13.6,
                        15.9,
                        11.6,
                        11.7,
                        16.1,
                        10.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 10.6,
                "unit": "days",
                "change": -5.5,
                "change_percent": -34.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 12.58,
                "min": 9.0,
                "max": 16.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.94,
                        "percentage": 27.7
                },
                {
                        "category": "Segment B",
                        "value": 2.22,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 1.81,
                        "percentage": 17.1
                },
                {
                        "category": "Segment D",
                        "value": 0.68,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 2.95,
                        "percentage": 27.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.129291",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Lead Time Reduction"
        }
    },
}
