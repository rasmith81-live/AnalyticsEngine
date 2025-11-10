"""
Product Penetration Rate KPI

The rate at which a specific product is sold to the target market or within customer accounts.
"""

from analytics_models import KPI

PRODUCT_PENETRATION_RATE = KPI(
    name="Product Penetration Rate",
    code="PRODUCT_PENETRATION_RATE",
    category="Outside Sales",
    
    # Core Definition
    description="The rate at which a specific product is sold to the target market or within customer accounts.",
    kpi_definition="The rate at which a specific product is sold to the target market or within customer accounts.",
    expected_business_insights="Indicates product popularity and adoption among the customer base, guiding marketing and product development efforts.",
    measurement_approach="Measures the percentage of customers who have purchased a specific product out of the total customer base.",
    
    # Formula
    formula="(Number of Customers Who Purchased the Product / Total Number of Customers) * 100",
    calculation_formula="(Number of Customers Who Purchased the Product / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing product penetration rate may indicate successful marketing efforts or a growing demand for the specific product.
    * A decreasing rate could signal market saturation or a shift in customer preferences towards other products.
    """,
    diagnostic_questions="""
    * Are there specific customer segments that are more receptive to the product?
    * What factors contribute to fluctuations in the product penetration rate, such as seasonality or competitive actions?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Conduct targeted marketing campaigns to promote the product to potential customers.
    * Offer incentives or discounts to encourage existing customers to purchase the product.
    * Regularly assess and adjust pricing strategies to maintain competitiveness in the market.
    """,
    visualization_suggestions="""
    * Line charts showing the product penetration rate over time.
    * Pie charts comparing the product penetration rate across different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining product penetration rate may lead to excess inventory and potential financial losses.
    * Over-reliance on a single product for sales can create vulnerability to market changes or disruptions.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and preferences related to the product.
    * Market research tools to gather insights on customer perceptions and preferences for the product.
    """,
    integration_points="""
    * Integrate product penetration rate data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link with inventory management systems to ensure adequate stock levels for the product based on demand.
    """,
    change_impact_analysis="""
    * An increase in product penetration rate can positively impact overall sales revenue and market share.
    * However, a decrease in penetration rate may require strategic adjustments to prevent negative effects on the business\'s bottom line.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Channel Market", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Knowledge Base", "Market Segment", "Product", "Product Adoption", "Product Usage", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
