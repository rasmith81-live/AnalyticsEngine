"""
Sales Opportunity Score

A quantified assessment of the potential value and likelihood to win a sales opportunity.
"""

SALES_OPPORTUNITY_SCORE = {
    "code": "SALES_OPPORTUNITY_SCORE",
    "name": "Sales Opportunity Score",
    "description": "A quantified assessment of the potential value and likelihood to win a sales opportunity.",
    "formula": "Scoring System Based on Opportunity Value and Likelihood to Close",
    "calculation_formula": "Scoring System Based on Opportunity Value and Likelihood to Close",
    "category": "Inside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Opportunity Score to be added.",
    "trend_analysis": """



    * Increasing sales opportunity scores may indicate a more effective sales process or a growing market demand.
    * Decreasing scores could signal increased competition, changing customer preferences, or ineffective sales strategies.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to the calculation of the sales opportunity score?
    * How do our sales opportunity scores compare to industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional training and resources to sales teams to improve their ability to identify and pursue high-value opportunities.
    * Regularly review and update the criteria used to assess the potential value and likelihood to win sales opportunities.
    * Implement a lead scoring system to prioritize high-value opportunities and allocate resources effectively.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of sales opportunity scores over time.
    * Pie charts to visualize the distribution of sales opportunity scores across different products or customer segments.
    
    
    
    """,
    "risk_warnings": """



    * Over-reliance on sales opportunity scores may lead to neglecting other important factors in the sales process, such as customer relationships or market dynamics.
    * Inaccurate or biased scoring criteria can result in missed opportunities or wasted resources.
    
    
    
    """,
    "tracking_tools": """



    * Customer Relationship Management (CRM) software with advanced opportunity tracking and scoring capabilities.
    * Data analytics tools to identify patterns and correlations between sales opportunity scores and other performance metrics.
    
    
    
    """,
    "integration_points": """



    * Integrate sales opportunity scores with sales forecasting to align resource allocation with expected revenue.
    * Link sales opportunity scores with customer feedback and satisfaction metrics to assess the accuracy of the scoring criteria.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving sales opportunity scores can lead to increased revenue and market share, but may also require additional investment in sales and marketing efforts.
    * Lowering scores may indicate a need for strategic adjustments in product offerings, pricing, or target markets.
    
    
    
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Deal", "Expansion Opportunity", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.446851"},
    "required_objects": [],
    "modules": ["INSIDE_SALES", "SALES_PERFORMANCE"],
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
                        86.0,
                        86.2,
                        85.6,
                        81.9,
                        82.4,
                        82.8,
                        79.9,
                        82.3,
                        81.7,
                        89.9,
                        84.7,
                        83.4
                ],
                "unit": "score"
        },
        "current": {
                "value": 83.4,
                "unit": "score",
                "change": -1.3,
                "change_percent": -1.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 83.9,
                "min": 79.9,
                "max": 89.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 22.85,
                        "percentage": 27.4
                },
                {
                        "category": "Channel Sales",
                        "value": 16.8,
                        "percentage": 20.1
                },
                {
                        "category": "Online Sales",
                        "value": 11.71,
                        "percentage": 14.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.16,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 24.88,
                        "percentage": 29.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.054197",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Sales Opportunity Score"
        }
    },
}
