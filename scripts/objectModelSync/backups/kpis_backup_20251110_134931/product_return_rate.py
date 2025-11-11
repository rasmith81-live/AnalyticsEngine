"""
Product Return Rate

The percentage of products that are returned by customers, which can signal issues with product satisfaction or quality.
"""

PRODUCT_RETURN_RATE = {
    "code": "PRODUCT_RETURN_RATE",
    "name": "Product Return Rate",
    "description": "The percentage of products that are returned by customers, which can signal issues with product satisfaction or quality.",
    "formula": "(Number of Products Returned / Number of Products Sold) * 100",
    "calculation_formula": "(Number of Products Returned / Number of Products Sold) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Return Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product", "QualityMetric", "Return"], "last_validated": "2025-11-10T13:43:23.981102"},
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
                        65.94,
                        64.33,
                        56.15,
                        64.0,
                        60.59,
                        67.84,
                        73.7,
                        69.3,
                        68.04,
                        63.24,
                        59.31,
                        61.04
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.04,
                "unit": "%",
                "change": 1.73,
                "change_percent": 2.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 64.46,
                "min": 56.15,
                "max": 73.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.68,
                        "percentage": 15.9
                },
                {
                        "category": "Category B",
                        "value": 17.29,
                        "percentage": 28.3
                },
                {
                        "category": "Category C",
                        "value": 6.18,
                        "percentage": 10.1
                },
                {
                        "category": "Category D",
                        "value": 4.78,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 23.11,
                        "percentage": 37.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.981102",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Product Return Rate"
        }
    },
}
