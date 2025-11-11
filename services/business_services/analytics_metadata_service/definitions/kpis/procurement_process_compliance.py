"""
Procurement Process Compliance

The adherence to established procurement policies and procedures.
"""

PROCUREMENT_PROCESS_COMPLIANCE = {
    "code": "PROCUREMENT_PROCESS_COMPLIANCE",
    "name": "Procurement Process Compliance",
    "description": "The adherence to established procurement policies and procedures.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Procurement Process Compliance to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.256950"},
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
                        1039.06,
                        967.59,
                        964.38,
                        1061.88,
                        995.4,
                        1051.6,
                        994.69,
                        916.31,
                        1057.19,
                        1035.23,
                        1009.59,
                        981.17
                ],
                "unit": "units"
        },
        "current": {
                "value": 981.17,
                "unit": "units",
                "change": -28.42,
                "change_percent": -2.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 1006.17,
                "min": 916.31,
                "max": 1061.88,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 199.48,
                        "percentage": 20.3
                },
                {
                        "category": "Segment B",
                        "value": 251.86,
                        "percentage": 25.7
                },
                {
                        "category": "Segment C",
                        "value": 114.24,
                        "percentage": 11.6
                },
                {
                        "category": "Segment D",
                        "value": 110.04,
                        "percentage": 11.2
                },
                {
                        "category": "Other",
                        "value": 305.55,
                        "percentage": 31.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.606038",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Procurement Process Compliance"
        }
    },
}
