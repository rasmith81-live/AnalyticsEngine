"""
New Product Sales Ratio KPI

The percentage of total sales that come from new products, indicating the success of product launches.
"""

from analytics_models import KPI

NEW_PRODUCT_SALES_RATIO = KPI(
    name="New Product Sales Ratio",
    code="NEW_PRODUCT_SALES_RATIO",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of total sales that come from new products, indicating the success of product launches.",
    kpi_definition="The percentage of total sales that come from new products, indicating the success of product launches.",
    expected_business_insights="Evaluates the success and market acceptance of new product launches.",
    measurement_approach="Compares the sales of new products to the total sales over a specific period.",
    
    # Formula
    formula="(New Product Sales / Total Sales) * 100",
    calculation_formula="(New Product Sales / Total Sales) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing new product sales ratio may indicate successful product launches and a growing customer interest in new offerings.
    * A decreasing ratio could signal challenges in marketing or positioning new products, or a lack of innovation in the product development pipeline.
    """,
    diagnostic_questions="""
    * Are there specific new products that consistently contribute to a high sales ratio, and if so, what factors contribute to their success?
    * How does the new product sales ratio compare to historical data and industry benchmarks, and what insights can be gained from any deviations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in market research and customer feedback to better understand the demand for new products and tailor marketing strategies accordingly.
    * Provide sales teams with targeted training and resources to effectively promote and sell new products to customers.
    * Regularly review and refine the new product development process to ensure a steady stream of successful product launches.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of new product sales ratio over time.
    * Pie charts comparing the contribution of new products to total sales in different time periods.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low new product sales ratio may indicate a lack of innovation or relevance in the product portfolio, leading to potential market stagnation.
    * Over-reliance on new product sales without a strong foundation of core product sales may lead to volatility in revenue and customer retention.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer preferences and feedback related to new products.
    * Product lifecycle management (PLM) tools to streamline the development and launch process of new products.
    """,
    integration_points="""
    * Integrate new product sales data with product development and marketing systems to align efforts and resources for successful launches.
    * Link new product sales ratio with customer satisfaction metrics to understand the impact of new products on overall customer experience.
    """,
    change_impact_analysis="""
    * An increase in new product sales ratio can lead to a more diverse product portfolio and potentially higher customer engagement and loyalty.
    * Conversely, a decrease in the ratio may impact the organization\'s ability to stay competitive and relevant in the market, affecting long-term growth and profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
