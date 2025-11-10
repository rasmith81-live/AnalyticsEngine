"""
Referral Rate KPI

Module: Business Development
"""

from analytics_models import KPI

REFERRAL_RATE = KPI(
    name="Referral Rate",
    code="REFERRAL_RATE",
    description="The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.",
    
    # Definition & Context
    kpi_definition="The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.",
    expected_business_insights="Indicates customer satisfaction and the effectiveness of referral programs.",
    measurement_approach="Calculates the percentage of new customers acquired through referrals.",
    
    # Calculation
    formula="(Number of New Customers from Referrals / Total Number of New Customers) * 100",
    
    # Analysis
    trend_analysis="An increasing referral rate may indicate a growing customer base and higher customer satisfaction, leading to more organic growth. A decreasing rate could signal a decline in customer advocacy and satisfaction, potentially impacting future sales opportunities.",
    diagnostic_questions=['What methods are currently in place to encourage and track customer referrals?', 'Are there specific customer segments or products that generate more referrals than others?'],
    actionable_steps={
        "operational": ['Implement a formal referral program to incentivize and reward customers for referring new business.'],
        "strategic": ['Regularly survey customers to gauge satisfaction and identify areas for improvement that could impact referral rates.', 'Provide exceptional customer service to increase the likelihood of positive referrals and recommendations.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing referral rates over time to identify trends and seasonal variations.', 'Pie charts to compare referral sources and identify which customers are most likely to refer new business.']
    ],
    risk_warnings=['A low referral rate may indicate dissatisfaction among existing customers, leading to potential churn and lost revenue.', 'Dependence on referrals for new business without a proactive sales strategy may lead to inconsistent or unpredictable revenue growth.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track customer interactions and identify potential referral opportunities.', 'Referral management platforms to automate and streamline the referral process, making it easier for customers to refer new business.'],
    integration_points=['Integrate referral tracking with sales and marketing systems to measure the impact of referrals on overall revenue and customer acquisition costs.', 'Link referral data with customer satisfaction metrics to understand the relationship between advocacy and customer experience.'],
    
    # Impact
    change_impact="Improving the referral rate can lead to more cost-effective customer acquisition and higher lifetime customer value. Conversely, a declining referral rate may require increased investment in traditional marketing and sales efforts to maintain or grow the customer base.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Quarterly Business Review", "Referral"]
    }
)
