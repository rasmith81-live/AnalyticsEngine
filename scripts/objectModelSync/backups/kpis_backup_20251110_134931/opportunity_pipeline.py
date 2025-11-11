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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.729755"},
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
                        812.44,
                        808.95,
                        833.21,
                        721.08,
                        825.96,
                        748.71,
                        729.75,
                        818.87,
                        838.54,
                        715.09,
                        738.29,
                        724.09
                ],
                "unit": "units"
        },
        "current": {
                "value": 724.09,
                "unit": "units",
                "change": -14.2,
                "change_percent": -1.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 776.25,
                "min": 715.09,
                "max": 838.54,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 187.63,
                        "percentage": 25.9
                },
                {
                        "category": "Category B",
                        "value": 116.53,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 98.97,
                        "percentage": 13.7
                },
                {
                        "category": "Category D",
                        "value": 72.98,
                        "percentage": 10.1
                },
                {
                        "category": "Other",
                        "value": 247.98,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.729755",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Opportunity Pipeline"
        }
    },
}
