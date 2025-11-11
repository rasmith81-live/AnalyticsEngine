"""
Deal Slippage Rate KPI

The rate at which deals slip past their expected close date.
"""

DEAL_SLIPPAGE_RATE = {
    "code": "DEAL_SLIPPAGE_RATE",
    "name": "Deal Slippage Rate",
    "description": "The rate at which deals slip past their expected close date.",
    "formula": "(Number of Deals Slipped / Total Number of Deals Expected to Close) * 100",
    "calculation_formula": "(Number of Deals Slipped / Total Number of Deals Expected to Close) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The rate at which deals slip past their expected close date.",
    "expected_business_insights": "Indicates issues with the sales process or forecasting accuracy, prompting the need for adjustments.",
    "measurement_approach": "The percentage of deals that move past their expected close date.",
    "trend_analysis": """
    * Increasing deal slippage rate may indicate issues with sales forecasting or longer sales cycles.
    * A decreasing rate could signal improved sales pipeline management or more accurate sales projections.
    """,
    "diagnostic_questions": """
    * Are there common factors causing deals to slip, such as specific customer objections or internal process bottlenecks?
    * How does our deal slippage rate compare with industry averages or benchmarks for similar products or services?
    """,
    "actionable_tips": """
    * Implement regular pipeline reviews to identify potential deal slippage early and take proactive measures.
    * Provide additional sales training or resources to address common reasons for deal slippage.
    * Consider adjusting sales projections and timelines based on historical deal slippage patterns.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of deal slippage rate over time.
    * Pareto charts to identify the most common reasons for deal slippage.
    """,
    "risk_warnings": """
    * High deal slippage rates can lead to missed revenue targets and impact overall sales performance.
    * Consistently high deal slippage may indicate underlying issues in the sales process that need to be addressed.
    """,
    "tracking_tools": """
    * CRM systems with robust pipeline management and forecasting capabilities to track deal progress and identify potential slippage.
    * Sales analytics platforms to analyze historical data and identify patterns leading to deal slippage.
    """,
    "integration_points": """
    * Integrate deal slippage rate tracking with sales performance management systems to align incentives with timely deal closures.
    * Link with customer relationship management systems to communicate transparently with customers about potential delays.
    """,
    "change_impact_analysis": """
    * Reducing deal slippage can lead to improved revenue predictability and better resource allocation.
    * However, overly aggressive measures to reduce deal slippage may put undue pressure on sales teams and impact morale.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Deal", "Deal", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES", "SALES_OPERATIONS"],
    "module_code": "INSIDE_SALES",
}
