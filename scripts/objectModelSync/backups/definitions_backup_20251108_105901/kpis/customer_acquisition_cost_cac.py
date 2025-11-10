"""
Customer Acquisition Cost (CAC) KPI

Module: Business Development
"""

from analytics_models import KPI

CUSTOMER_ACQUISITION_COST_CAC = KPI(
    name="Customer Acquisition Cost (CAC)",
    code="CUSTOMER_ACQUISITION_COST_CAC",
    description="The cost of acquiring a new customer, including marketing and sales expenses.",
    
    # Definition & Context
    kpi_definition="The cost of acquiring a new customer, including marketing and sales expenses.",
    expected_business_insights="Evaluates the efficiency of marketing and sales investments and helps in strategic decision-making.",
    measurement_approach="Measures the total cost associated with acquiring a new customer.",
    
    # Calculation
    formula="(Total Cost of Sales and Marketing) / (Number of New Customers Acquired)",
    
    # Analysis
    trend_analysis="Customer acquisition cost may increase over time due to rising advertising costs or competitive pressures. A decreasing trend in CAC could indicate improved marketing efficiency or better targeting of high-value customers.",
    diagnostic_questions=['Are there specific marketing channels or campaigns that have higher CAC, and what can be done to optimize them?', 'How does our CAC compare with industry benchmarks, and what factors contribute to any deviations?'],
    actionable_steps={
        "operational": ['Focus on improving lead quality to reduce the overall cost of acquisition.'],
        "strategic": ['Implement marketing automation to streamline lead nurturing and conversion processes.', 'Explore partnerships or referral programs to acquire customers at a lower cost.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing CAC trends over time and by different marketing channels.', 'Comparison bar charts to visualize CAC differences between customer segments or product lines.']
    ],
    risk_warnings=['High CAC can lead to reduced profitability if not balanced with customer lifetime value.', 'Fluctuations in CAC may indicate market volatility or inefficiencies in the sales and marketing processes.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) systems to track the effectiveness of different marketing campaigns.', 'Marketing analytics platforms like Google Analytics or Adobe Analytics to measure and optimize CAC.'],
    integration_points=['Integrate CAC tracking with sales performance metrics to understand the overall cost of acquiring and retaining customers.', 'Link CAC data with customer satisfaction scores to assess the quality of acquired customers.'],
    
    # Impact
    change_impact="Reducing CAC may require changes in marketing strategies and could impact short-term revenue. Increased focus on CAC optimization may lead to more targeted and efficient sales and marketing efforts.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
