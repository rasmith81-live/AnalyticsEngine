"""
Meeting Conversion Rate KPI

The percentage of sales meetings that result in a follow-up action or sale.
"""

from analytics_models import KPI

MEETING_CONVERSION_RATE = KPI(
    name="Meeting Conversion Rate",
    code="MEETING_CONVERSION_RATE",
    category="Outside Sales",
    
    # Core Definition
    description="The percentage of sales meetings that result in a follow-up action or sale.",
    kpi_definition="The percentage of sales meetings that result in a follow-up action or sale.",
    expected_business_insights="Indicates the effectiveness of sales presentations and the proficiency of sales representatives in advancing the sales process.",
    measurement_approach="Measures the percentage of sales meetings that result in a further action or sale.",
    
    # Formula
    formula="(Number of Successful Meetings / Total Number of Meetings) * 100",
    calculation_formula="(Number of Successful Meetings / Total Number of Meetings) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing meeting conversion rate may indicate improved sales strategies or a higher quality of leads being pursued.
    * A decreasing rate could signal issues with the sales process, product offering, or market demand.
    """,
    diagnostic_questions="""
    * Are there specific sales representatives or territories with consistently higher or lower meeting conversion rates?
    * How does our meeting conversion rate compare with industry benchmarks or historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and support for representatives with lower meeting conversion rates.
    * Regularly review and refine the sales process to identify and address any bottlenecks or inefficiencies.
    * Focus on targeting high-quality leads and prospects to improve the likelihood of successful meetings.
    """,
    visualization_suggestions="""
    * Line charts to track the meeting conversion rate over time and identify any significant fluctuations.
    * Pie charts to compare meeting conversion rates across different sales representatives or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low meeting conversion rate can lead to wasted resources and decreased sales effectiveness.
    * An excessively high rate may indicate a lack of qualification in the sales process, leading to potential customer dissatisfaction.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze meeting outcomes and follow-up actions.
    * Sales enablement platforms to provide sales representatives with the necessary tools and resources to improve meeting effectiveness.
    """,
    integration_points="""
    * Integrate meeting conversion rate data with lead generation and marketing systems to better understand the quality of leads being generated.
    * Link meeting conversion rate with customer relationship management systems to track the impact of meetings on overall customer engagement and satisfaction.
    """,
    change_impact_analysis="""
    * An improved meeting conversion rate can lead to increased sales revenue and customer acquisition, but may also require additional resources for managing the increased workload.
    * Conversely, a declining rate can impact overall sales performance and the ability to meet revenue targets, affecting the organization\'s financial health.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lead", "Lost Sale", "Meeting", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
