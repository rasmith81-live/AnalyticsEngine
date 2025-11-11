"""
Profit Margin per Sale

The percentage of profit made on each sale, indicating the profitability of the sales process.
"""

PROFIT_MARGIN_PER_SALE = {
    "code": "PROFIT_MARGIN_PER_SALE",
    "name": "Profit Margin per Sale",
    "description": "The percentage of profit made on each sale, indicating the profitability of the sales process.",
    "formula": "Base: (Revenue - Cost of Goods Sold) per Sale. Percentage: ((Revenue - COGS) / Revenue) \u00d7 100. Aggregations: AVG(profit_margin), MEDIAN(profit_margin), SUM(profit), MIN(profit_margin), MAX(profit_margin)",
    "calculation_formula": "Base: (Revenue - Cost of Goods Sold) per Sale. Percentage: ((Revenue - COGS) / Revenue) \u00d7 100. Aggregations: AVG(profit_margin), MEDIAN(profit_margin), SUM(profit), MIN(profit_margin), MAX(profit_margin)",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Profit Margin per Sale to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.285320"},
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
                        95961.66,
                        97254.21,
                        103964.69,
                        99162.6,
                        108552.96,
                        97724.8,
                        100570.38,
                        105229.3,
                        104348.25,
                        95140.78,
                        100866.09,
                        97974.1
                ],
                "unit": "$"
        },
        "current": {
                "value": 97974.1,
                "unit": "$",
                "change": -2891.99,
                "change_percent": -2.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 100562.49,
                "min": 95140.78,
                "max": 108552.96,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 24365.88,
                        "percentage": 24.9
                },
                {
                        "category": "Category B",
                        "value": 13900.7,
                        "percentage": 14.2
                },
                {
                        "category": "Category C",
                        "value": 10595.87,
                        "percentage": 10.8
                },
                {
                        "category": "Category D",
                        "value": 9182.98,
                        "percentage": 9.4
                },
                {
                        "category": "Other",
                        "value": 39928.67,
                        "percentage": 40.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.995163",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Profit Margin per Sale"
        }
    },
}
