"""
Opportunity Pipeline

The number of opportunities in the pipeline and their value.
"""

OPPORTUNITY_PIPELINE = {
    "code": "OPPORTUNITY_PIPELINE",
    "name": "Opportunity Pipeline",
    "description": "The number of opportunities in the pipeline and their value.",
    "formula": "Sum of All Opportunities at Various Stages of the Sales Cycle",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Opportunity Pipeline to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.106259"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        876.03,
                        820.35,
                        790.19,
                        774.26,
                        833.67,
                        750.96,
                        793.33,
                        797.13,
                        806.82,
                        787.89,
                        796.2,
                        857.88
                ],
                "unit": "units"
        },
        "current": {
                "value": 857.88,
                "unit": "units",
                "change": 61.68,
                "change_percent": 7.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 807.06,
                "min": 750.96,
                "max": 876.03,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 233.5,
                        "percentage": 27.2
                },
                {
                        "category": "Channel Sales",
                        "value": 208.56,
                        "percentage": 24.3
                },
                {
                        "category": "Online Sales",
                        "value": 97.62,
                        "percentage": 11.4
                },
                {
                        "category": "Enterprise Sales",
                        "value": 33.98,
                        "percentage": 4.0
                },
                {
                        "category": "Other",
                        "value": 284.22,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.293284",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Opportunity Pipeline"
        }
    },
}
