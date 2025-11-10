"""
Up-Sell/Cross-Sell Rate KPI

The percentage increase in up-sell or cross-sell successes after sales training.
"""

from analytics_models import KPI

UP_SELLCROSS_SELL_RATE = KPI(
    name="Up-Sell/Cross-Sell Rate",
    code="UP_SELLCROSS_SELL_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage increase in up-sell or cross-sell successes after sales training.",
    kpi_definition="The percentage increase in up-sell or cross-sell successes after sales training.",
    expected_business_insights="Provides insights into sales team performance in generating additional revenue through strategic product recommendations.",
    measurement_approach="Measures the percentage of sales transactions that include an up-sell or cross-sell item relative to the total number of transactions.",
    
    # Formula
    formula="(Number of Transactions with Up-Sell or Cross-Sell / Total Number of Transactions) * 100",
    calculation_formula="(Number of Transactions with Up-Sell or Cross-Sell / Total Number of Transactions) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing up-sell/cross-sell rate may indicate that the sales team is effectively implementing the training and coaching strategies.
    * A decreasing rate could signal a need for additional training or adjustments to the sales process.
    """,
    diagnostic_questions="""
    * Are there specific products or services that have a higher success rate in up-selling or cross-selling?
    * How does our up-sell/cross-sell rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide targeted training on effective up-selling and cross-selling techniques.
    * Implement a structured follow-up process to ensure that opportunities for up-selling or cross-selling are not missed.
    * Utilize customer relationship management (CRM) tools to track and analyze up-sell/cross-sell opportunities.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of up-sell/cross-sell rates over time.
    * Pie charts to compare the success rates of different up-sell/cross-sell strategies or products.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low up-sell/cross-sell rate may result in missed revenue opportunities and underperformance.
    * An excessively high rate could indicate aggressive or pushy sales tactics that may harm customer relationships.
    """,
    tracking_tools="""
    * CRM systems with built-in up-sell/cross-sell tracking and reporting capabilities.
    * Sales performance management software to monitor and analyze the effectiveness of training and coaching programs.
    """,
    integration_points="""
    * Integrate up-sell/cross-sell data with customer feedback and satisfaction metrics to understand the impact on overall customer experience.
    * Link up-sell/cross-sell performance with inventory and supply chain systems to ensure availability of recommended products.
    """,
    change_impact_analysis="""
    * An increase in up-sell/cross-sell rate can lead to higher revenue and customer lifetime value.
    * However, aggressive up-selling or cross-selling may negatively impact customer trust and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
