"""
Supplier Compliance to Quality Standards

The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.
"""

SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS = {
    "code": "SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS",
    "name": "Supplier Compliance to Quality Standards",
    "description": "The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Compliance to Quality Standards to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["QualityMetric", "Supplier"], "last_validated": "2025-11-10T13:49:33.624935"},
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
                        894.03,
                        905.66,
                        922.41,
                        889.98,
                        955.45,
                        941.46,
                        1005.02,
                        1022.8,
                        975.3,
                        999.53,
                        946.66,
                        970.04
                ],
                "unit": "units"
        },
        "current": {
                "value": 970.04,
                "unit": "units",
                "change": 23.38,
                "change_percent": 2.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 952.36,
                "min": 889.98,
                "max": 1022.8,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 175.11,
                        "percentage": 18.1
                },
                {
                        "category": "Segment B",
                        "value": 235.19,
                        "percentage": 24.2
                },
                {
                        "category": "Segment C",
                        "value": 136.99,
                        "percentage": 14.1
                },
                {
                        "category": "Segment D",
                        "value": 116.53,
                        "percentage": 12.0
                },
                {
                        "category": "Other",
                        "value": 306.22,
                        "percentage": 31.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.519095",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Compliance to Quality Standards"
        }
    },
}
