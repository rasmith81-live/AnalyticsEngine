"""
Sales Training Completion Rate KPI

Module: Business Development
"""

from analytics_models import KPI

SALES_TRAINING_COMPLETION_RATE = KPI(
    name="Sales Training Completion Rate",
    code="SALES_TRAINING_COMPLETION_RATE",
    description="The percentage of sales representatives who have completed mandatory sales training programs.",
    
    # Definition & Context
    kpi_definition="The percentage of sales representatives who have completed mandatory sales training programs.",
    expected_business_insights="Reveals the commitment to professional development and the potential for improved sales performance.",
    measurement_approach="Measures the percentage of sales representatives who complete mandatory sales training programs.",
    
    # Calculation
    formula="(Number of Sales Reps Who Completed Training / Total Number of Sales Reps) * 100",
    
    # Analysis
    trend_analysis="A rising sales training completion rate may indicate increased engagement and commitment from the sales team. A decreasing rate could signal a need for reevaluation of the training content or delivery methods.",
    diagnostic_questions=['Are there specific training modules that have lower completion rates, and if so, what might be the reasons for this?', 'How does the completion rate correlate with sales performance and customer satisfaction metrics?'],
    actionable_steps={
        "operational": ['Regularly review and update training content to ensure it remains relevant and engaging for the sales team.'],
        "strategic": ['Provide incentives or recognition for sales representatives who consistently complete training on time.', 'Offer flexible training options to accommodate different learning styles and schedules.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the completion rate over time to identify any patterns or fluctuations.', 'Comparison bar charts to visualize completion rates across different sales teams or regions.']
    ],
    risk_warnings=['Low completion rates may lead to gaps in knowledge and skills, impacting sales performance and customer interactions.', 'High completion rates without corresponding improvements in sales metrics may indicate ineffective or irrelevant training content.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Learning management systems (LMS) to track and manage sales training programs efficiently.', 'Survey and feedback tools to gather input from sales representatives on the effectiveness of the training.'],
    integration_points=['Integrate completion rate data with sales performance metrics to analyze the impact of training on actual results.', 'Link training completion with individual performance reviews and development plans for sales representatives.'],
    
    # Impact
    change_impact="Improving the completion rate can lead to better-equipped sales teams and potentially higher sales effectiveness. However, a high completion rate alone does not guarantee improved sales performance, so it's important to assess the actual impact of the training.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "SALES_ENABLEMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Partner Training", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
