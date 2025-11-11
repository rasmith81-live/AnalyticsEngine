"""
Product Penetration Rate

The rate at which a specific product is sold to the target market or within customer accounts.
"""

PRODUCT_PENETRATION_RATE = {
    "code": "PRODUCT_PENETRATION_RATE",
    "name": "Product Penetration Rate",
    "description": "The rate at which a specific product is sold to the target market or within customer accounts.",
    "formula": "(Number of Customers Who Purchased the Product / Total Number of Customers) * 100",
    "calculation_formula": "(Number of Customers Who Purchased the Product / Total Number of Customers) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Product Penetration Rate to be added.",
    "trend_analysis": """



    * An increasing product penetration rate may indicate successful marketing efforts or a growing demand for the specific product.
    * A decreasing rate could signal market saturation or a shift in customer preferences towards other products.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific customer segments that are more receptive to the product?
    * What factors contribute to fluctuations in the product penetration rate, such as seasonality or competitive actions?
    
    
    
    """,
    "actionable_tips": """



    * Conduct targeted marketing campaigns to promote the product to potential customers.
    * Offer incentives or discounts to encourage existing customers to purchase the product.
    * Regularly assess and adjust pricing strategies to maintain competitiveness in the market.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the product penetration rate over time.
    * Pie charts comparing the product penetration rate across different customer segments.
    
    
    
    """,
    "risk_warnings": """



    * A declining product penetration rate may lead to excess inventory and potential financial losses.
    * Over-reliance on a single product for sales can create vulnerability to market changes or disruptions.
    
    
    
    """,
    "tracking_tools": """



    * Customer relationship management (CRM) software to track customer interactions and preferences related to the product.
    * Market research tools to gather insights on customer perceptions and preferences for the product.
    
    
    
    """,
    "integration_points": """



    * Integrate product penetration rate data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link with inventory management systems to ensure adequate stock levels for the product based on demand.
    
    
    
    """,
    "change_impact_analysis": """



    * An increase in product penetration rate can positively impact overall sales revenue and market share.
    * However, a decrease in penetration rate may require strategic adjustments to prevent negative effects on the business's bottom line.
    
    
    
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Knowledge Base", "Market Segment", "Product", "Product Adoption", "Product Usage", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:49:33.267580"},
    "required_objects": [],
    "modules": ["OUTSIDE_SALES", "SALES_STRATEGY"],
    "module_code": "OUTSIDE_SALES",
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
                        56.37,
                        43.48,
                        49.68,
                        52.35,
                        44.11,
                        56.02,
                        56.14,
                        49.66,
                        44.57,
                        60.7,
                        43.21,
                        56.7
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.7,
                "unit": "%",
                "change": 13.49,
                "change_percent": 31.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 51.08,
                "min": 43.21,
                "max": 60.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 12.26,
                        "percentage": 21.6
                },
                {
                        "category": "Existing Customers",
                        "value": 13.83,
                        "percentage": 24.4
                },
                {
                        "category": "VIP Customers",
                        "value": 10.45,
                        "percentage": 18.4
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.13,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 15.03,
                        "percentage": 26.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.636564",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Product Penetration Rate"
        }
    },
}
