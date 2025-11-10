"""
Margin per Sale KPI

The profit margin for each sale, calculated as the selling price minus the cost of goods sold.
"""

from analytics_models import KPI

MARGIN_PER_SALE = KPI(
    name="Margin per Sale",
    code="MARGIN_PER_SALE",
    category="Sales Operations",
    
    # Core Definition
    description="The profit margin for each sale, calculated as the selling price minus the cost of goods sold.",
    kpi_definition="The profit margin for each sale, calculated as the selling price minus the cost of goods sold.",
    expected_business_insights="Indicates the profitability of products and services sold.",
    measurement_approach="Compares the profit made on each sale to the revenue generated.",
    
    # Formula
    formula="(Revenue - Cost of Goods Sold) / Revenue",
    calculation_formula="(Revenue - Cost of Goods Sold) / Revenue",
    
    # Analysis
    trend_analysis="""
    * Increasing margin per sale may indicate successful pricing strategies or cost-saving measures.
    * Decreasing margin could signal increased competition, rising production costs, or ineffective pricing strategies.
    """,
    diagnostic_questions="""
    * Are there specific products with consistently low margins that need reevaluation?
    * How does our margin per sale compare with industry benchmarks or changes in production costs?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and adjust pricing strategies based on market conditions and cost fluctuations.
    * Identify and address inefficiencies in the production process to reduce cost of goods sold.
    * Explore opportunities for upselling or cross-selling to increase the average selling price.
    """,
    visualization_suggestions="""
    * Line charts to track the trend of margin per sale over time.
    * Pareto charts to identify which products contribute the most to overall margin.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low margins may lead to reduced profitability and financial instability.
    * Overly high margins could result in loss of competitiveness and customer attrition.
    """,
    tracking_tools="""
    * Enterprise resource planning (ERP) systems to track production costs and pricing data.
    * Business intelligence tools for in-depth analysis of sales and cost data.
    """,
    integration_points="""
    * Integrate margin per sale data with pricing and product development processes to optimize profitability.
    * Link with financial systems to understand the impact of margin changes on overall revenue and profit.
    """,
    change_impact_analysis="""
    * Improving margin per sale can lead to increased profitability but may require strategic shifts in pricing and cost management.
    * Reducing margins to gain market share may impact short-term profitability but could lead to long-term growth and customer loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Lost Sale", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
