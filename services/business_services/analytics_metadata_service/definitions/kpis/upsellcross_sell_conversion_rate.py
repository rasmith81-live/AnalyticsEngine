"""
Upsell/Cross-sell Conversion Rate

The success rate of converting existing customers to purchase additional or related products and services.
"""

UPSELLCROSS_SELL_CONVERSION_RATE = {
    "code": "UPSELLCROSS_SELL_CONVERSION_RATE",
    "name": "Upsell/Cross-sell Conversion Rate",
    "description": "The success rate of converting existing customers to purchase additional or related products and services.",
    "formula": "(Number of Upsell/Cross-sell Sales / Total Number of Sales Opportunities) * 100",
    "calculation_formula": "(Number of Upsell/Cross-sell Sales / Total Number of Sales Opportunities) * 100",
    "category": "Customer Retention",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Upsell/Cross-sell Conversion Rate to be added.",
    "trend_analysis": """



    * An increasing upsell/cross-sell conversion rate may indicate successful sales strategies or improved customer engagement.
    * A decreasing rate could signal a need for better product knowledge among sales teams or a lack of customer interest in additional offerings.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that have higher conversion rates for upsell/cross-sell opportunities?
    * How does our upsell/cross-sell conversion rate compare with industry benchmarks or with historical data?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional training to sales teams on product knowledge and effective upselling techniques.
    * Implement targeted marketing campaigns to promote related products or services to existing customers.
    * Create bundled offerings or package deals to make upselling/cross-selling more attractive to customers.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the upsell/cross-sell conversion rate over time.
    * Pie charts comparing conversion rates for different product or service categories.
    
    
    
    """,
    "risk_warnings": """



    * A low upsell/cross-sell conversion rate may lead to missed revenue opportunities and underutilization of the existing customer base.
    * Pushing too aggressively for upselling or cross-selling may result in customer dissatisfaction and potential churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and identify upsell/cross-sell opportunities.
    * Analytics tools to analyze customer behavior and preferences for targeted upselling/cross-selling.
    
    
    
    """,
    "integration_points": """



    * Integrate upsell/cross-sell data with customer support systems to provide personalized recommendations during customer interactions.
    * Link with inventory management systems to ensure availability of additional products or services for upsell/cross-sell opportunities.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in upsell/cross-sell conversion rate can lead to higher revenue and improved customer lifetime value.
    * However, too much focus on upselling/cross-selling may impact the overall customer experience and satisfaction.
    
    
    
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Opportunity", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.767891"},
    "required_objects": [],
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
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
                        52.93,
                        57.37,
                        52.45,
                        46.42,
                        54.28,
                        50.88,
                        44.46,
                        54.98,
                        43.8,
                        57.73,
                        44.87,
                        45.37
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.37,
                "unit": "%",
                "change": 0.5,
                "change_percent": 1.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 50.46,
                "min": 43.8,
                "max": 57.73,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 8.81,
                        "percentage": 19.4
                },
                {
                        "category": "Channel Sales",
                        "value": 10.07,
                        "percentage": 22.2
                },
                {
                        "category": "Online Sales",
                        "value": 8.53,
                        "percentage": 18.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.66,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 14.3,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.914647",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upsell/Cross-sell Conversion Rate"
        }
    },
}
