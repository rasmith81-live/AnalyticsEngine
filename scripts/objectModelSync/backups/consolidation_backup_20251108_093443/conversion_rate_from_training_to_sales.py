"""
Conversion Rate from Training to Sales KPI

The percentage of sales reps who complete training and coaching and go on to achieve sales targets. A higher conversion rate indicates effective training and coaching.
"""

from analytics_models import KPI

CONVERSION_RATE_FROM_TRAINING_TO_SALES = KPI(
    name="Conversion Rate from Training to Sales",
    code="CONVERSION_RATE_FROM_TRAINING_TO_SALES",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage of sales reps who complete training and coaching and go on to achieve sales targets. A higher conversion rate indicates effective training and coaching.",
    kpi_definition="The percentage of sales reps who complete training and coaching and go on to achieve sales targets. A higher conversion rate indicates effective training and coaching.",
    expected_business_insights="Indicates the direct impact of training on sales performance and can inform the ROI of sales training initiatives.",
    measurement_approach="The percentage of sales reps who successfully apply training to close deals or generate revenue.",
    
    # Formula
    formula="(Number of Sales Made by Trained Reps / Number of Trained Reps) * 100",
    calculation_formula="(Number of Sales Made by Trained Reps / Number of Trained Reps) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising conversion rate may indicate the effectiveness of new training and coaching methods.
    * A decreasing rate could signal a need for reevaluation of the training content or coaching techniques.
    """,
    diagnostic_questions="""
    * Are there specific areas of the training program where sales reps tend to struggle?
    * How does the conversion rate compare with industry benchmarks or with the performance of top-performing sales reps?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide personalized coaching and mentoring for sales reps who are struggling to meet targets.
    * Regularly update training materials to ensure they reflect the latest sales techniques and product knowledge.
    * Implement a peer-to-peer learning program where successful sales reps can share their strategies with others.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of conversion rates over time.
    * Comparison bar charts to visualize the performance of different sales reps or teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining conversion rate may lead to missed sales targets and revenue loss.
    * Consistently low conversion rates could indicate a need for a complete overhaul of the training and coaching program.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track the performance of individual sales reps and identify areas for improvement.
    * Learning management systems (LMS) to deliver and track the completion of training modules.
    """,
    integration_points="""
    * Integrate with performance management systems to align training and coaching efforts with individual sales goals.
    * Link with sales forecasting tools to understand the impact of training and coaching on future sales projections.
    """,
    change_impact_analysis="""
    * Improving the conversion rate can lead to increased revenue and higher overall sales team performance.
    * Conversely, a declining conversion rate may indicate a need for a reevaluation of the entire sales management process.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Lead", "Opportunity", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
