"""
Land-and-Expand Success Rate KPI

Module: Business Development
"""

from analytics_models import KPI

LAND_AND_EXPAND_SUCCESS_RATE = KPI(
    name="Land-and-Expand Success Rate",
    code="LAND_AND_EXPAND_SUCCESS_RATE",
    description="The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.",
    
    # Definition & Context
    kpi_definition="The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.",
    expected_business_insights="Indicates the effectiveness of account management strategies and the potential for customer base expansion.",
    measurement_approach="Measures the growth in revenue from existing customers through upselling and cross-selling.",
    
    # Calculation
    formula="(Revenue from Upselling and Cross-Selling to Existing Customers / Total Revenue from Existing Customers) * 100",
    
    # Analysis
    trend_analysis="An increasing land-and-expand success rate may indicate strong customer satisfaction and a growing product portfolio that meets customer needs. A decreasing rate could signal challenges in upselling or cross-selling to existing customers, potentially due to product fit or value perception issues.",
    diagnostic_questions=['Are there specific products or services that have a higher success rate in leading to subsequent sales within the same account?', 'How does our land-and-expand success rate compare with industry benchmarks or with different customer segments?'],
    actionable_steps={
        "operational": ['Invest in customer relationship management (CRM) systems to better track customer interactions and identify upsell or cross-sell opportunities.'],
        "strategic": ['Provide sales teams with training and resources to effectively communicate the value of additional products or services to existing customers.', 'Regularly review customer feedback and usage data to identify opportunities for expansion within existing accounts.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of initial sales and subsequent sales within the same account over time.', 'Stacked bar charts comparing the contribution of different products or services to the overall land-and-expand success rate.']
    ],
    risk_warnings=['A declining land-and-expand success rate may lead to missed revenue opportunities and reduced customer lifetime value.', 'High variability in the success rate across different customer segments could indicate challenges in understanding and meeting diverse customer needs.'],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM platforms with built-in analytics and reporting capabilities to track and analyze customer expansion opportunities.', 'Data analytics tools to identify patterns and correlations between initial sales and subsequent sales within the same account.'],
    integration_points=['Integrate land-and-expand success rate data with customer support systems to identify opportunities for upselling or cross-selling during customer interactions.', 'Link with product development and marketing teams to align offerings and messaging with customer needs and preferences.'],
    
    # Impact
    change_impact="Improving the land-and-expand success rate can lead to increased customer lifetime value and overall revenue growth. Conversely, a declining success rate may indicate challenges in product-market fit or customer satisfaction, impacting long-term business performance.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Success Manager", "Key Account", "Key Account Manager", "Lead", "Lead Qualification", "Product", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
