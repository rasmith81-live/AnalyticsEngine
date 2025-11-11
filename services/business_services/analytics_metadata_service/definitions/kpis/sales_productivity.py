"""
Sales Productivity

The effectiveness of the sales team in generating revenue relative to their cost.
"""

SALES_PRODUCTIVITY = {
    "code": "SALES_PRODUCTIVITY",
    "name": "Sales Productivity",
    "description": "The effectiveness of the sales team in generating revenue relative to their cost.",
    "formula": "Total Revenue / Number of Sales Reps or Efforts",
    "calculation_formula": "Total Revenue / Number of Sales Reps or Efforts",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Productivity to be added.",
    "trend_analysis": """



    * Increasing sales productivity may indicate improved sales processes, better lead generation, or more effective sales training.
    * Decreasing productivity could signal issues with sales team motivation, market saturation, or ineffective sales strategies.
    
    
    
    """,
    "diagnostic_questions": """



    * What are the main factors contributing to the current level of sales productivity?
    * Are there specific sales territories, products, or customer segments that are underperforming in terms of productivity?
    
    
    
    """,
    "actionable_tips": """



    * Invest in sales training and coaching to improve the effectiveness of the sales team.
    * Implement or optimize sales automation tools to streamline processes and free up more time for actual selling activities.
    * Regularly review and update the sales compensation structure to ensure it incentivizes high productivity.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing sales productivity over time, segmented by individual sales reps or sales teams.
    * Pareto charts to identify the most and least productive sales activities or products.
    
    
    
    """,
    "risk_warnings": """



    * Low sales productivity can lead to missed revenue targets and decreased profitability.
    * High sales productivity without proper quality control can result in increased customer complaints and returns.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software to track sales activities and customer interactions.
    * Sales performance management tools to monitor and analyze individual and team productivity metrics.
    
    
    
    """,
    "integration_points": """



    * Integrate sales productivity data with marketing analytics to understand the impact of marketing efforts on sales outcomes.
    * Link sales productivity with customer satisfaction metrics to assess the overall impact of sales efforts on customer experience.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing sales productivity may lead to higher revenue and improved profitability, but it could also strain resources if not managed effectively.
    * Decreasing sales productivity can result in missed sales opportunities and decreased market share, impacting long-term business growth.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.472010"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
    "module_code": "INSIDE_SALES",
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
                        292,
                        281,
                        292,
                        301,
                        303,
                        288,
                        316,
                        306,
                        285,
                        287,
                        296,
                        299
                ],
                "unit": "count"
        },
        "current": {
                "value": 299,
                "unit": "count",
                "change": 3,
                "change_percent": 1.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 295.5,
                "min": 281,
                "max": 316,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Product Line A",
                        "value": 66.06,
                        "percentage": 22.1
                },
                {
                        "category": "Product Line B",
                        "value": 68.04,
                        "percentage": 22.8
                },
                {
                        "category": "Product Line C",
                        "value": 51.81,
                        "percentage": 17.3
                },
                {
                        "category": "Services",
                        "value": 27.5,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 85.59,
                        "percentage": 28.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.132849",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Sales Productivity"
        }
    },
}
