"""
Strategic Account ROI KPI

Return on investment for each strategic account, factoring in the costs of sales and support.
"""

from analytics_models import KPI

STRATEGIC_ACCOUNT_ROI = KPI(
    name="Strategic Account ROI",
    code="STRATEGIC_ACCOUNT_ROI",
    category="Key Account Management",
    
    # Core Definition
    description="Return on investment for each strategic account, factoring in the costs of sales and support.",
    kpi_definition="Return on investment for each strategic account, factoring in the costs of sales and support.",
    expected_business_insights="Evaluates the financial effectiveness of strategic account investments and guides decision-making.",
    measurement_approach="Measures the return on investment for resources dedicated to managing strategic accounts.",
    
    # Formula
    formula="(Net Profit from Strategic Account / Cost of Investment in Strategic Account) * 100",
    calculation_formula="(Net Profit from Strategic Account / Cost of Investment in Strategic Account) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing ROI for strategic accounts may indicate successful sales and support efforts, leading to higher customer satisfaction and loyalty.
    * Decreasing ROI could signal inefficiencies in sales and support processes, potential dissatisfaction among strategic accounts, or increased competition.
    """,
    diagnostic_questions="""
    * Are there specific strategic accounts that consistently show higher or lower ROI, and what factors contribute to this trend?
    * How does the ROI of strategic accounts compare with industry benchmarks or with the ROI of non-strategic accounts?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and adjust sales and support strategies for each strategic account based on their unique needs and potential for growth.
    * Invest in training and development for sales and support teams to ensure they are equipped to effectively manage strategic accounts.
    * Implement customer relationship management (CRM) systems to better track interactions and identify opportunities for improving ROI.
    """,
    visualization_suggestions="""
    * Line charts showing the ROI of each strategic account over time to identify trends and patterns.
    * Pareto charts to visualize the distribution of ROI across strategic accounts and prioritize efforts accordingly.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low ROI for strategic accounts may lead to loss of key customers and revenue.
    * High ROI for certain strategic accounts may create over-reliance on a few customers, increasing vulnerability to market changes.
    """,
    tracking_tools="""
    * CRM software like Salesforce or HubSpot for tracking and managing interactions with strategic accounts.
    * Business intelligence tools such as Tableau or Power BI for analyzing ROI data and identifying opportunities for improvement.
    """,
    integration_points="""
    * Integrate ROI data with sales and marketing systems to align efforts and resources towards high-potential strategic accounts.
    * Link ROI tracking with customer feedback and satisfaction metrics to gain a comprehensive view of strategic account performance.
    """,
    change_impact_analysis="""
    * Improving ROI for strategic accounts can lead to increased revenue and customer lifetime value, but may require additional resources and investments.
    * Conversely, declining ROI may indicate the need for strategic shifts in sales and support strategies to prevent further losses.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Key Account", "Key Account Manager", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Initiative", "Strategic Review", "Support Ticket"]
    }
)
