"""
Sales Target Achievement KPI

The percentage of sales targets or quotas met by the sales team.
"""

from analytics_models import KPI

SALES_TARGET_ACHIEVEMENT = KPI(
    name="Sales Target Achievement",
    code="SALES_TARGET_ACHIEVEMENT",
    category="Inside Sales",
    
    # Core Definition
    description="The percentage of sales targets or quotas met by the sales team.",
    kpi_definition="The percentage of sales targets or quotas met by the sales team.",
    expected_business_insights="Assesses the performance of sales teams and individuals against their goals.",
    measurement_approach="The percentage of sales targets or quotas met.",
    
    # Formula
    formula="(Total Sales / Sales Target) * 100",
    calculation_formula="(Total Sales / Sales Target) * 100",
    
    # Analysis
    trend_analysis="""
    * Consistently meeting or exceeding sales targets may indicate a strong market demand or effective sales strategies.
    * A declining trend in sales target achievement could signal changes in customer preferences, increased competition, or internal issues affecting sales performance.
    """,
    diagnostic_questions="""
    * Are there specific products or regions where sales targets are consistently missed?
    * How does our sales target achievement compare with industry benchmarks or seasonal variations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and support for underperforming regions or products.
    * Regularly review and adjust sales targets based on market conditions and internal capabilities.
    * Implement incentive programs to motivate the sales team and drive performance towards meeting targets.
    """,
    visualization_suggestions="""
    * Line charts showing sales target achievement over time for different regions or product categories.
    * Pie charts comparing the percentage of sales targets met versus those missed.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently missing sales targets can lead to revenue shortfalls and impact overall business performance.
    * High sales target achievement without proper capacity planning may strain resources and lead to fulfillment issues.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track sales performance and customer interactions.
    * Sales forecasting tools to accurately predict future sales targets and adjust strategies accordingly.
    """,
    integration_points="""
    * Integrate sales target achievement data with financial systems to understand the impact on revenue and profitability.
    * Link with marketing analytics to align sales efforts with effective lead generation and customer acquisition strategies.
    """,
    change_impact_analysis="""
    * Improving sales target achievement can lead to increased revenue and market share, but may also require additional resources and investment in sales infrastructure.
    * Consistently missing sales targets can impact employee morale, customer trust, and overall business growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07"
        "replaces": ["SALES_QUOTA_ACHIEVEMENT", "SALES_TARGET_ACHIEVEMENT_RATE"],
        "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
