"""
Customer Feedback on Sales Interactions KPI

A measure of customer impressions and feedback regarding interactions with trained sales reps.
"""

from analytics_models import KPI

CUSTOMER_FEEDBACK_ON_SALES_INTERACTIONS = KPI(
    name="Customer Feedback on Sales Interactions",
    code="CUSTOMER_FEEDBACK_ON_SALES_INTERACTIONS",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="A measure of customer impressions and feedback regarding interactions with trained sales reps.",
    kpi_definition="A measure of customer impressions and feedback regarding interactions with trained sales reps.",
    expected_business_insights="Can suggest the effectiveness of sales training in customer-facing scenarios and indicate potential improvements in sales tactics.",
    measurement_approach="A measure of customer satisfaction and feedback regarding interactions with sales reps.",
    
    # Formula
    formula="Quality Score Derived from Customer Feedback Surveys",
    calculation_formula="Quality Score Derived from Customer Feedback Surveys",
    
    # Analysis
    trend_analysis="""
    * Increasing positive feedback may indicate improved sales rep performance or customer satisfaction.
    * Decreasing feedback or a rise in negative comments could signal declining sales rep effectiveness or customer dissatisfaction.
    """,
    diagnostic_questions="""
    * Are there common themes or patterns in the feedback received from customers?
    * How do our sales reps\' interactions compare with industry benchmarks or customer expectations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing training and coaching for sales reps to enhance their communication and relationship-building skills.
    * Implement a feedback loop for sales reps to receive and act upon customer feedback in real-time.
    * Utilize customer relationship management (CRM) tools to track and analyze customer interactions for continuous improvement.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of positive and negative feedback over time.
    * Word clouds to visually represent common themes or keywords in customer feedback.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently negative feedback may lead to customer churn and loss of revenue.
    * Ignoring or mishandling customer feedback can damage brand reputation and trust.
    """,
    tracking_tools="""
    * CRM systems with built-in feedback management features, such as Salesforce or HubSpot.
    * Social listening tools to monitor and analyze customer sentiment across various channels.
    """,
    integration_points="""
    * Integrate customer feedback data with sales performance metrics to identify correlations and areas for improvement.
    * Link customer feedback with employee performance evaluations to align incentives with customer satisfaction goals.
    """,
    change_impact_analysis="""
    * Improving customer feedback can lead to increased customer retention and lifetime value.
    * However, focusing solely on positive feedback may neglect areas of improvement and hinder overall sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
