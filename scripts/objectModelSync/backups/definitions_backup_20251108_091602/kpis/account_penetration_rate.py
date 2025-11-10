"""
Account Penetration Rate KPI

Module: Business Development
"""

from analytics_models import KPI

ACCOUNT_PENETRATION_RATE = KPI(
    name="Account Penetration Rate",
    code="ACCOUNT_PENETRATION_RATE",
    description="The percentage of a customer account's potential that has been realized by the sales team, indicating the depth of the relationship.",
    
    # Definition & Context
    kpi_definition="The percentage of a customer account's potential that has been realized by the sales team, indicating the depth of the relationship.",
    expected_business_insights="Indicates the success of upselling or cross-selling strategies within an existing customer base.",
    measurement_approach="Measures the percentage of products or services sold within an existing account.",
    
    # Calculation
    formula="(Number of Products or Services Sold to an Account / Total Number of Available Offerings) * 100",
    
    # Analysis
    trend_analysis="An increasing account penetration rate may indicate successful upselling or cross-selling efforts, as well as deeper customer engagement. A decreasing rate could signal a lack of focus on growing existing accounts or potential dissatisfaction among customers.",
    diagnostic_questions=['What strategies are in place to identify and capitalize on upselling or cross-selling opportunities within existing accounts?', 'Are there any common reasons why customers may not be fully utilizing our products or services, and how can we address those?'],
    actionable_steps={
        "operational": ['Implement a structured account management program to regularly assess customer needs and identify opportunities for deeper engagement.'],
        "strategic": ['Provide sales teams with training on consultative selling techniques to uncover additional customer needs and opportunities for expansion.', 'Establish metrics and incentives to encourage sales representatives to focus on growing existing accounts.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing account penetration rate over time to visualize trends and identify periods of growth or decline.', 'Pie charts to compare the distribution of realized potential across different customer accounts.']
    ],
    risk_warnings=['A low account penetration rate may lead to missed revenue opportunities and increased vulnerability to competitive incursions.', 'Overemphasis on upselling without considering customer satisfaction and value delivery may lead to churn and negative brand perception.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track customer interactions, preferences, and potential opportunities for growth.', 'Analytical tools to segment customer accounts based on potential and track progress in realizing that potential.'],
    integration_points=['Integrate account penetration rate data with customer support systems to identify potential issues or opportunities for additional sales or support.', 'Link with marketing automation platforms to align sales efforts with targeted campaigns aimed at existing customers.'],
    
    # Impact
    change_impact="Improving account penetration rate can lead to increased customer lifetime value and loyalty, impacting overall revenue and profitability. However, a singular focus on account penetration without considering customer satisfaction and value delivery may lead to increased churn and decreased long-term profitability.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Product", "Quarterly Business Review", "Sale", "Sales Team"]
    }
)
