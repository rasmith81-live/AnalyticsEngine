"""
Sales Call-to-Appointment Ratio KPI

The ratio of sales calls made to the number of appointments or follow-up meetings secured.
"""

from analytics_models import KPI

SALES_CALL_TO_APPOINTMENT_RATIO = KPI(
    name="Sales Call-to-Appointment Ratio",
    code="SALES_CALL_TO_APPOINTMENT_RATIO",
    category="Outside Sales",
    
    # Core Definition
    description="The ratio of sales calls made to the number of appointments or follow-up meetings secured.",
    kpi_definition="The ratio of sales calls made to the number of appointments or follow-up meetings secured.",
    expected_business_insights="Highlights the effectiveness of sales calls in progressing leads through the sales funnel and can pinpoint areas for training or process improvement.",
    measurement_approach="Measures the number of sales calls made against the number of appointments set.",
    
    # Formula
    formula="Number of Appointments Set / Total Number of Sales Calls Made * 100",
    calculation_formula="Number of Appointments Set / Total Number of Sales Calls Made * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales call-to-appointment ratio may indicate a more effective sales pitch or better targeting of potential clients.
    * A decreasing ratio could signal a decline in the quality of leads or a need for sales training and development.
    """,
    diagnostic_questions="""
    * Are there specific sales strategies or pitches that have led to a higher appointment ratio?
    * How does our appointment ratio compare with industry benchmarks or with different sales representatives?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide sales training to improve the quality of sales pitches and increase the likelihood of securing appointments.
    * Implement a lead scoring system to prioritize higher quality leads for follow-up.
    * Regularly review and update the sales pitch based on feedback and performance data.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of appointment ratios over time for different sales representatives or regions.
    * Pie charts to compare the distribution of secured appointments across different lead sources or industries.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low appointment ratio may lead to missed sales opportunities and revenue loss.
    * Consistently high ratios may indicate that sales representatives are being too selective and missing out on potential clients.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze sales call outcomes and appointment conversions.
    * Sales enablement platforms to provide sales representatives with the necessary tools and resources to improve their appointment conversion rates.
    """,
    integration_points="""
    * Integrate appointment ratio data with lead generation systems to identify which sources are providing the highest quality leads.
    * Link appointment ratio with customer relationship management systems to track the conversion of appointments into actual sales.
    """,
    change_impact_analysis="""
    * Improving the appointment ratio can lead to increased sales revenue and customer acquisition.
    * However, a focus solely on increasing the ratio may lead to a decline in the quality of appointments and potential long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Appointment", "Call", "Meeting", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
