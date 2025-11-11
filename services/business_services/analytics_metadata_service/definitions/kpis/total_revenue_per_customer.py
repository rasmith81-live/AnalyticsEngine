"""
Total Revenue per Customer

The total revenue received from an average customer, which is useful for understanding the value generated from customer relationships.
"""

TOTAL_REVENUE_PER_CUSTOMER = {
    "code": "TOTAL_REVENUE_PER_CUSTOMER",
    "name": "Total Revenue per Customer",
    "description": "The total revenue received from an average customer, which is useful for understanding the value generated from customer relationships.",
    "formula": "Total Revenue / Total Number of Customers",
    "calculation_formula": "Total Revenue / Total Number of Customers",
    "category": "Sales Strategy",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Total Revenue per Customer to be added.",
    "trend_analysis": """



    * Increasing total revenue per customer may indicate successful upselling or cross-selling strategies.
    * Decreasing revenue per customer could signal declining customer loyalty or satisfaction.
    
    
    
    """,
    "diagnostic_questions": """



    * What factors contribute to the increase or decrease in revenue per customer?
    * How does the revenue per customer compare to industry benchmarks or historical data?
    
    
    
    """,
    "actionable_tips": """



    * Implement personalized marketing and sales strategies to increase customer spend.
    * Focus on improving customer experience and satisfaction to retain and grow customer value.
    * Regularly review and adjust pricing strategies to maximize revenue per customer.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing revenue per customer over time.
    * Pareto charts to identify the most valuable customers contributing to total revenue.
    
    
    
    """,
    "risk_warnings": """



    * Overemphasis on short-term revenue gains may lead to customer churn and long-term revenue loss.
    * Failure to adapt to changing customer preferences and needs can result in declining revenue per customer.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track and analyze customer purchasing behavior.
    * Business intelligence tools to segment and analyze customer data for targeted sales strategies.
    
    
    
    """,
    "integration_points": """



    * Integrate revenue per customer data with customer feedback systems to understand the correlation between satisfaction and spending.
    * Link with marketing automation platforms to personalize offers and promotions based on customer purchasing patterns.
    
    
    
    """,
    "change_impact_analysis": """



    * Increasing revenue per customer may lead to higher profitability and improved customer lifetime value.
    * However, aggressive sales tactics to boost revenue per customer can negatively impact customer relationships and brand reputation.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.726703"},
    "required_objects": [],
    "modules": ["SALES_STRATEGY"],
    "module_code": "SALES_STRATEGY",
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
                        443,
                        432,
                        464,
                        462,
                        453,
                        438,
                        449,
                        470,
                        457,
                        443,
                        452,
                        441
                ],
                "unit": "count"
        },
        "current": {
                "value": 441,
                "unit": "count",
                "change": -11,
                "change_percent": -2.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 450.33,
                "min": 432,
                "max": 470,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 96.04,
                        "percentage": 21.8
                },
                {
                        "category": "Existing Customers",
                        "value": 66.87,
                        "percentage": 15.2
                },
                {
                        "category": "VIP Customers",
                        "value": 60.39,
                        "percentage": 13.7
                },
                {
                        "category": "At-Risk Customers",
                        "value": 54.58,
                        "percentage": 12.4
                },
                {
                        "category": "Other",
                        "value": 163.12,
                        "percentage": 37.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.807670",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Total Revenue per Customer"
        }
    },
}
