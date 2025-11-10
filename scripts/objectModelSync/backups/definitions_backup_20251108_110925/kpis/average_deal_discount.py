"""
Average Deal Discount KPI

Module: Business Development
"""

from analytics_models import KPI

AVERAGE_DEAL_DISCOUNT = KPI(
    name="Average Deal Discount",
    code="AVERAGE_DEAL_DISCOUNT",
    description="The average percentage discount applied to deals, which can reflect the sales team's negotiation skills and pricing strategy.",
    
    # Definition & Context
    kpi_definition="The average percentage discount applied to deals, which can reflect the sales team's negotiation skills and pricing strategy.",
    expected_business_insights="Provides insights into sales team negotiation effectiveness and pricing strategies.",
    measurement_approach="Considers the average percentage that the list price is reduced to close a deal.",
    
    # Calculation
    formula="(Total Discounts Given / Number of Deals Closed) * 100",
    
    # Analysis
    trend_analysis="An increasing average deal discount may indicate a need for better pricing strategies or a lack of negotiation skills among the sales team. A decreasing average deal discount could signal improved negotiation tactics or a shift towards value-based selling rather than discounting.",
    diagnostic_questions=['Are there specific products or customer segments that consistently receive higher discounts?', "How does our average deal discount compare with industry benchmarks or competitors' pricing strategies?"],
    actionable_steps={
        "operational": ['Provide sales teams with training on value-based selling and negotiation techniques.'],
        "strategic": ['Implement pricing analytics tools to identify opportunities for more strategic discounting.', 'Regularly review and update pricing strategies based on market conditions and customer feedback.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the average deal discount over time to identify trends and seasonal variations.', 'Scatter plots comparing deal size and discount percentage to understand the relationship between the two variables.']
    ],
    risk_warnings=["Consistently high average deal discounts can erode profit margins and devalue the company's offerings in the market.", 'Overly aggressive discounting may lead to customer expectations of perpetual discounts, impacting long-term revenue potential.'],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM systems with built-in pricing optimization modules to track and analyze discounting patterns.', 'Business intelligence tools for in-depth analysis of deal discounting and its impact on sales performance.'],
    integration_points=['Integrate average deal discount data with sales performance metrics to understand the relationship between discounting and revenue generation.', 'Link discounting information with customer relationship management systems to track the impact of discounts on customer retention and satisfaction.'],
    
    # Impact
    change_impact="Reducing average deal discounts may initially impact sales volume but can lead to improved profitability and customer perception in the long run. Conversely, increasing average deal discounts may boost short-term sales but could harm the company's brand image and financial health over time.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Channel Deal", "Deal", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
