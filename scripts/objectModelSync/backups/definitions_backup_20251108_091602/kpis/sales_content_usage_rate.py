"""
Sales Content Usage Rate KPI

The usage rate of sales content created by the sales enablement team by sales reps, such as presentations, proposals, and case studies.
"""

from analytics_models import KPI

SALES_CONTENT_USAGE_RATE = KPI(
    name="Sales Content Usage Rate",
    code="SALES_CONTENT_USAGE_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The usage rate of sales content created by the sales enablement team by sales reps, such as presentations, proposals, and case studies.",
    kpi_definition="The usage rate of sales content created by the sales enablement team by sales reps, such as presentations, proposals, and case studies.",
    expected_business_insights="Indicates how integral the provided content is to the sales process and its alignment with sales needs.",
    measurement_approach="Assesses the frequency with which sales content is used by the sales team during their sales activities.",
    
    # Formula
    formula="(Number of Times Content is Used / Total Number of Sales Activities) * 100",
    calculation_formula="(Number of Times Content is Used / Total Number of Sales Activities) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales content usage rate may indicate better alignment between the content created and the needs of sales reps, resulting in more effective sales interactions.
    * A decreasing rate could signal a lack of relevance or accessibility of the content, leading to missed sales opportunities or ineffective customer engagements.
    """,
    diagnostic_questions="""
    * Are sales reps actively using the provided sales content, and if not, what barriers are preventing its usage?
    * How does the usage rate of different types of sales content vary, and what insights can be gained from this variation?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from sales reps to understand their content needs and preferences, and adjust content creation accordingly.
    * Ensure easy access to sales content through a centralized and user-friendly platform, and provide training on how to effectively utilize the available resources.
    * Monitor the performance of sales content in terms of conversion rates and customer feedback, and iterate on content creation based on these insights.
    """,
    visualization_suggestions="""
    * Line charts showing the usage rate of different types of sales content over time to identify trends and patterns.
    * Stacked bar charts comparing the overall usage rate of sales content across different sales teams or regions to pinpoint areas of high and low adoption.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low sales content usage rate may lead to inconsistent messaging and missed sales opportunities, impacting revenue and customer relationships.
    * An excessively high usage rate of certain content may indicate a lack of variety or customization, potentially leading to decreased effectiveness in engaging diverse customer segments.
    """,
    tracking_tools="""
    * Sales enablement platforms like Seismic or Highspot that provide analytics on content usage and performance.
    * Customer relationship management (CRM) systems with integrated content management capabilities to track content usage in the context of sales activities.
    """,
    integration_points="""
    * Integrate sales content usage data with sales performance metrics to understand the impact of content on sales outcomes and identify areas for improvement.
    * Link content usage with customer feedback and engagement data to assess the effectiveness of content in driving customer interactions and conversions.
    """,
    change_impact_analysis="""
    * An increase in sales content usage rate can lead to improved sales productivity and customer engagement, potentially driving revenue growth.
    * Conversely, a decrease in usage rate may result in missed sales opportunities and a negative impact on the overall effectiveness of the sales team.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product Usage", "Proposal", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
