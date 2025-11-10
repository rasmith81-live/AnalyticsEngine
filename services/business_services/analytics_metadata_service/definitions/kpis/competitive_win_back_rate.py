"""
Competitive Win-back Rate KPI

The rate at which lost customers from key accounts are regained from competitors.
"""

from analytics_models import KPI

COMPETITIVE_WIN_BACK_RATE = KPI(
    name="Competitive Win-back Rate",
    code="COMPETITIVE_WIN_BACK_RATE",
    category="Key Account Management",
    
    # Core Definition
    description="The rate at which lost customers from key accounts are regained from competitors.",
    kpi_definition="The rate at which lost customers from key accounts are regained from competitors.",
    expected_business_insights="Shines light on the effectiveness of win-back strategies and the value proposition against competitors.",
    measurement_approach="Measures the percentage of customers regained after having lost them to competitors.",
    
    # Formula
    formula="(Number of Customers Won Back / Total Number of Customers Lost to Competitors) * 100",
    calculation_formula="(Number of Customers Won Back / Total Number of Customers Lost to Competitors) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing competitive win-back rate may indicate successful strategies for regaining lost customers and outperforming competitors.
    * A decreasing rate could signal challenges in retaining or reacquiring lost customers, potentially due to stronger competitor offerings or poor customer experience.
    """,
    diagnostic_questions="""
    * What specific actions or initiatives have contributed to the increase or decrease in the competitive win-back rate?
    * Are there common reasons or patterns behind the loss of key accounts to competitors, and how can these be addressed?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance customer relationship management to better understand the reasons for customer defection and tailor win-back strategies accordingly.
    * Regularly monitor competitor activities and offerings to identify areas where the organization can differentiate and regain lost customers.
    * Invest in customer experience improvements to reduce the likelihood of losing key accounts to competitors.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of competitive win-back rates over time.
    * Comparison bar charts displaying the organization\'s win-back rates versus those of key competitors.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low competitive win-back rate may indicate a lack of effective strategies for regaining lost customers, leading to potential revenue loss.
    * High win-back rates may also suggest aggressive pricing or unsustainable efforts to win back customers, impacting profitability.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage win-back efforts and customer interactions.
    * Competitive intelligence tools to gather insights on competitor activities and customer preferences.
    """,
    integration_points="""
    * Integrate win-back rate data with customer feedback and satisfaction metrics to understand the impact of win-back efforts on overall customer sentiment.
    * Link win-back strategies with sales and marketing automation systems to ensure consistent and targeted outreach to lost customers.
    """,
    change_impact_analysis="""
    * Improving the competitive win-back rate can positively impact overall sales performance and customer retention, contributing to long-term revenue growth.
    * However, overly aggressive win-back strategies may strain customer relationships and brand reputation, affecting long-term customer loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Competitive Analysis", "Customer", "Key Account", "Key Account Manager", "Lost Sale", "Renewal Management"]
    }
)
