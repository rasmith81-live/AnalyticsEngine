"""
Supplier Risk Assessment Coverage

The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.
"""

SUPPLIER_RISK_ASSESSMENT_COVERAGE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_COVERAGE",
    "name": "Supplier Risk Assessment Coverage",
    "description": "The extent to which the supply base has been assessed for risks related to social, environmental, and economic factors as per ISO 20400.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Risk Assessment Coverage to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["Supplier"], "last_validated": "2025-11-10T13:49:33.651596"},
    "required_objects": [],
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
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
                        514.63,
                        464.36,
                        427.5,
                        503.53,
                        520.65,
                        486.01,
                        538.61,
                        491.96,
                        436.29,
                        421.31,
                        461.06,
                        459.8
                ],
                "unit": "units"
        },
        "current": {
                "value": 459.8,
                "unit": "units",
                "change": -1.26,
                "change_percent": -0.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 477.14,
                "min": 421.31,
                "max": 538.61,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 82.54,
                        "percentage": 18.0
                },
                {
                        "category": "Segment B",
                        "value": 123.36,
                        "percentage": 26.8
                },
                {
                        "category": "Segment C",
                        "value": 57.3,
                        "percentage": 12.5
                },
                {
                        "category": "Segment D",
                        "value": 26.88,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 169.72,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.597338",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Supplier Risk Assessment Coverage"
        }
    },
}
