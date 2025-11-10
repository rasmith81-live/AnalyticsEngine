"""
Customer Feedback Incorporation Rate KPI

The rate at which customer feedback is incorporated into sales strategies and content creation.
"""

from analytics_models import KPI

CUSTOMER_FEEDBACK_INCORPORATION_RATE = KPI(
    name="Customer Feedback Incorporation Rate",
    code="CUSTOMER_FEEDBACK_INCORPORATION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The rate at which customer feedback is incorporated into sales strategies and content creation.",
    kpi_definition="The rate at which customer feedback is incorporated into sales strategies and content creation.",
    expected_business_insights="Highlights the company\'s responsiveness to customer needs and its commitment to continuous improvement.",
    measurement_approach="Measures how quickly and effectively customer feedback is integrated into the product or service development.",
    
    # Formula
    formula="(Number of Implemented Customer Feedback Items / Total Number of Feedback Items Received) * 100",
    calculation_formula="(Number of Implemented Customer Feedback Items / Total Number of Feedback Items Received) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer feedback incorporation rate may indicate a more customer-centric approach to sales strategies and content creation.
    * A decreasing rate could signal a disconnect between customer feedback and the sales team, leading to potential missed opportunities.
    """,
    diagnostic_questions="""
    * How frequently are sales strategies and content updated based on customer feedback?
    * Are there specific channels or touchpoints where customer feedback is underutilized in the sales process?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular feedback review sessions with the sales team to ensure customer insights are being incorporated into strategies.
    * Utilize customer relationship management (CRM) tools to track and analyze customer feedback for actionable insights.
    * Create a feedback loop between the sales team and customer support to ensure all feedback is considered in sales strategies.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer feedback incorporation rate over time.
    * Word clouds to visually represent the most common themes or topics in customer feedback that are being incorporated into sales strategies.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low customer feedback incorporation rate may lead to missed opportunities and decreased customer satisfaction.
    * An inconsistent incorporation rate could result in disjointed sales strategies that do not align with customer needs.
    """,
    tracking_tools="""
    * Utilize survey and feedback collection tools such as SurveyMonkey or Qualtrics to gather and organize customer feedback.
    * Implement sales enablement platforms like Seismic or Highspot to centralize customer insights and content creation.
    """,
    integration_points="""
    * Integrate customer feedback data with sales performance metrics to identify correlations between feedback incorporation and sales success.
    * Link customer feedback systems with content management platforms to streamline the process of incorporating feedback into sales materials.
    """,
    change_impact_analysis="""
    * Improving the customer feedback incorporation rate can lead to more targeted and effective sales strategies, potentially increasing conversion rates.
    * However, a lack of alignment between customer feedback and sales content could result in wasted resources and missed revenue opportunities.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Enablement Feedback", "Enablement Platform", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
