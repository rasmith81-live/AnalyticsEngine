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
                        51.07,
                        60.55,
                        63.3,
                        58.17,
                        50.48,
                        53.37,
                        65.94,
                        63.31,
                        56.66,
                        47.94,
                        60.14,
                        51.2
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.2,
                "unit": "%",
                "change": -8.94,
                "change_percent": -14.9,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.84,
                "min": 47.94,
                "max": 65.94,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.2,
                        "percentage": 18.0
                },
                {
                        "category": "Segment B",
                        "value": 6.4,
                        "percentage": 12.5
                },
                {
                        "category": "Segment C",
                        "value": 11.45,
                        "percentage": 22.4
                },
                {
                        "category": "Segment D",
                        "value": 2.89,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 21.26,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.670510",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Profit Margin per Sale"
        }
    },
}
