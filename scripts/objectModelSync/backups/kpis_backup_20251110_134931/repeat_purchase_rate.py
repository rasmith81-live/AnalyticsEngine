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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:43:24.073956"},
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
                        53.62,
                        48.56,
                        47.88,
                        59.9,
                        61.04,
                        52.61,
                        49.72,
                        54.8,
                        56.44,
                        48.82,
                        56.04,
                        61.44
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.44,
                "unit": "%",
                "change": 5.4,
                "change_percent": 9.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 54.24,
                "min": 47.88,
                "max": 61.44,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.59,
                        "percentage": 22.1
                },
                {
                        "category": "Category B",
                        "value": 8.01,
                        "percentage": 13.0
                },
                {
                        "category": "Category C",
                        "value": 11.3,
                        "percentage": 18.4
                },
                {
                        "category": "Category D",
                        "value": 3.43,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 25.11,
                        "percentage": 40.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.073956",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Repeat Purchase Rate"
        }
    },
}
