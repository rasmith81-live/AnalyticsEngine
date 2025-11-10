"""
Sales Retention Rate KPI

The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction.
"""

from analytics_models import KPI

SALES_RETENTION_RATE = KPI(
    name="Sales Retention Rate",
    code="SALES_RETENTION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction.",
    kpi_definition="The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction.",
    expected_business_insights="Reflects employee satisfaction, effectiveness of talent management, and potential impact on customer relationships.",
    measurement_approach="Measures the percentage of sales reps who remain with the company over a specific period of time.",
    
    # Formula
    formula="(Number of Sales Reps Remaining / Total Number of Sales Reps at Start of Period) * 100",
    calculation_formula="(Number of Sales Reps Remaining / Total Number of Sales Reps at Start of Period) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing sales retention rate may indicate improved job satisfaction and effectiveness of sales enablement efforts.
    * Decreasing retention rate could signal dissatisfaction with sales enablement support or changes in the company culture.
    """,
    diagnostic_questions="""
    * What specific aspects of the sales enablement program are positively impacting sales representative retention?
    * Are there any common reasons or patterns behind the departure of sales representatives?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from sales representatives to understand their needs and challenges.
    * Provide ongoing training and development opportunities to keep sales representatives engaged and motivated.
    * Implement recognition and reward programs to acknowledge the contributions of sales representatives.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales retention rate over time.
    * Comparison charts to analyze retention rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low sales retention rates can lead to increased recruitment and training costs.
    * High turnover may negatively impact team morale and overall sales performance.
    """,
    tracking_tools="""
    * Employee engagement and feedback platforms to gather insights from sales representatives.
    * HR analytics software to track and analyze retention data.
    """,
    integration_points="""
    * Integrate sales retention data with performance management systems to identify correlations between retention and sales performance.
    * Link retention data with training and development programs to tailor support based on retention trends.
    """,
    change_impact_analysis="""
    * Improving sales retention can lead to a more experienced and knowledgeable sales team, potentially impacting overall sales performance positively.
    * Conversely, high turnover rates can disrupt team dynamics and affect customer relationships, leading to potential revenue loss.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
