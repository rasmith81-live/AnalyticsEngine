"""
Upsell and Cross-Sell Rate

The percentage of customers who purchase additional products or services from the company. This KPI measures the effectiveness of the Customer Success Team in identifying opportunities for upselling or cross-selling.
"""

UPSELL_AND_CROSS_SELL_RATE = {
    "code": "UPSELL_AND_CROSS_SELL_RATE",
    "name": "Upsell and Cross-Sell Rate",
    "description": "The percentage of customers who purchase additional products or services from the company. This KPI measures the effectiveness of the Customer Success Team in identifying opportunities for upselling or cross-selling.",
    "formula": "(Number of Successful Upsell/Cross-Sell Transactions / Total Number of Sales Opportunities) * 100",
    "calculation_formula": "(Number of Successful Upsell/Cross-Sell Transactions / Total Number of Sales Opportunities) * 100",
    "category": "Customer Success",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Upsell and Cross-Sell Rate to be added.",
    "trend_analysis": """



    * An increasing upsell/cross-sell rate may indicate improved customer engagement and satisfaction, leading to more opportunities for additional sales.
    * A decreasing rate could signal a need for better product knowledge or a shift in customer preferences, requiring adjustments in the sales approach.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments or industries that are more receptive to upsell/cross-sell offers?
    * How effective are our current upsell/cross-sell strategies, and what feedback have we received from customers?
    
    
    
    """,
    "actionable_tips": """



    * Train the sales team to identify customer needs and pain points to better position upsell/cross-sell opportunities.
    * Utilize customer data and analytics to personalize and target upsell/cross-sell offers for maximum relevance.
    * Implement a proactive communication strategy to educate customers about additional products or services that complement their existing purchases.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the upsell/cross-sell rate over time to identify seasonal or trend-based patterns.
    * Pie charts to visualize the distribution of additional purchases by product or service category.
    
    
    
    """,
    "risk_warnings": """



    * A low upsell/cross-sell rate may indicate missed revenue opportunities and underutilization of the customer base.
    * Pushing irrelevant or excessive upsell/cross-sell offers can lead to customer annoyance and potential churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify upsell/cross-sell opportunities.
    * Marketing automation platforms to personalize and automate upsell/cross-sell campaigns based on customer behavior.
    
    
    
    """,
    "integration_points": """



    * Integrate upsell/cross-sell data with sales performance metrics to evaluate the impact on overall revenue and customer lifetime value.
    * Link customer feedback and satisfaction scores with upsell/cross-sell efforts to understand the relationship between customer experience and additional purchases.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in the upsell/cross-sell rate can positively impact revenue and customer lifetime value, but it may also require adjustments in sales strategies and resources.
    * Conversely, a decrease in the rate may signal a need for reevaluation of customer engagement tactics and product relevance.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_SUCCESS", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.763948"},
    "required_objects": [],
    "modules": ["CUSTOMER_SUCCESS", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
    "module_code": "CUSTOMER_SUCCESS",
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
                        67.26,
                        63.73,
                        57.36,
                        49.77,
                        56.53,
                        55.42,
                        52.86,
                        54.08,
                        63.64,
                        53.58,
                        56.57,
                        51.3
                ],
                "unit": "%"
        },
        "current": {
                "value": 51.3,
                "unit": "%",
                "change": -5.27,
                "change_percent": -9.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 56.84,
                "min": 49.77,
                "max": 67.26,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 8.24,
                        "percentage": 16.1
                },
                {
                        "category": "Channel Sales",
                        "value": 10.95,
                        "percentage": 21.3
                },
                {
                        "category": "Online Sales",
                        "value": 7.35,
                        "percentage": 14.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 6.02,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 18.74,
                        "percentage": 36.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.906289",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upsell and Cross-Sell Rate"
        }
    },
}
