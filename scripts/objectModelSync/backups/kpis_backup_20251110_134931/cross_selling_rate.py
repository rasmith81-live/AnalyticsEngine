"""
Cross-selling Rate

The percentage of customers who have been sold additional, complementary products or services.
"""

CROSS_SELLING_RATE = {
    "code": "CROSS_SELLING_RATE",
    "name": "Cross-selling Rate",
    "description": "The percentage of customers who have been sold additional, complementary products or services.",
    "formula": "(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Purchasing Additional Offerings / Total Number of Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cross-selling Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product"], "last_validated": "2025-11-10T13:43:23.198519"},
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
                        67.12,
                        78.32,
                        81.58,
                        79.78,
                        64.08,
                        70.44,
                        65.4,
                        76.87,
                        80.12,
                        73.37,
                        65.4,
                        74.92
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.92,
                "unit": "%",
                "change": 9.52,
                "change_percent": 14.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73.12,
                "min": 64.08,
                "max": 81.58,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 13.82,
                        "percentage": 18.4
                },
                {
                        "category": "Category B",
                        "value": 18.44,
                        "percentage": 24.6
                },
                {
                        "category": "Category C",
                        "value": 7.9,
                        "percentage": 10.5
                },
                {
                        "category": "Category D",
                        "value": 7.28,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 27.48,
                        "percentage": 36.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.198519",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Cross-selling Rate"
        }
    },
}
