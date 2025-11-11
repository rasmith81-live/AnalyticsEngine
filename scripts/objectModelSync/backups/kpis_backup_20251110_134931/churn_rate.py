"""
Churn Rate

The percentage of customers or subscribers who stop using a company
"""

CHURN_RATE = {
    "code": "CHURN_RATE",
    "name": "Churn Rate",
    "description": "The percentage of customers or subscribers who stop using a company",
    "formula": "(Number of Customers Lost During Period / Number of Customers at the Start of Period) * 100",
    "calculation_formula": "(Number of Customers Lost During Period / Number of Customers at the Start of Period) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Churn Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:43:23.108768"},
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
                        64.98,
                        52.5,
                        45.86,
                        60.54,
                        63.9,
                        60.87,
                        57.39,
                        52.46,
                        54.4,
                        46.04,
                        57.69,
                        62.08
                ],
                "unit": "%"
        },
        "current": {
                "value": 62.08,
                "unit": "%",
                "change": 4.39,
                "change_percent": 7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.56,
                "min": 45.86,
                "max": 64.98,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.06,
                        "percentage": 25.9
                },
                {
                        "category": "Category B",
                        "value": 13.6,
                        "percentage": 21.9
                },
                {
                        "category": "Category C",
                        "value": 10.08,
                        "percentage": 16.2
                },
                {
                        "category": "Category D",
                        "value": 4.53,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 17.81,
                        "percentage": 28.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.108768",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Churn Rate"
        }
    },
}
