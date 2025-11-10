"""
Account Coverage Ratio KPI

Module: Business Development
"""

from analytics_models import KPI

ACCOUNT_COVERAGE_RATIO = KPI(
    name="Account Coverage Ratio",
    code="ACCOUNT_COVERAGE_RATIO",
    description="The ratio of accounts actively managed by the sales team compared to the total number of target accounts.",
    
    # Definition & Context
    kpi_definition="The ratio of accounts actively managed by the sales team compared to the total number of target accounts.",
    expected_business_insights="Reveals the extent of market penetration and opportunity reach by the sales team.",
    measurement_approach="Considers the number of accounts managed by a sales representative against the total number of target accounts in the market.",
    
    # Calculation
    formula="(Number of Accounts Managed by Sales Rep / Total Target Accounts) * 100",
    
    # Analysis
    trend_analysis="An increasing account coverage ratio may indicate a more proactive and effective sales team, leading to potential growth in sales. A decreasing ratio could signal a lack of focus on target accounts or a need for additional resources to manage accounts effectively.",
    diagnostic_questions=['Are there specific target accounts that are consistently being overlooked or undermanaged?', 'How does our account coverage ratio compare with industry benchmarks or with our competitors?'],
    actionable_steps={
        "operational": ['Implement a clear account prioritization strategy to ensure that the most important accounts receive appropriate attention.'],
        "strategic": ['Provide ongoing training and support for the sales team to improve their account management skills.', 'Utilize customer relationship management (CRM) software to track and manage interactions with target accounts.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Pie charts showing the distribution of accounts by level of management (e.g., actively managed, undermanaged, not managed).', 'Line graphs to track changes in the account coverage ratio over time.']
    ],
    risk_warnings=['A low account coverage ratio may result in missed sales opportunities and decreased customer satisfaction.', 'An excessively high ratio may lead to inefficiencies and decreased effectiveness in managing accounts.'],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM systems such as Salesforce or HubSpot for tracking and managing customer interactions.', 'Data analytics tools to identify trends and patterns in account coverage and sales performance.'],
    integration_points=['Integrate account coverage data with sales performance metrics to understand the impact of effective account management on overall sales results.', 'Link account coverage information with marketing automation platforms to align sales efforts with targeted marketing campaigns.'],
    
    # Impact
    change_impact="Improving the account coverage ratio can lead to increased sales and customer satisfaction, but may require additional resources and investment in sales capabilities. Conversely, a declining account coverage ratio may result in missed opportunities and decreased revenue.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "KEY_ACCOUNT_MANAGEMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Key Account", "Key Account Manager", "Market Segment", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
