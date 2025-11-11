"""
Opportunity-to-Close Rate

The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team
"""

OPPORTUNITY_TO_CLOSE_RATE = {
    "code": "OPPORTUNITY_TO_CLOSE_RATE",
    "name": "Opportunity-to-Close Rate",
    "description": "The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team",
    "formula": "(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
    "calculation_formula": "(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Opportunity-to-Close Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Opportunity", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.731930"},
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
                        41.11,
                        50.76,
                        37.87,
                        50.02,
                        38.49,
                        48.9,
                        53.03,
                        39.31,
                        47.65,
                        53.71,
                        37.8,
                        45.96
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.96,
                "unit": "%",
                "change": 8.16,
                "change_percent": 21.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 45.38,
                "min": 37.8,
                "max": 53.71,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 12.12,
                        "percentage": 26.4
                },
                {
                        "category": "Category B",
                        "value": 5.65,
                        "percentage": 12.3
                },
                {
                        "category": "Category C",
                        "value": 8.73,
                        "percentage": 19.0
                },
                {
                        "category": "Category D",
                        "value": 3.33,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 16.13,
                        "percentage": 35.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.731930",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Opportunity-to-Close Rate"
        }
    },
}
