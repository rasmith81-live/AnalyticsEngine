"""
Pipeline Growth Rate

The rate at which the sales pipeline is growing, indicating the potential for future sales.
"""

PIPELINE_GROWTH_RATE = {
    "code": "PIPELINE_GROWTH_RATE",
    "name": "Pipeline Growth Rate",
    "description": "The rate at which the sales pipeline is growing, indicating the potential for future sales.",
    "formula": "((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
    "calculation_formula": "((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Pipeline Growth Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.241190"},
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
                        72.36,
                        66.46,
                        80.38,
                        76.46,
                        70.07,
                        67.06,
                        83.06,
                        81.24,
                        67.78,
                        80.18,
                        65.26,
                        67.57
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.57,
                "unit": "%",
                "change": 2.31,
                "change_percent": 3.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.16,
                "min": 65.26,
                "max": 83.06,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 16.42,
                        "percentage": 24.3
                },
                {
                        "category": "Segment B",
                        "value": 12.3,
                        "percentage": 18.2
                },
                {
                        "category": "Segment C",
                        "value": 10.29,
                        "percentage": 15.2
                },
                {
                        "category": "Segment D",
                        "value": 6.2,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 22.36,
                        "percentage": 33.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.571825",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Pipeline Growth Rate"
        }
    },
}
