"""
Appointment-to-Demo Ratio KPI

The ratio of sales appointments to the number of product or service demos given.
"""

from analytics_models import KPI

APPOINTMENT_TO_DEMO_RATIO = KPI(
    name="Appointment-to-Demo Ratio",
    code="APPOINTMENT_TO_DEMO_RATIO",
    category="Outside Sales",
    
    # Core Definition
    description="The ratio of sales appointments to the number of product or service demos given.",
    kpi_definition="The ratio of sales appointments to the number of product or service demos given.",
    expected_business_insights="Indicates the effectiveness of the appointment setting process and sales team’s ability to advance leads in the sales funnel.",
    measurement_approach="Compares the number of appointments scheduled to the number of product demonstrations conducted.",
    
    # Formula
    formula="Number of Demos Conducted / Number of Appointments Scheduled * 100",
    calculation_formula="Number of Demos Conducted / Number of Appointments Scheduled * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing appointment-to-demo ratio may indicate a lack of qualified leads or ineffective sales prospecting.
    * A decreasing ratio could signal improved lead quality or more efficient sales processes.
    """,
    diagnostic_questions="""
    * Are there specific sales channels or sources that consistently lead to higher appointment-to-demo ratios?
    * How does our appointment-to-demo ratio compare with industry benchmarks or with different sales teams within the organization?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement lead scoring to prioritize high-quality leads for appointments.
    * Provide additional sales training to improve the effectiveness of product or service demos.
    * Regularly review and refine the sales prospecting process to attract more qualified leads.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of appointment-to-demo ratios over time.
    * Comparison bar charts to visualize the appointment-to-demo ratios across different sales channels or teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low appointment-to-demo ratio may lead to wasted resources and inefficiencies in the sales process.
    * A high ratio may indicate a lack of proactive sales prospecting and lead generation.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze lead sources and appointment outcomes.
    * Sales enablement platforms to streamline the demo process and provide sales reps with the necessary tools and materials.
    """,
    integration_points="""
    * Integrate appointment-to-demo ratio tracking with marketing automation systems to align lead generation efforts with sales activities.
    * Link with customer feedback systems to gather insights on the quality of demos and potential areas for improvement.
    """,
    change_impact_analysis="""
    * Improving the appointment-to-demo ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant increase in the ratio may also indicate a need for more aggressive lead generation efforts to maintain a healthy pipeline.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Appointment", "Demo", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
