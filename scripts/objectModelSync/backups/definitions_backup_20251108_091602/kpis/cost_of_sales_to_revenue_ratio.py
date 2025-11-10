"""
Cost of Sales to Revenue Ratio KPI

The ratio of the cost of sales (including salaries, commissions, expenses) to the total revenue generated.
"""

from analytics_models import KPI

COST_OF_SALES_TO_REVENUE_RATIO = KPI(
    name="Cost of Sales to Revenue Ratio",
    code="COST_OF_SALES_TO_REVENUE_RATIO",
    category="Outside Sales",
    
    # Core Definition
    description="The ratio of the cost of sales (including salaries, commissions, expenses) to the total revenue generated.",
    kpi_definition="The ratio of the cost of sales (including salaries, commissions, expenses) to the total revenue generated.",
    expected_business_insights="Offers a view of how much the company spends to generate sales relative to the revenue, indicating overall profitability.",
    measurement_approach="Compares the total cost of sales to the total revenue generated.",
    
    # Formula
    formula="Total Cost of Sales / Total Revenue",
    calculation_formula="Total Cost of Sales / Total Revenue",
    
    # Analysis
    trend_analysis="""
    * An increasing cost of sales to revenue ratio may indicate rising expenses relative to revenue, potentially signaling inefficiencies in the sales process or increased costs that are not being offset by revenue growth.
    * A decreasing ratio could suggest improved cost management, increased sales efficiency, or a decline in costs relative to revenue.
    """,
    diagnostic_questions="""
    * What specific cost components are driving the increase in the cost of sales to revenue ratio?
    * How does our cost of sales to revenue ratio compare with industry benchmarks or historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement cost control measures to reduce unnecessary expenses and improve sales efficiency.
    * Explore opportunities to increase revenue through upselling, cross-selling, or expanding into new markets.
    * Regularly review and optimize sales compensation and incentive structures to ensure alignment with revenue generation.
    """,
    visualization_suggestions="""
    * Line charts to track the trend of the cost of sales to revenue ratio over time.
    * Stacked bar charts to visually represent the composition of the cost of sales and its relationship to revenue.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A high cost of sales to revenue ratio can erode profitability and indicate potential financial challenges.
    * Chronic increases in the ratio may point to systemic issues in sales management, resource allocation, or pricing strategies.
    """,
    tracking_tools="""
    * CRM systems with robust reporting capabilities to track sales-related expenses and revenue generation.
    * Business intelligence tools for in-depth analysis of cost components and revenue sources.
    """,
    integration_points="""
    * Integrate cost of sales to revenue ratio analysis with financial reporting systems for a comprehensive view of sales performance.
    * Link with sales forecasting and planning systems to align resource allocation with revenue targets.
    """,
    change_impact_analysis="""
    * Reducing the cost of sales to revenue ratio may lead to improved profitability but could require strategic shifts in sales operations and resource allocation.
    * Conversely, a high ratio can impact overall financial health and may necessitate changes in pricing, sales strategies, or cost management.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
