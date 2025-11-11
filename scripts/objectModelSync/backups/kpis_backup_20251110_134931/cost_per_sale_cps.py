"""
Cost Per Sale (CPS)

The average cost incurred to make a single sale, including marketing, sales personnel, and other related expenses.
"""

COST_PER_SALE_CPS = {
    "code": "COST_PER_SALE_CPS",
    "name": "Cost Per Sale (CPS)",
    "description": "The average cost incurred to make a single sale, including marketing, sales personnel, and other related expenses.",
    "formula": "Total Sales Costs / Number of Sales Made",
    "calculation_formula": "Total Sales Costs / Number of Sales Made",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Cost Per Sale (CPS) to be added.",
    "trend_analysis": """

    * Increasing cost per sale may indicate rising marketing or sales expenses without a proportional increase in revenue.
    * Decreasing cost per sale could signal improved efficiency in the sales process or reduced marketing costs.
    
    """,
    "diagnostic_questions": """

    * Are there specific sales channels or campaigns that have significantly higher or lower cost per sale?
    * How does our cost per sale compare with industry averages or benchmarks for similar products or services?
    
    """,
    "actionable_tips": """

    * Implement lead scoring and qualification processes to focus sales efforts on high-potential leads.
    * Regularly review and optimize marketing and advertising spend to ensure cost-effectiveness.
    * Provide sales teams with training and tools to improve their efficiency and effectiveness.
    
    """,
    "visualization_suggestions": """

    * Line charts showing the trend of cost per sale over time.
    * Pareto charts to identify the most significant contributors to overall cost per sale.
    
    """,
    "risk_warnings": """

    * High cost per sale can lead to reduced profitability and competitiveness in the market.
    * Significant fluctuations in cost per sale may indicate instability or inefficiency in sales and marketing operations.
    
    """,
    "tracking_tools": """

    * Customer Relationship Management (CRM) systems to track and analyze sales and marketing expenses.
    * Marketing automation platforms to optimize campaign performance and cost-effectiveness.
    
    """,
    "integration_points": """

    * Integrate cost per sale analysis with financial reporting to understand its impact on overall profitability.
    * Link cost per sale data with customer relationship management systems to assess the relationship between cost and customer acquisition.
    
    """,
    "change_impact_analysis": """

    * Reducing cost per sale may lead to increased sales volume but could also impact the quality of leads and customer relationships.
    * Increasing cost per sale to improve lead quality or customer experience may result in lower immediate profitability.
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lost Sale", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.175832"},
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
                        119,
                        149,
                        122,
                        121,
                        149,
                        169,
                        167,
                        153,
                        122,
                        144,
                        125,
                        155
                ],
                "unit": "count"
        },
        "current": {
                "value": 155,
                "unit": "count",
                "change": 30,
                "change_percent": 24.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 141.25,
                "min": 119,
                "max": 169,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 32.65,
                        "percentage": 21.1
                },
                {
                        "category": "Category B",
                        "value": 41.38,
                        "percentage": 26.7
                },
                {
                        "category": "Category C",
                        "value": 14.4,
                        "percentage": 9.3
                },
                {
                        "category": "Category D",
                        "value": 7.7,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 58.87,
                        "percentage": 38.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.175832",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Cost Per Sale (CPS)"
        }
    },
}
