"""
Demo-to-Close Ratio KPI

The percentage of product demos given to prospects that result in closed sales.
"""

from analytics_models import KPI

DEMO_TO_CLOSE_RATIO = KPI(
    name="Demo-to-Close Ratio",
    code="DEMO_TO_CLOSE_RATIO",
    category="Inside Sales",
    
    # Core Definition
    description="The percentage of product demos given to prospects that result in closed sales.",
    kpi_definition="The percentage of product demos given to prospects that result in closed sales.",
    expected_business_insights="Assesses the effectiveness of sales presentations and product demonstrations in the sales process.",
    measurement_approach="The percentage of demonstrations or presentations that lead to closed deals.",
    
    # Formula
    formula="(Number of Closed Deals Post-Demo / Total Number of Demos Given) * 100",
    calculation_formula="(Number of Closed Deals Post-Demo / Total Number of Demos Given) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing demo-to-close ratio may indicate improved sales techniques or a better understanding of customer needs.
    * A decreasing ratio could signal issues with product quality, pricing, or the effectiveness of the sales team.
    """,
    diagnostic_questions="""
    * Are there specific products or sales reps that consistently have higher or lower demo-to-close ratios?
    * How does our demo-to-close ratio compare with industry benchmarks or with different customer segments?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and resources to improve the effectiveness of product demos.
    * Regularly review and update sales scripts and materials to ensure they align with customer needs and objections.
    * Implement a lead scoring system to prioritize prospects with a higher likelihood of closing.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of demo-to-close ratios over time.
    * Pie charts comparing demo-to-close ratios for different product categories or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low demo-to-close ratio can lead to wasted resources and decreased sales effectiveness.
    * High fluctuations in the ratio may indicate inconsistent sales processes or customer targeting.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze the effectiveness of product demos and sales follow-ups.
    * Sales enablement platforms to provide sales reps with the necessary tools and content to improve their demo-to-close ratio.
    """,
    integration_points="""
    * Integrate demo-to-close ratio tracking with marketing automation systems to align lead generation efforts with sales effectiveness.
    * Link with customer feedback systems to understand how product demos and sales interactions are perceived by prospects.
    """,
    change_impact_analysis="""
    * Improving the demo-to-close ratio can lead to increased revenue and customer satisfaction, but may require additional resources for sales training and support.
    * Conversely, a declining ratio can negatively impact sales performance and overall business growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Demo", "Lead", "Lead Qualification", "Opportunity", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
