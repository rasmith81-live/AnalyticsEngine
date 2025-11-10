"""
Sales Cycle Time Reduction Rate KPI

The rate of reduction in the average sales cycle time due to sales enablement efforts.
"""

from analytics_models import KPI

SALES_CYCLE_TIME_REDUCTION_RATE = KPI(
    name="Sales Cycle Time Reduction Rate",
    code="SALES_CYCLE_TIME_REDUCTION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The rate of reduction in the average sales cycle time due to sales enablement efforts.",
    kpi_definition="The rate of reduction in the average sales cycle time due to sales enablement efforts.",
    expected_business_insights="Reflects the effectiveness of sales strategies and tools in streamlining the sales process.",
    measurement_approach="Measures the change in the average length of the sales cycle over a period of time.",
    
    # Formula
    formula="(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    calculation_formula="(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    
    # Analysis
    trend_analysis="""
    * An increasing sales cycle time reduction rate may indicate inefficiencies in the sales process or a lack of alignment between sales and marketing efforts.
    * A decreasing rate can signal improved sales enablement strategies, better use of technology, or more effective training for sales teams.
    """,
    diagnostic_questions="""
    * Are there specific stages in the sales cycle where the reduction rate is slower or faster?
    * How do our sales cycle time reduction rate compare with industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement sales enablement tools and technologies to automate manual tasks and streamline the sales process.
    * Provide ongoing training and coaching for sales teams to improve their efficiency and effectiveness in closing deals.
    * Analyze customer feedback and sales data to identify bottlenecks in the sales cycle and address them proactively.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of sales cycle time reduction rate over time.
    * Funnel charts to visualize the conversion rates at each stage of the sales cycle.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A slow or stagnant reduction rate may lead to missed sales opportunities and decreased revenue.
    * Rapid reduction without proper analysis may result in overlooked quality or customer satisfaction issues.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track and analyze the sales cycle and customer interactions.
    * Sales enablement platforms to provide sales teams with the necessary content, training, and tools to close deals more effectively.
    """,
    integration_points="""
    * Integrate sales cycle time reduction rate with customer feedback systems to understand the impact of sales processes on customer satisfaction.
    * Link with marketing automation systems to ensure alignment between marketing efforts and the sales cycle.
    """,
    change_impact_analysis="""
    * Improving the sales cycle time reduction rate can lead to increased revenue and customer satisfaction, but it may also require investment in technology and training.
    * Conversely, a slow reduction rate can impact the overall sales performance and the ability to meet revenue targets.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
