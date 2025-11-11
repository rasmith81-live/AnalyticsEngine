"""
Repeat Purchase Rate

The percentage of customers who make more than one purchase, which can indicate customer loyalty and satisfaction with a company
"""

REPEAT_PURCHASE_RATE = {
    "code": "REPEAT_PURCHASE_RATE",
    "name": "Repeat Purchase Rate",
    "description": "The percentage of customers who make more than one purchase, which can indicate customer loyalty and satisfaction with a company",
    "formula": "(Number of Customers with Multiple Purchases / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers with Multiple Purchases / Total Number of Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Repeat Purchase Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:49:33.337096"},
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
                        68.85,
                        79.64,
                        73.29,
                        67.34,
                        61.78,
                        79.57,
                        73.91,
                        72.59,
                        71.29,
                        78.85,
                        71.61,
                        77.27
                ],
                "unit": "%"
        },
        "current": {
                "value": 77.27,
                "unit": "%",
                "change": 5.66,
                "change_percent": 7.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.0,
                "min": 61.78,
                "max": 79.64,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 21.73,
                        "percentage": 28.1
                },
                {
                        "category": "Existing Customers",
                        "value": 17.72,
                        "percentage": 22.9
                },
                {
                        "category": "VIP Customers",
                        "value": 11.0,
                        "percentage": 14.2
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.64,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 22.18,
                        "percentage": 28.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.792021",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Repeat Purchase Rate"
        }
    },
}
