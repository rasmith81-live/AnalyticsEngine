"""
Sales Training ROI KPI

The return on investment for sales training, assessing the effectiveness of training programs in improving sales performance.
"""

from analytics_models import KPI

SALES_TRAINING_ROI = KPI(
    name="Sales Training ROI",
    code="SALES_TRAINING_ROI",
    category="Outside Sales",
    
    # Core Definition
    description="The return on investment for sales training, assessing the effectiveness of training programs in improving sales performance.",
    kpi_definition="The return on investment for sales training, assessing the effectiveness of training programs in improving sales performance.",
    expected_business_insights="Evaluates the effectiveness of sales training programs and their impact on sales performance.",
    measurement_approach="Calculates the return on investment for sales training by comparing the increase in sales to the cost of training.",
    
    # Formula
    formula="(Increase in Sales Revenue - Cost of Training) / Cost of Training * 100",
    calculation_formula="(Increase in Sales Revenue - Cost of Training) / Cost of Training * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales training ROI may indicate the effectiveness of new training programs or improved adoption of training by the sales team.
    * A decreasing ROI could signal a need to reassess the training content or delivery methods, as well as potential issues with sales team engagement.
    """,
    diagnostic_questions="""
    * Are there specific sales training programs or modules that are consistently rated as more effective by the sales team?
    * How does the sales training ROI compare with industry benchmarks or with the performance of top-performing sales teams?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from the sales team to identify areas for improvement in the training programs.
    * Customize training content to address specific sales challenges or market conditions that the team is facing.
    * Invest in coaching and mentorship programs to reinforce and apply the knowledge gained from sales training.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales training ROI over time.
    * Comparison charts to visualize the ROI of different training programs or initiatives.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low sales training ROI may lead to decreased sales performance and missed revenue targets.
    * An inconsistent or declining ROI could indicate a need for a more strategic approach to sales training and development.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track participation and engagement with training materials.
    * Sales performance analytics tools to correlate training effectiveness with actual sales results.
    """,
    integration_points="""
    * Integrate sales training ROI data with individual sales performance metrics to identify correlations and opportunities for targeted training interventions.
    * Link training ROI with customer satisfaction and retention metrics to understand the impact of training on customer relationships.
    """,
    change_impact_analysis="""
    * Improving sales training ROI can lead to increased sales productivity and revenue generation.
    * Conversely, a declining ROI may result in decreased motivation and confidence among the sales team, impacting overall sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
