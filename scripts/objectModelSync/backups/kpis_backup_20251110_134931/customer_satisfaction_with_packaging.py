"""
Customer Satisfaction with Packaging

The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.
"""

CUSTOMER_SATISFACTION_WITH_PACKAGING = {
    "code": "CUSTOMER_SATISFACTION_WITH_PACKAGING",
    "name": "Customer Satisfaction with Packaging",
    "description": "The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Satisfaction with Packaging to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Delivery", "PurchaseOrder", "QualityMetric"], "last_validated": "2025-11-10T13:43:23.356105"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        863.76,
                        921.0,
                        918.9,
                        823.59,
                        875.91,
                        810.58,
                        780.8,
                        876.83,
                        841.99,
                        882.76,
                        839.12,
                        832.4
                ],
                "unit": "units"
        },
        "current": {
                "value": 832.4,
                "unit": "units",
                "change": -6.72,
                "change_percent": -0.8,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 855.64,
                "min": 780.8,
                "max": 921.0,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 209.21,
                        "percentage": 25.1
                },
                {
                        "category": "Category B",
                        "value": 126.35,
                        "percentage": 15.2
                },
                {
                        "category": "Category C",
                        "value": 83.97,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 114.91,
                        "percentage": 13.8
                },
                {
                        "category": "Other",
                        "value": 297.96,
                        "percentage": 35.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.356105",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Satisfaction with Packaging"
        }
    },
}
