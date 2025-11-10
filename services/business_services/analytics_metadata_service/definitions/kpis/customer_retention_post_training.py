"""
Customer Retention Post-Training KPI

The change in customer retention rates attributed to improved sales rep performance post-training.
"""

from analytics_models import KPI

CUSTOMER_RETENTION_POST_TRAINING = KPI(
    name="Customer Retention Post-Training",
    code="CUSTOMER_RETENTION_POST_TRAINING",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The change in customer retention rates attributed to improved sales rep performance post-training.",
    kpi_definition="The change in customer retention rates attributed to improved sales rep performance post-training.",
    expected_business_insights="Indicates the impact of sales training on customer loyalty and satisfaction with sales interactions.",
    measurement_approach="The percentage of customers who continue to do business with the company following interactions with recently trained sales reps.",
    
    # Formula
    formula="(Number of Customers Retained Post-Training / Total Number of Customers Engaged Post-Training) * 100",
    calculation_formula="(Number of Customers Retained Post-Training / Total Number of Customers Engaged Post-Training) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer retention rate post-training may indicate that the sales reps are effectively applying the skills and knowledge gained from the training.
    * A decreasing rate could signal that the training content or delivery method needs to be reassessed for effectiveness.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or products that show a significant change in retention rates post-training?
    * How does the customer retention rate post-training compare with industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular follow-up sessions or refresher courses to reinforce the training and ensure continued application of new skills.
    * Provide ongoing coaching and support to sales reps to address specific challenges or areas for improvement identified post-training.
    * Collect feedback from customers to understand the impact of the training on their experience and satisfaction.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in customer retention rates over time, pre and post-training.
    * Comparison bar charts to visualize the change in retention rates across different sales reps or teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A decline in customer retention post-training may lead to lost revenue and damage to the company\'s reputation.
    * Consistently high retention rates without improvement may indicate a lack of impact from the training, leading to wasted resources.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer retention rates and feedback post-training.
    * Sales performance management platforms to monitor the application of training concepts and identify areas for improvement.
    """,
    integration_points="""
    * Integrate customer retention data with sales training performance metrics to assess the direct impact of training on retention rates.
    * Link customer feedback systems with training evaluation to understand the correlation between customer satisfaction and training effectiveness.
    """,
    change_impact_analysis="""
    * Improving customer retention post-training can lead to increased sales, customer loyalty, and positive word-of-mouth referrals.
    * Conversely, a decline in retention rates may require additional resources to address customer dissatisfaction and potential loss of business.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
