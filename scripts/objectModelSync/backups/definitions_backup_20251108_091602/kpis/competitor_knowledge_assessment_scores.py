"""
Competitor Knowledge Assessment Scores KPI

The scores achieved by sales representatives on assessments regarding competitors' offerings and strategies.
"""

from analytics_models import KPI

COMPETITOR_KNOWLEDGE_ASSESSMENT_SCORES = KPI(
    name="Competitor Knowledge Assessment Scores",
    code="COMPETITOR_KNOWLEDGE_ASSESSMENT_SCORES",
    category="Sales Enablement",
    
    # Core Definition
    description="The scores achieved by sales representatives on assessments regarding competitors\' offerings and strategies.",
    kpi_definition="The scores achieved by sales representatives on assessments regarding competitors\' offerings and strategies.",
    expected_business_insights="Helps determine the preparedness of the sales team to effectively compete and devise strategies to win over competitors.",
    measurement_approach="Assesses sales team\'s understanding of competitor products, strategies, and market positioning.",
    
    # Formula
    formula="Average Score on Competitor Knowledge Assessments",
    calculation_formula="Average Score on Competitor Knowledge Assessments",
    
    # Analysis
    trend_analysis="""
    * Increasing competitor knowledge assessment scores may indicate improved training programs or a deeper understanding of the market.
    * Decreasing scores could signal a lack of focus on competitive intelligence or a shift in the competitive landscape that is not being addressed.
    """,
    diagnostic_questions="""
    * Are there specific competitors or product segments where our sales representatives consistently score lower?
    * How do our competitor knowledge assessment scores compare with industry benchmarks or with our own historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide regular updates on competitor strategies and offerings through internal communications or training sessions.
    * Encourage sales representatives to actively engage with industry news, attend conferences, and participate in webinars to stay updated on competitors.
    * Implement gamification or rewards for sales reps who demonstrate strong competitor knowledge in their sales pitches or interactions.
    """,
    visualization_suggestions="""
    * Radar charts comparing sales representatives\' scores on different aspects of competitor knowledge.
    * Line graphs showing the trend of average competitor knowledge assessment scores over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low competitor knowledge assessment scores may result in ineffective sales strategies and missed opportunities.
    * Overemphasis on competitor knowledge without a focus on product knowledge or customer needs can lead to a misalignment in sales approaches.
    """,
    tracking_tools="""
    * Competitor tracking software like Crayon or Kompyte to monitor and analyze competitors\' offerings and strategies.
    * Sales enablement platforms with built-in competitor intelligence modules to integrate competitor knowledge assessment with sales processes.
    """,
    integration_points="""
    * Integrate competitor knowledge assessment scores with performance management systems to align training and coaching efforts with individual sales representatives\' needs.
    * Link competitor knowledge assessment with CRM systems to provide sales reps with real-time competitor insights during customer interactions.
    """,
    change_impact_analysis="""
    * Improving competitor knowledge assessment scores can lead to more effective sales pitches, better objection handling, and increased win rates.
    * However, a singular focus on competitor knowledge may lead to neglect of other critical sales skills and customer-centric approaches.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Knowledge Base", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
