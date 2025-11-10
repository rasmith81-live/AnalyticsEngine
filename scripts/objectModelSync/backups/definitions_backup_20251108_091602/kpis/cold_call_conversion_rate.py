"""
Cold Call Conversion Rate KPI

The percentage of cold calls that result in a successful action, such as a meeting scheduled or further interest expressed.
"""

from analytics_models import KPI

COLD_CALL_CONVERSION_RATE = KPI(
    name="Cold Call Conversion Rate",
    code="COLD_CALL_CONVERSION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of cold calls that result in a successful action, such as a meeting scheduled or further interest expressed.",
    kpi_definition="The percentage of cold calls that result in a successful action, such as a meeting scheduled or further interest expressed.",
    expected_business_insights="Helps assess the effectiveness of cold calling scripts and techniques, as well as the skill level of sales representatives.",
    measurement_approach="Measures the percentage of cold calls that result in a meaningful interaction or progress in the sales process.",
    
    # Formula
    formula="(Number of Successful Calls / Total Number of Cold Calls) * 100",
    calculation_formula="(Number of Successful Calls / Total Number of Cold Calls) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising cold call conversion rate may indicate improved targeting or messaging in the sales pitch.
    * A decreasing rate could signal market saturation or a decline in the effectiveness of the sales team\'s approach.
    """,
    diagnostic_questions="""
    * Are there specific industries or segments where the cold call conversion rate is consistently higher or lower?
    * How does the cold call conversion rate compare with industry benchmarks or historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide targeted training and resources to improve the quality of cold calls and increase conversion rates.
    * Implement a lead scoring system to prioritize cold call efforts on leads with higher potential for conversion.
    * Regularly review and update the cold call script and value proposition to align with customer needs and market trends.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of cold call conversion rates over time.
    * Pie charts comparing conversion rates across different sales representatives or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low cold call conversion rate can lead to demotivation and burnout among the sales team.
    * An excessively high conversion rate may indicate that the sales team is being too conservative in their outreach and missing potential opportunities.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software with built-in cold call tracking and analytics capabilities.
    * Sales engagement platforms that provide insights into call performance and enable A/B testing of different approaches.
    """,
    integration_points="""
    * Integrate cold call conversion data with lead generation and marketing automation systems to track the entire customer acquisition process.
    * Link conversion rates with sales performance metrics to identify correlations and optimize sales strategies.
    """,
    change_impact_analysis="""
    * Improving the cold call conversion rate can lead to increased sales revenue and customer acquisition efficiency.
    * However, a significant increase in conversion rate may require adjustments in sales resource allocation and capacity planning.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Enablement Feedback", "Enablement Platform", "Lead", "Meeting", "Opportunity", "Outbound Call", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
