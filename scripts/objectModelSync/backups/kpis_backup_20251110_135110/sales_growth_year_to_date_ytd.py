"""
Sales Growth Year-to-Date (YTD)

The increase in sales revenue from the beginning of the current fiscal year up to the present date, compared against the same period in the prior year.
"""

SALES_GROWTH_YEAR_TO_DATE_YTD = {
    "code": "SALES_GROWTH_YEAR_TO_DATE_YTD",
    "name": "Sales Growth Year-to-Date (YTD)",
    "description": "The increase in sales revenue from the beginning of the current fiscal year up to the present date, compared against the same period in the prior year.",
    "formula": "(Current YTD Sales - Previous YTD Sales) / Previous YTD Sales",
    "calculation_formula": "(Current YTD Sales - Previous YTD Sales) / Previous YTD Sales",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Growth Year-to-Date (YTD) to be added.",
    "trend_analysis": """


    * Sales growth tends to follow seasonal patterns, with higher performance during certain times of the year.
    * Changes in market conditions, such as new competitors or economic downturns, can significantly impact sales growth.
    
    
    """,
    "diagnostic_questions": """


    * What factors have historically driven sales growth during certain periods?
    * How does our sales growth compare to industry averages and benchmarks?
    
    
    """,
    "actionable_tips": """


    * Invest in targeted marketing and promotional campaigns during peak sales periods.
    * Regularly analyze and adjust pricing strategies to maximize revenue.
    * Explore new sales channels or geographic markets to expand customer reach.
    
    
    """,
    "visualization_suggestions": """


    * Line charts showing year-over-year sales growth by month or quarter.
    * Comparative bar graphs illustrating sales growth performance against industry averages.
    
    
    """,
    "risk_warnings": """


    * Over-reliance on a small number of key clients or products can make sales growth vulnerable to sudden changes.
    * Rapid sales growth may strain operational capacity and lead to service or quality issues.
    
    
    """,
    "tracking_tools": """


    * Customer relationship management (CRM) software to track and manage customer interactions and sales opportunities.
    * Business intelligence and analytics tools to identify sales trends and opportunities for growth.
    
    
    """,
    "integration_points": """


    * Integrate sales growth data with financial systems to understand the impact on revenue and profitability.
    * Link sales growth metrics with inventory and supply chain systems to ensure adequate stock levels to meet demand.
    
    
    """,
    "change_impact_analysis": """


    * Increasing sales growth may require additional investment in sales and marketing resources.
    * Significant changes in sales growth can impact cash flow and working capital requirements.
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.434337"},
    "required_objects": [],
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
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
                        786.18,
                        848.14,
                        781.79,
                        735.85,
                        833.21,
                        782.3,
                        806.7,
                        775.65,
                        839.21,
                        757.99,
                        858.47,
                        825.55
                ],
                "unit": "units"
        },
        "current": {
                "value": 825.55,
                "unit": "units",
                "change": -32.92,
                "change_percent": -3.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 802.59,
                "min": 735.85,
                "max": 858.47,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 216.23,
                        "percentage": 26.2
                },
                {
                        "category": "Category B",
                        "value": 212.62,
                        "percentage": 25.8
                },
                {
                        "category": "Category C",
                        "value": 64.02,
                        "percentage": 7.8
                },
                {
                        "category": "Category D",
                        "value": 72.61,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 260.07,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.413916",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Sales Growth Year-to-Date (YTD)"
        }
    },
}
