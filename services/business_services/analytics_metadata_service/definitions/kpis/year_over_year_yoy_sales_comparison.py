"""
Year-over-Year (YoY) Sales Comparison

A comparison of sales figures from one year to the same period in the previous year, indicating trends and growth patterns.
"""

YEAR_OVER_YEAR_YOY_SALES_COMPARISON = {
    "code": "YEAR_OVER_YEAR_YOY_SALES_COMPARISON",
    "name": "Year-over-Year (YoY) Sales Comparison",
    "description": "A comparison of sales figures from one year to the same period in the previous year, indicating trends and growth patterns.",
    "formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "calculation_formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Year-over-Year (YoY) Sales Comparison to be added.",
    "trend_analysis": """



    * Positive trends in YoY sales comparison may indicate successful marketing strategies or product innovations that are resonating with customers.
    * Negative trends could signal market saturation, increased competition, or economic downturns affecting consumer spending.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific regions or customer segments driving the YoY sales growth or decline?
    * How do external factors such as industry trends or regulatory changes impact YoY sales performance?
    
    
    
    """,
    "actionable_tips": """



    * Invest in market research to identify emerging opportunities and customer preferences.
    * Adjust pricing strategies or promotional activities based on seasonal variations or competitive pressures.
    * Enhance sales team training and performance management to capitalize on growth opportunities and address declining sales trends.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts to visualize the trajectory of YoY sales comparison over time.
    * Stacked bar graphs to compare sales performance by product categories or geographic regions.
    
    
    
    """,
    "risk_warnings": """



    * Declining YoY sales may lead to revenue shortfalls and impact overall business profitability.
    * Rapid YoY sales growth without proper capacity planning can strain operational resources and lead to customer dissatisfaction.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track customer interactions and identify sales opportunities.
    * Business Intelligence (BI) tools for in-depth analysis of sales data and performance metrics.
    
    
    
    """,
    "integration_points": """



    * Integrate YoY sales comparison with inventory management systems to ensure adequate stock levels to meet demand.
    * Link sales performance with financial systems to analyze the impact on revenue and profitability.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving YoY sales comparison can lead to increased market share and brand recognition.
    * Conversely, declining sales performance may necessitate cost-cutting measures or strategic repositioning to remain competitive.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.825459"},
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
                        50.27,
                        60.9,
                        53.62,
                        58.82,
                        49.22,
                        48.15,
                        57.71,
                        49.55,
                        46.98,
                        57.22,
                        50.23,
                        56.89
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.89,
                "unit": "%",
                "change": 6.66,
                "change_percent": 13.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.3,
                "min": 46.98,
                "max": 60.9,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 18.06,
                        "percentage": 31.7
                },
                {
                        "category": "Channel Sales",
                        "value": 6.01,
                        "percentage": 10.6
                },
                {
                        "category": "Online Sales",
                        "value": 9.8,
                        "percentage": 17.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.43,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 18.59,
                        "percentage": 32.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:14.012934",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Year-over-Year (YoY) Sales Comparison"
        }
    },
}
