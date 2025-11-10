"""
Average Sales Discount KPI

The average discount rate applied to sales during a particular period.
"""

from analytics_models import KPI

AVERAGE_SALES_DISCOUNT = KPI(
    name="Average Sales Discount",
    code="AVERAGE_SALES_DISCOUNT",
    category="Outside Sales",
    
    # Core Definition
    description="The average discount rate applied to sales during a particular period.",
    kpi_definition="The average discount rate applied to sales during a particular period.",
    expected_business_insights="Reflects on the company’s pricing strategy and its impact on profitability; provides insights for future pricing adjustments.",
    measurement_approach="Identifies the average discount percentage offered to customers to close deals.",
    
    # Formula
    formula="Sum of all Discount Percentages Offered / Number of Discounted Deals",
    calculation_formula="Sum of all Discount Percentages Offered / Number of Discounted Deals",
    
    # Analysis
    trend_analysis="""
    * Increasing average sales discount may indicate a need to move excess inventory or meet aggressive sales targets.
    * Decreasing average sales discount could signal improved pricing strategies or increased customer loyalty.
    """,
    diagnostic_questions="""
    * Are there specific products or customer segments that consistently receive higher discounts?
    * How does our average sales discount compare with industry benchmarks or competitor pricing?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement dynamic pricing strategies based on customer behavior and market conditions.
    * Provide sales teams with negotiation training to maintain margins while meeting customer needs.
    * Analyze the impact of discounts on overall profitability to ensure they are strategic and sustainable.
    """,
    visualization_suggestions="""
    * Line charts showing average sales discount over time to identify seasonal or cyclical patterns.
    * Pie charts comparing discount rates across different product categories or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Excessive discounting can erode profit margins and devalue the brand in the eyes of customers.
    * Consistently low discount rates may indicate an inability to compete effectively in the market.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track discounting trends by customer and sales representative.
    * Price optimization tools to analyze pricing elasticity and recommend optimal discount levels.
    """,
    integration_points="""
    * Integrate average sales discount data with customer satisfaction metrics to understand the impact of discounts on customer loyalty.
    * Link discount rates with inventory management systems to ensure discounts are aligned with inventory levels and turnover.
    """,
    change_impact_analysis="""
    * Increasing average sales discount may boost short-term sales but could impact long-term profitability and brand perception.
    * Decreasing average sales discount may improve margins but could require additional efforts to maintain customer satisfaction and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
