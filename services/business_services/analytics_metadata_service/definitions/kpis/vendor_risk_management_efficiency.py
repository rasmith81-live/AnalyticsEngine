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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.786131"},
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
                        683.86,
                        690.07,
                        664.87,
                        709.22,
                        756.83,
                        739.77,
                        707.97,
                        665.91,
                        735.33,
                        640.43,
                        758.3,
                        672.07
                ],
                "unit": "units"
        },
        "current": {
                "value": 672.07,
                "unit": "units",
                "change": -86.23,
                "change_percent": -11.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 702.05,
                "min": 640.43,
                "max": 758.3,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 166.93,
                        "percentage": 24.8
                },
                {
                        "category": "Segment B",
                        "value": 126.5,
                        "percentage": 18.8
                },
                {
                        "category": "Segment C",
                        "value": 116.92,
                        "percentage": 17.4
                },
                {
                        "category": "Segment D",
                        "value": 43.32,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 218.4,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.948967",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Vendor Risk Management Efficiency"
        }
    },
}
