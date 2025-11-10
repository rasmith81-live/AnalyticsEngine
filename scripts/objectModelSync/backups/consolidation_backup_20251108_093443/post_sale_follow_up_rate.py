"""
Post-Sale Follow-Up Rate KPI

Module: Business Development
"""

from analytics_models import KPI

POST_SALE_FOLLOW_UP_RATE = KPI(
    name="Post-Sale Follow-Up Rate",
    code="POST_SALE_FOLLOW_UP_RATE",
    description="The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.",
    
    # Definition & Context
    kpi_definition="The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.",
    expected_business_insights="Reveals commitment to customer service and can impact customer retention and satisfaction.",
    measurement_approach="Tracks the percentage of completed sales that receive post-sale follow-up.",
    
    # Calculation
    formula="(Number of Completed Sales with Follow-Up / Total Number of Completed Sales) * 100",
    
    # Analysis
    trend_analysis="An increasing post-sale follow-up rate may indicate a proactive sales team focused on customer satisfaction and retention. A decreasing rate could signal a lack of attention to post-sale customer engagement, leading to potential churn and lost opportunities for repeat business.",
    diagnostic_questions=['Are there specific customer segments or product categories that receive more follow-up than others?', 'How do our post-sale follow-up rates compare with industry benchmarks or with our competitors?'],
    actionable_steps={
        "operational": ['Implement a structured post-sale follow-up process to ensure all customers are contacted within a specified timeframe.'],
        "strategic": ['Leverage customer relationship management (CRM) software to automate and track follow-up activities.', 'Train and incentivize the sales team to prioritize post-sale engagement and relationship-building.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of post-sale follow-up rates over time.', 'Pie charts to compare follow-up rates across different customer segments or product categories.']
    ],
    risk_warnings=['Low post-sale follow-up rates can result in dissatisfied customers and decreased likelihood of repeat business.', 'Inconsistent follow-up may lead to missed opportunities for upselling or cross-selling to existing customers.'],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM systems such as Salesforce or HubSpot for tracking and managing customer interactions.', 'Email marketing platforms like Mailchimp or Constant Contact for automated follow-up communications.'],
    integration_points=['Integrate post-sale follow-up data with customer satisfaction surveys to measure the impact of follow-up activities on customer loyalty.', 'Link follow-up activities with sales performance metrics to understand the correlation between post-sale engagement and revenue generation.'],
    
    # Impact
    change_impact="Improving post-sale follow-up can lead to increased customer satisfaction and loyalty, potentially boosting overall sales performance. Conversely, neglecting post-sale engagement may result in reduced customer retention and negative impact on brand reputation.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Lost Sale", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
