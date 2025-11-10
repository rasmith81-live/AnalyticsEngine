"""
Competency Improvement Rate KPI

The rate at which sales reps improve their competencies and skills through training.
"""

from analytics_models import KPI

COMPETENCY_IMPROVEMENT_RATE = KPI(
    name="Competency Improvement Rate",
    code="COMPETENCY_IMPROVEMENT_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The rate at which sales reps improve their competencies and skills through training.",
    kpi_definition="The rate at which sales reps improve their competencies and skills through training.",
    expected_business_insights="Highlights the effectiveness of training in enhancing the skills and abilities necessary for sales success.",
    measurement_approach="The rate at which sales reps show improvements in competencies identified as crucial for their role post-training.",
    
    # Formula
    formula="(Number of Competencies Improved Post-Training / Total Number of Competencies Targeted) * 100",
    calculation_formula="(Number of Competencies Improved Post-Training / Total Number of Competencies Targeted) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing competency improvement rate may indicate the effectiveness of training programs and coaching initiatives.
    * A decreasing rate could signal a need for reevaluation of training methods or a lack of engagement from sales reps.
    """,
    diagnostic_questions="""
    * Are there specific competencies or skills that sales reps struggle to improve?
    * How does the competency improvement rate align with the implementation of new training initiatives or coaching strategies?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide personalized coaching and training plans tailored to individual sales reps\' needs.
    * Implement regular feedback mechanisms to track progress and adjust training programs accordingly.
    * Encourage a culture of continuous learning and skill development within the sales team.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of competency improvement rate over time.
    * Comparison charts to visualize the competency improvement rate across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A stagnant or declining competency improvement rate may lead to decreased sales performance and missed opportunities.
    * An overly rapid improvement rate could indicate a lack of challenge or insufficient training depth.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and manage individual sales reps\' training progress.
    * Coaching and feedback platforms to facilitate ongoing communication between sales managers and reps.
    """,
    integration_points="""
    * Integrate competency improvement data with performance management systems to correlate skill development with sales outcomes.
    * Link training and coaching programs with customer relationship management (CRM) systems to align skill development with customer needs.
    """,
    change_impact_analysis="""
    * Improving competency improvement rate can lead to increased sales effectiveness and customer satisfaction.
    * However, rapid improvement without proper reinforcement may lead to short-term gains but long-term skill degradation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
