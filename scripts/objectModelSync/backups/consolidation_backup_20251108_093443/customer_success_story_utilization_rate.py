"""
Customer Success Story Utilization Rate KPI

The rate at which customer success stories and case studies are used in the sales process.
"""

from analytics_models import KPI

CUSTOMER_SUCCESS_STORY_UTILIZATION_RATE = KPI(
    name="Customer Success Story Utilization Rate",
    code="CUSTOMER_SUCCESS_STORY_UTILIZATION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The rate at which customer success stories and case studies are used in the sales process.",
    kpi_definition="The rate at which customer success stories and case studies are used in the sales process.",
    expected_business_insights="Provides insight into the impact of customer testimonials on the sales process and helps to build trust with prospects.",
    measurement_approach="Tracks the frequency of customer success stories used in sales engagements.",
    
    # Formula
    formula="(Number of Times Success Stories are Used / Total Number of Sales Engagements) * 100",
    calculation_formula="(Number of Times Success Stories are Used / Total Number of Sales Engagements) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer success story utilization rate may indicate a more effective sales process and better alignment with customer needs.
    * A decreasing rate could signal a lack of relevant success stories or a disconnect between the sales team and customer needs.
    """,
    diagnostic_questions="""
    * Are the customer success stories being used at the right stages of the sales process?
    * Are the success stories resonating with the target audience, or do they need to be tailored to different buyer personas?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train the sales team on how to effectively incorporate customer success stories into their pitches and presentations.
    * Create a library of success stories that cover a wide range of industries and use cases to ensure relevance to different prospects.
    * Solicit feedback from the sales team and customers to continuously improve the quality and impact of the success stories.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of success story utilization over time.
    * Pie charts to illustrate the distribution of success story usage across different customer segments or product lines.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low utilization rate may indicate a disconnect between the sales team and the value proposition of the product or service.
    * Over-reliance on a few success stories may lead to a lack of variety and relevance for different prospects.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with built-in capabilities for tracking the usage of customer success stories.
    * Content management systems to organize and categorize success stories for easy access by the sales team.
    """,
    integration_points="""
    * Integrate success story utilization data with sales performance metrics to understand the impact of using these stories on closing deals.
    * Link success story usage with customer feedback and satisfaction scores to gauge the effectiveness of the stories in influencing purchase decisions.
    """,
    change_impact_analysis="""
    * Improving the utilization rate can lead to higher conversion rates and increased customer satisfaction, ultimately impacting revenue and customer retention.
    * On the other hand, a low utilization rate may indicate missed opportunities and a need for reevaluation of the sales strategy and messaging.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
