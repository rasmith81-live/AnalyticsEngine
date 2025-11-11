"""
Total Revenue

The total amount of income generated from the sale of goods or services related to the company's primary operations.
"""

TOTAL_REVENUE = {
    "code": "TOTAL_REVENUE",
    "name": "Total Revenue",
    "description": "The total amount of income generated from the sale of goods or services related to the company's primary operations.",
    "formula": "Sum of All Revenue Streams",
    "calculation_formula": "Sum of All Revenue Streams",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Total Revenue to be added.",
    "trend_analysis": """



    * Increasing total revenue may indicate successful product launches or market expansion.
    * Decreasing revenue could signal market saturation or declining demand for existing products/services.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services driving the majority of the revenue, and are there opportunities to diversify offerings?
    * How does our revenue growth compare with industry benchmarks or economic trends?
    
    
    
    """,
    "actionable_tips": """



    * Explore new market segments or geographical areas to expand customer base.
    * Invest in marketing and sales strategies to promote existing products/services to new or existing customers.
    * Regularly review pricing strategies to ensure they align with market demand and competition.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing revenue trends over time.
    * Pie charts to visualize revenue distribution by product or service category.
    
    
    
    """,
    "risk_warnings": """



    * Reliance on a small number of high-revenue products/services can expose the business to significant risk if demand shifts.
    * Declining revenue may lead to financial instability and impact the ability to invest in future growth.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) systems to track and manage customer interactions and sales opportunities.
    * Business intelligence and analytics tools to identify revenue trends and customer behavior patterns.
    
    
    
    """,
    "integration_points": """



    * Integrate revenue data with marketing and sales systems to understand the impact of campaigns and promotions on revenue generation.
    * Link revenue tracking with financial systems to ensure accurate reporting and forecasting.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing revenue may require additional resources and investment in sales and marketing efforts.
    * Decreasing revenue can impact the ability to invest in research and development or expansion opportunities.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lost Sale", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.725067"},
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
                        89928.32,
                        93507.35,
                        91063.02,
                        94436.88,
                        92214.11,
                        100734.14,
                        87105.29,
                        91274.88,
                        99321.18,
                        86821.17,
                        91435.21,
                        92688.83
                ],
                "unit": "$"
        },
        "current": {
                "value": 92688.83,
                "unit": "$",
                "change": 1253.62,
                "change_percent": 1.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 92544.2,
                "min": 86821.17,
                "max": 100734.14,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 21907.82,
                        "percentage": 23.6
                },
                {
                        "category": "Channel Sales",
                        "value": 12439.57,
                        "percentage": 13.4
                },
                {
                        "category": "Online Sales",
                        "value": 8889.83,
                        "percentage": 9.6
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7446.25,
                        "percentage": 8.0
                },
                {
                        "category": "Other",
                        "value": 42005.36,
                        "percentage": 45.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.802122",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Total Revenue"
        }
    },
}
