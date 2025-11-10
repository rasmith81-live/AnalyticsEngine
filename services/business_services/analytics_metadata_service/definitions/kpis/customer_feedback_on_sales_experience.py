"""
Customer Feedback on Sales Experience KPI

Customer perceptions of their buying experience, which can influence satisfaction, loyalty, and future sales.
"""

from analytics_models import KPI

CUSTOMER_FEEDBACK_ON_SALES_EXPERIENCE = KPI(
    name="Customer Feedback on Sales Experience",
    code="CUSTOMER_FEEDBACK_ON_SALES_EXPERIENCE",
    category="Sales Strategy",
    
    # Core Definition
    description="Customer perceptions of their buying experience, which can influence satisfaction, loyalty, and future sales.",
    kpi_definition="Customer perceptions of their buying experience, which can influence satisfaction, loyalty, and future sales.",
    expected_business_insights="Provides insights into the customer journey and identifies strengths and weaknesses in the sales process.",
    measurement_approach="Considers qualitative data from customer surveys, interviews, and feedback forms.",
    
    # Formula
    formula="Qualitative analysis, no standard formula",
    calculation_formula="Qualitative analysis, no standard formula",
    
    # Analysis
    trend_analysis="""
    * An increasing customer feedback on sales experience may indicate a decline in customer satisfaction and loyalty.
    * A decreasing feedback may signal improved sales processes and customer interactions.
    """,
    diagnostic_questions="""
    * Are there common themes or issues mentioned in customer feedback?
    * How does our customer feedback compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular customer feedback surveys to gather insights and identify areas for improvement.
    * Train sales teams to actively listen to customer concerns and address them effectively.
    * Use customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer feedback over time.
    * Word clouds to visually represent common themes or issues mentioned in customer feedback.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer feedback scores can lead to decreased customer retention and negative word-of-mouth.
    * Consistently negative feedback may indicate systemic issues in the sales process that need to be addressed.
    """,
    tracking_tools="""
    * Customer feedback management platforms like Medallia or Qualtrics to collect and analyze feedback data.
    * CRM systems with built-in feedback tracking and reporting capabilities.
    """,
    integration_points="""
    * Integrate customer feedback data with sales performance metrics to understand the impact on overall sales effectiveness.
    * Link customer feedback with employee performance evaluations to align incentives with customer satisfaction goals.
    """,
    change_impact_analysis="""
    * Improving customer feedback can lead to increased customer retention and higher lifetime value.
    * Conversely, consistently low feedback scores can impact brand reputation and market competitiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Competitive Analysis", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Loyalty Program", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
