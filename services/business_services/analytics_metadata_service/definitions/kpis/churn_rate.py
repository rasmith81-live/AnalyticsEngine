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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:49:32.695400"},
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
                        64.97,
                        54.77,
                        65.49,
                        54.9,
                        71.18,
                        71.42,
                        73.6,
                        73.26,
                        72.3,
                        57.9,
                        69.74,
                        64.59
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.59,
                "unit": "%",
                "change": -5.15,
                "change_percent": -7.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 66.18,
                "min": 54.77,
                "max": 73.6,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 21.64,
                        "percentage": 33.5
                },
                {
                        "category": "Existing Customers",
                        "value": 10.98,
                        "percentage": 17.0
                },
                {
                        "category": "VIP Customers",
                        "value": 7.79,
                        "percentage": 12.1
                },
                {
                        "category": "At-Risk Customers",
                        "value": 2.44,
                        "percentage": 3.8
                },
                {
                        "category": "Other",
                        "value": 21.74,
                        "percentage": 33.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.467379",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Churn Rate"
        }
    },
}
