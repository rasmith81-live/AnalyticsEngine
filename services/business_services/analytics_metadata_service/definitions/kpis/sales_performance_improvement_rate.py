"""
Sales Performance Improvement Rate KPI

The percentage of sales reps who have shown improvement in their sales performance after receiving training and support from the sales enablement team.
"""

from analytics_models import KPI

SALES_PERFORMANCE_IMPROVEMENT_RATE = KPI(
    name="Sales Performance Improvement Rate",
    code="SALES_PERFORMANCE_IMPROVEMENT_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales reps who have shown improvement in their sales performance after receiving training and support from the sales enablement team.",
    kpi_definition="The percentage of sales reps who have shown improvement in their sales performance after receiving training and support from the sales enablement team.",
    expected_business_insights="Shows the progress of the sales team\'s abilities and the impact of training and development initiatives.",
    measurement_approach="Measures the rate of improvement in sales performance metrics over time.",
    
    # Formula
    formula="(Current Sales Performance - Previous Sales Performance) / Previous Sales Performance",
    calculation_formula="(Current Sales Performance - Previous Sales Performance) / Previous Sales Performance",
    
    # Analysis
    trend_analysis="""
    * Increasing sales performance improvement rate may indicate the effectiveness of the sales enablement team\'s training and support programs.
    * Decreasing rate could signal a need for reassessment of training methods or changes in market conditions affecting sales performance.
    """,
    diagnostic_questions="""
    * Are there specific sales techniques or product knowledge areas where sales reps consistently struggle?
    * How does the sales performance improvement rate correlate with changes in the sales process or product offerings?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing coaching and mentoring to reinforce training and support initiatives.
    * Implement regular performance assessments to identify areas for improvement and tailor training accordingly.
    * Utilize sales enablement technologies to provide real-time support and resources to sales reps.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales performance improvement rate over time.
    * Comparison bar charts displaying improvement rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low sales performance improvement rates may lead to missed revenue targets and decreased motivation among sales reps.
    * Consistently high improvement rates without corresponding sales growth could indicate a need for more challenging performance targets.
    """,
    tracking_tools="""
    * Sales performance management software to track individual rep performance and improvement over time.
    * Learning management systems for delivering and monitoring the effectiveness of training programs.
    """,
    integration_points="""
    * Integrate sales performance improvement data with CRM systems to analyze the impact on customer acquisition and retention.
    * Link improvement rates with sales forecasting tools to align training efforts with anticipated market demands.
    """,
    change_impact_analysis="""
    * Improving sales performance can lead to increased revenue and customer satisfaction, but may also require additional resources for training and support.
    * Conversely, a decline in improvement rates could affect overall sales team morale and retention.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Training Program"]
    }
)
