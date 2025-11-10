"""
Customer Onboarding Efficacy KPI

Module: Business Development
"""

from analytics_models import KPI

CUSTOMER_ONBOARDING_EFFICACY = KPI(
    name="Customer Onboarding Efficacy",
    code="CUSTOMER_ONBOARDING_EFFICACY",
    description="The effectiveness of the onboarding process for new customers, measured by their time to value and overall satisfaction.",
    
    # Definition & Context
    kpi_definition="The effectiveness of the onboarding process for new customers, measured by their time to value and overall satisfaction.",
    expected_business_insights="Highlights the effectiveness of onboarding processes and can point out areas needing improvement.",
    measurement_approach="Considers the success rate of new customer integration into product or service use.",
    
    # Calculation
    formula="(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
    
    # Analysis
    trend_analysis="An increasing time to value may indicate a more complex onboarding process or issues with product/service understanding. Decreasing overall satisfaction could signal gaps in the onboarding process or a lack of personalized support.",
    diagnostic_questions=['Are there specific stages in the onboarding process where customers tend to get stuck or drop off?', 'How does our customer satisfaction with onboarding compare to industry benchmarks or competitors?'],
    actionable_steps={
        "operational": ['Personalize the onboarding process to address specific customer needs and pain points.'],
        "strategic": ['Provide clear and comprehensive training materials to expedite the time to value for new customers.', 'Implement regular check-ins and feedback sessions to ensure ongoing satisfaction and address any issues promptly.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the average time to value over different periods.', 'Stacked bar charts comparing satisfaction levels at different stages of the onboarding process.']
    ],
    risk_warnings=['Low satisfaction with onboarding can lead to increased churn and negative word-of-mouth, impacting future sales.', 'A prolonged time to value may result in customer frustration and reduced usage of the product/service.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track onboarding progress and satisfaction levels.', 'Survey and feedback tools to gather insights from customers about their onboarding experience.'],
    integration_points=['Integrate onboarding data with customer success platforms to align ongoing support with initial onboarding needs.', 'Link onboarding metrics with sales performance data to understand the impact of onboarding on customer lifetime value.'],
    
    # Impact
    change_impact="Improving the onboarding process can lead to higher customer retention and increased lifetime value. However, changes to the onboarding process may require additional resources and training, impacting operational costs.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Sales Process Workflow", "Service Level Agreement"]
    }
)
