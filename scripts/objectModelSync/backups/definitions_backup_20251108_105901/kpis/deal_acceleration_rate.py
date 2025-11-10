"""
Deal Acceleration Rate KPI

The rate at which sales enablement tools and strategies help to shorten the sales cycle for deals in the pipeline.
"""

from analytics_models import KPI

DEAL_ACCELERATION_RATE = KPI(
    name="Deal Acceleration Rate",
    code="DEAL_ACCELERATION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The rate at which sales enablement tools and strategies help to shorten the sales cycle for deals in the pipeline.",
    kpi_definition="The rate at which sales enablement tools and strategies help to shorten the sales cycle for deals in the pipeline.",
    expected_business_insights="Reflects the efficiency and effectiveness of sales processes and sales enablement tools in shortening the sales cycle.",
    measurement_approach="Evaluates the change in the average time taken to close deals after implementing sales enablement strategies.",
    
    # Formula
    formula="(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    calculation_formula="(Previous Average Sales Cycle Time - Current Average Sales Cycle Time) / Previous Average Sales Cycle Time",
    
    # Analysis
    trend_analysis="""
    * Increasing deal acceleration rate may indicate the effectiveness of new sales enablement tools or strategies.
    * A decreasing rate could signal a need for reevaluation of current sales enablement methods or a shift in customer behavior.
    """,
    diagnostic_questions="""
    * Are there specific stages in the sales cycle where deals tend to get stuck or delayed?
    * How do our deal acceleration rates compare with industry benchmarks or with competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide targeted training for sales teams on how to effectively use sales enablement tools to move deals forward.
    * Analyze customer feedback to identify potential pain points in the sales process and address them with relevant enablement resources.
    * Regularly review and update the sales enablement toolkit to ensure it aligns with the evolving needs of the sales team and customers.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of deal acceleration rates over time.
    * Funnel charts to visualize the progression of deals through different stages of the sales cycle.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low deal acceleration rate may lead to missed revenue targets and decreased sales team motivation.
    * A sudden spike in deal acceleration rate could indicate a potential issue with deal quality or customer satisfaction.
    """,
    tracking_tools="""
    * CRM systems with built-in sales enablement features to track the impact of enablement tools on deal acceleration.
    * Data analytics platforms to identify patterns and correlations between enablement strategies and deal acceleration rates.
    """,
    integration_points="""
    * Integrate deal acceleration rate tracking with performance management systems to align sales team incentives with the goal of shortening the sales cycle.
    * Link sales enablement platforms with customer relationship management systems to understand the impact of enablement tools on customer interactions and deal progression.
    """,
    change_impact_analysis="""
    * Improving deal acceleration rates can lead to increased sales efficiency and potentially higher revenue generation.
    * However, a focus solely on accelerating deals may impact the quality of customer interactions and long-term customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Deal", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
