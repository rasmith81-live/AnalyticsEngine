"""
Vendor Risk Management Efficiency

The efficiency of the vendor risk management process, indicating the ability to identify and mitigate risks posed by third-party vendors.
"""

VENDOR_RISK_MANAGEMENT_EFFICIENCY = {
    "code": "VENDOR_RISK_MANAGEMENT_EFFICIENCY",
    "name": "Vendor Risk Management Efficiency",
    "description": "The efficiency of the vendor risk management process, indicating the ability to identify and mitigate risks posed by third-party vendors.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Vendor Risk Management Efficiency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:43:25.226595"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        586.65,
                        651.97,
                        613.8,
                        534.55,
                        615.38,
                        582.52,
                        640.03,
                        674.2,
                        578.44,
                        547.46,
                        639.19,
                        575.06
                ],
                "unit": "units"
        },
        "current": {
                "value": 575.06,
                "unit": "units",
                "change": -64.13,
                "change_percent": -10.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 603.27,
                "min": 534.55,
                "max": 674.2,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 177.43,
                        "percentage": 30.9
                },
                {
                        "category": "Category B",
                        "value": 101.7,
                        "percentage": 17.7
                },
                {
                        "category": "Category C",
                        "value": 82.52,
                        "percentage": 14.3
                },
                {
                        "category": "Category D",
                        "value": 60.71,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 152.7,
                        "percentage": 26.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.226595",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Vendor Risk Management Efficiency"
        }
    },
}
