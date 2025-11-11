"""
Supplier Diversity Rate

The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400
"""

SUPPLIER_DIVERSITY_RATE = {
    "code": "SUPPLIER_DIVERSITY_RATE",
    "name": "Supplier Diversity Rate",
    "description": "The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 20400",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Supplier Diversity Rate to be added.",
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
    "metadata_": {"modules": ["ISO_20400"], "required_objects": ["PurchaseOrder", "Supplier"], "last_validated": "2025-11-10T13:49:33.632723"},
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
                        33.82,
                        30.46,
                        41.88,
                        32.53,
                        37.16,
                        31.74,
                        30.87,
                        38.96,
                        44.02,
                        46.11,
                        45.21,
                        43.09
                ],
                "unit": "%"
        },
        "current": {
                "value": 43.09,
                "unit": "%",
                "change": -2.12,
                "change_percent": -4.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 37.99,
                "min": 30.46,
                "max": 46.11,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.45,
                        "percentage": 33.5
                },
                {
                        "category": "Segment B",
                        "value": 5.79,
                        "percentage": 13.4
                },
                {
                        "category": "Segment C",
                        "value": 7.01,
                        "percentage": 16.3
                },
                {
                        "category": "Segment D",
                        "value": 2.47,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 13.37,
                        "percentage": 31.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.541292",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Supplier Diversity Rate"
        }
    },
}
