"""
Training Cost Per Employee KPI

The average cost incurred by the company for training each sales representative.
"""

from analytics_models import KPI

TRAINING_COST_PER_EMPLOYEE = KPI(
    name="Training Cost Per Employee",
    code="TRAINING_COST_PER_EMPLOYEE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The average cost incurred by the company for training each sales representative.",
    kpi_definition="The average cost incurred by the company for training each sales representative.",
    expected_business_insights="Helps in budgeting and assessing the financial investment in sales rep training, relative to the number of participants.",
    measurement_approach="The average cost of providing training to each sales representative.",
    
    # Formula
    formula="Total Training Costs / Number of Sales Reps Trained",
    calculation_formula="Total Training Costs / Number of Sales Reps Trained",
    
    # Analysis
    trend_analysis="""
    * Training cost per employee may increase over time due to inflation, higher demand for specialized training, or the need for more advanced training materials.
    * A decreasing trend could indicate more cost-effective training methods, improved training efficiency, or a reduction in the need for external training resources.
    """,
    diagnostic_questions="""
    * Are there specific training programs or materials that are driving up the cost per employee?
    * How does the cost per employee compare with industry benchmarks or with the performance of top-performing sales representatives?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in digital training resources and e-learning platforms to reduce the cost of physical training materials and external trainers.
    * Implement mentorship programs to provide on-the-job training at a lower cost.
    * Regularly review and update training programs to ensure they remain relevant and cost-effective.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of training cost per employee over time.
    * Comparison bar charts to visualize the cost per employee for different training programs or sales teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High training costs per employee may impact the company\'s overall profitability and competitiveness.
    * Excessive training costs without a corresponding increase in sales performance could indicate inefficiencies in the training process.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and manage training costs and materials.
    * Cost analysis software to identify areas of high training costs and potential cost-saving opportunities.
    """,
    integration_points="""
    * Integrate training cost data with sales performance metrics to assess the effectiveness of training programs.
    * Link training cost information with HR systems to analyze the impact of training on employee retention and performance.
    """,
    change_impact_analysis="""
    * Reducing training costs may lead to lower overall expenses, but could also impact the quality and effectiveness of training programs.
    * Increased training costs may indicate a strategic investment in developing a highly skilled sales force, potentially leading to improved sales performance in the long run.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
