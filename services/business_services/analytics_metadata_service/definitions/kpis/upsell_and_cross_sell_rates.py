"""
Upsell and Cross-Sell Rates

The success rates of efforts to sell more expensive items or additional products to existing customers, indicating the effectiveness of sales strategies.
"""

UPSELL_AND_CROSS_SELL_RATES = {
    "code": "UPSELL_AND_CROSS_SELL_RATES",
    "name": "Upsell and Cross-Sell Rates",
    "description": "The success rates of efforts to sell more expensive items or additional products to existing customers, indicating the effectiveness of sales strategies.",
    "formula": "(Number of Upsell or Cross-sell Sales / Total Number of Transactions) * 100",
    "calculation_formula": "(Number of Upsell or Cross-sell Sales / Total Number of Transactions) * 100",
    "category": "Sales Performance",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Upsell and Cross-Sell Rates to be added.",
    "trend_analysis": """



    * An increasing upsell and cross-sell rate may indicate the effectiveness of sales strategies in identifying customer needs and preferences.
    * A decreasing rate could signal a need for reevaluation of sales tactics or a shift in customer behavior.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific products or services that have higher success rates in upselling or cross-selling?
    * How does our upsell and cross-sell rate compare with industry benchmarks or competitors?
    
    
    
    """,
    "actionable_tips": """



    * Train sales teams to better understand customer needs and offer relevant upsell or cross-sell options.
    * Utilize customer data and insights to personalize upsell and cross-sell recommendations.
    * Implement targeted marketing campaigns to promote complementary products or upgrades to existing customers.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing upsell and cross-sell rates over time to identify trends and seasonality.
    * Pie charts to visualize the distribution of successful upsell and cross-sell efforts by product or service category.
    
    
    
    """,
    "risk_warnings": """



    * A low upsell and cross-sell rate may lead to missed revenue opportunities and underutilization of existing customer base.
    * Overly aggressive upselling or cross-selling tactics can result in customer dissatisfaction and potential churn.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and preferences for targeted upsell and cross-sell opportunities.
    * Analytics tools to analyze customer behavior and identify potential upsell or cross-sell opportunities.
    
    
    
    """,
    "integration_points": """



    * Integrate upsell and cross-sell data with customer support systems to provide a seamless experience for customers.
    * Link with inventory management systems to ensure availability of upsell or cross-sell items.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in upsell and cross-sell rates can positively impact revenue and customer lifetime value.
    * However, a focus solely on upselling and cross-selling may impact customer trust and loyalty if not done in a customer-centric manner.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Success Manager", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.765892"},
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
                        57.06,
                        63.02,
                        66.58,
                        68.32,
                        59.67,
                        70.58,
                        56.38,
                        73.01,
                        59.79,
                        61.45,
                        66.3,
                        74.52
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.52,
                "unit": "%",
                "change": 8.22,
                "change_percent": 12.4,
                "trend": "increasing"
        },
        "statistics": {
                "average": 64.72,
                "min": 56.38,
                "max": 74.52,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 15.28,
                        "percentage": 20.5
                },
                {
                        "category": "Channel Sales",
                        "value": 17.64,
                        "percentage": 23.7
                },
                {
                        "category": "Online Sales",
                        "value": 13.39,
                        "percentage": 18.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.47,
                        "percentage": 4.7
                },
                {
                        "category": "Other",
                        "value": 24.74,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.909432",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Upsell and Cross-Sell Rates"
        }
    },
}
