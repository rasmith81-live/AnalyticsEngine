"""
Partner Sales Training Efficacy KPI

A measure of how effective sales training provided to partners is in improving their performance.
"""

from analytics_models import KPI

PARTNER_SALES_TRAINING_EFFICACY = KPI(
    name="Partner Sales Training Efficacy",
    code="PARTNER_SALES_TRAINING_EFFICACY",
    category="Channel Sales",
    
    # Core Definition
    description="A measure of how effective sales training provided to partners is in improving their performance.",
    kpi_definition="A measure of how effective sales training provided to partners is in improving their performance.",
    expected_business_insights="Measures the return on investment in partner training and informs future training initiatives.",
    measurement_approach="Evaluates the impact of sales training on partners’ sales performance.",
    
    # Formula
    formula="Percentage Increase in Sales Post-Training vs. Pre-Training",
    calculation_formula="Percentage Increase in Sales Post-Training vs. Pre-Training",
    
    # Analysis
    trend_analysis="""
    * An increasing efficacy in partner sales training may indicate improved sales performance and increased revenue from partner channels.
    * A decreasing efficacy could signal a need for reevaluation of the training content and methods, as well as potential impact on partner relationships and sales outcomes.
    """,
    diagnostic_questions="""
    * Are there specific areas or topics in the sales training that partners struggle with the most?
    * How do partners perceive the effectiveness of the sales training they receive, and what feedback do they provide?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from partners to understand which aspects of the training are most beneficial and which need improvement.
    * Customize sales training content to align with the unique needs and challenges of different partner organizations.
    * Provide ongoing support and resources to reinforce and apply the training concepts in real-world sales scenarios.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of partner sales performance alongside the efficacy of sales training over time.
    * Comparison bar charts displaying the performance of partners who have received different levels of sales training.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low efficacy in partner sales training may lead to missed sales opportunities and decreased partner satisfaction.
    * Failure to address training efficacy issues could result in disengagement from partners and a negative impact on overall channel sales performance.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to deliver, track, and assess the effectiveness of sales training content for partners.
    * Feedback and survey tools to gather insights from partners about the relevance and impact of the sales training they receive.
    """,
    integration_points="""
    * Integrate partner sales training efficacy data with sales performance metrics to understand the direct impact of training on revenue generation.
    * Link training efficacy with partner relationship management systems to identify correlations between training satisfaction and partner engagement.
    """,
    change_impact_analysis="""
    * Improving partner sales training efficacy can lead to increased partner loyalty, stronger sales relationships, and higher overall channel sales performance.
    * Conversely, a decline in training efficacy may result in decreased partner trust, reduced sales effectiveness, and potential loss of market share within partner channels.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
