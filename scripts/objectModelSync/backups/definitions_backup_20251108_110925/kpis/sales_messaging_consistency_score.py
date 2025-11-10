"""
Sales Messaging Consistency Score KPI

A measure of how consistent the sales messaging is across different sales representatives and content.
"""

from analytics_models import KPI

SALES_MESSAGING_CONSISTENCY_SCORE = KPI(
    name="Sales Messaging Consistency Score",
    code="SALES_MESSAGING_CONSISTENCY_SCORE",
    category="Sales Enablement",
    
    # Core Definition
    description="A measure of how consistent the sales messaging is across different sales representatives and content.",
    kpi_definition="A measure of how consistent the sales messaging is across different sales representatives and content.",
    expected_business_insights="Reflects the alignment of sales communications with brand messaging, potentially impacting customer perception.",
    measurement_approach="Evaluates how consistently sales messaging is conveyed across different sales reps and channels.",
    
    # Formula
    formula="Average Score on Consistency Assessments",
    calculation_formula="Average Score on Consistency Assessments",
    
    # Analysis
    trend_analysis="""
    * Consistent messaging may initially show a positive trend, but if it remains stagnant, it could indicate a lack of innovation or adaptation to changing market needs.
    * A decreasing consistency score may suggest a need for better training or clearer communication of sales messaging standards.
    """,
    diagnostic_questions="""
    * Are there specific sales reps or regions that consistently deviate from the standard messaging?
    * How do customer feedback and conversion rates correlate with messaging consistency?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update sales messaging guidelines to reflect market changes and customer feedback.
    * Provide ongoing training and coaching to ensure all sales reps understand and can effectively deliver the approved messaging.
    * Utilize sales enablement platforms to centralize and distribute approved messaging content to all reps.
    """,
    visualization_suggestions="""
    * Line charts showing the consistency score over time for each sales rep or region.
    * Comparison charts to visually represent the variance in messaging consistency across different content types or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Inconsistent messaging can lead to confusion and mistrust among potential customers.
    * Failure to address messaging inconsistencies may result in missed sales opportunities and decreased revenue.
    """,
    tracking_tools="""
    * Sales enablement platforms with content management and tracking capabilities, such as Highspot or Seismic.
    * CRM systems that allow for tracking and analysis of customer interactions and messaging effectiveness.
    """,
    integration_points="""
    * Integrate messaging consistency data with performance metrics to assess the impact on sales results.
    * Link messaging consistency with customer feedback systems to understand the correlation between messaging and customer satisfaction.
    """,
    change_impact_analysis="""
    * Improving messaging consistency can lead to increased customer trust and loyalty, ultimately impacting long-term revenue and market share.
    * However, overly rigid messaging standards may stifle creativity and personalization, potentially affecting customer engagement.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
