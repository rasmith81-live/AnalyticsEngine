"""
Sales Rep Content Contribution Rate KPI

The percentage of sales content that is contributed by sales representatives, encouraging involvement and tailored content.
"""

from analytics_models import KPI

SALES_REP_CONTENT_CONTRIBUTION_RATE = KPI(
    name="Sales Rep Content Contribution Rate",
    code="SALES_REP_CONTENT_CONTRIBUTION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales content that is contributed by sales representatives, encouraging involvement and tailored content.",
    kpi_definition="The percentage of sales content that is contributed by sales representatives, encouraging involvement and tailored content.",
    expected_business_insights="Encourages a collaborative culture and leverages frontline insights for content creation.",
    measurement_approach="Tracks the frequency with which sales reps contribute content or insights to the sales enablement resources.",
    
    # Formula
    formula="(Number of Rep Contributions / Total Number of Sales Reps) * 100",
    calculation_formula="(Number of Rep Contributions / Total Number of Sales Reps) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales rep content contribution rate may indicate a more engaged sales team and better alignment with customer needs.
    * A decreasing rate could signal disengagement or a lack of focus on creating tailored content for specific customer segments.
    """,
    diagnostic_questions="""
    * Are there specific sales reps consistently contributing high-quality content, and if so, what can be learned from their approach?
    * How does the content contributed by sales reps align with the overall sales strategy and customer preferences?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide training and resources to help sales reps understand the types of content that resonate with different customer personas.
    * Implement a content review process to ensure that contributed materials meet quality standards and align with the sales strategy.
    * Encourage collaboration between sales and marketing teams to develop content that addresses specific customer pain points and objections.
    """,
    visualization_suggestions="""
    * Line charts showing the contribution rate over time for individual sales reps or teams.
    * Pie charts illustrating the distribution of content contributions by sales reps across different customer segments or product lines.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low sales rep content contribution rate may result in generic, less effective sales materials that do not resonate with customers.
    * Over-reliance on a few sales reps for content contribution can lead to burnout and uneven distribution of workload.
    """,
    tracking_tools="""
    * Content management systems like HubSpot or Salesforce to track and analyze the content contributed by sales reps.
    * Sales enablement platforms that provide templates and guidance for creating tailored content based on customer insights.
    """,
    integration_points="""
    * Integrate the sales rep content contribution rate with customer relationship management (CRM) systems to understand how content impacts customer interactions and conversions.
    * Linking content contribution with sales performance metrics to assess the effectiveness of tailored content in driving revenue.
    """,
    change_impact_analysis="""
    * Improving the sales rep content contribution rate can lead to more personalized and effective sales interactions, potentially increasing conversion rates and customer satisfaction.
    * Conversely, a low contribution rate may result in missed opportunities to address customer needs and differentiate from competitors, impacting overall sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
