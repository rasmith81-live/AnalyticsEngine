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
                        68.61,
                        62.11,
                        65.4,
                        62.46,
                        63.46,
                        73.89,
                        76.7,
                        76.83,
                        61.64,
                        69.8,
                        70.63,
                        58.17
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.17,
                "unit": "%",
                "change": -12.46,
                "change_percent": -17.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 67.47,
                "min": 58.17,
                "max": 76.83,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.29,
                        "percentage": 28.0
                },
                {
                        "category": "Category B",
                        "value": 7.04,
                        "percentage": 12.1
                },
                {
                        "category": "Category C",
                        "value": 8.06,
                        "percentage": 13.9
                },
                {
                        "category": "Category D",
                        "value": 7.04,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 19.74,
                        "percentage": 33.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.973662",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Product Penetration Rate"
        }
    },
}
