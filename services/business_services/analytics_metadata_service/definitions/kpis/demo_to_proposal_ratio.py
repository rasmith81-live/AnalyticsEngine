"""
Demo-to-Proposal Ratio KPI

The ratio of demos conducted to the proposals generated for prospects.
"""

from analytics_models import KPI

DEMO_TO_PROPOSAL_RATIO = KPI(
    name="Demo-to-Proposal Ratio",
    code="DEMO_TO_PROPOSAL_RATIO",
    category="Outside Sales",
    
    # Core Definition
    description="The ratio of demos conducted to the proposals generated for prospects.",
    kpi_definition="The ratio of demos conducted to the proposals generated for prospects.",
    expected_business_insights="Indicates the efficiency of the sales team in moving leads from the demo stage to proposal stage in the sales funnel.",
    measurement_approach="Compares the number of product demonstrations to the number of proposals sent to prospects.",
    
    # Formula
    formula="Number of Proposals Sent / Number of Demos Conducted * 100",
    calculation_formula="Number of Proposals Sent / Number of Demos Conducted * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing demo-to-proposal ratio may indicate a more targeted approach in conducting demos, leading to higher quality prospects.
    * A decreasing ratio could signal a disconnect between the demos and the proposals, potentially pointing to issues in the sales process or product fit.
    """,
    diagnostic_questions="""
    * Are there specific sales representatives or teams with significantly higher or lower demo-to-proposal ratios?
    * What feedback have we received from prospects regarding the quality and relevance of the proposals generated?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional training and support for sales representatives to improve their demo-to-proposal conversion skills.
    * Regularly review and update the content and format of proposals to ensure they align with the needs and expectations of prospects.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of demo-to-proposal ratios over time for individual sales representatives or teams.
    * Pie charts comparing the distribution of proposals generated from different types of demos (e.g., in-person, virtual, product-specific).
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low demo-to-proposal ratio may lead to wasted resources and decreased sales efficiency.
    * High variability in the ratio across different sales representatives could indicate a lack of standardized sales processes or training.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze the conversion rates at each stage of the sales process.
    * Sales enablement platforms to provide sales representatives with the necessary tools and content to create compelling proposals.
    """,
    integration_points="""
    * Integrate demo-to-proposal ratios with lead generation systems to identify the most effective sources of leads for generating high-quality proposals.
    * Link this KPI with customer feedback and satisfaction metrics to understand the impact of proposals on overall customer experience.
    """,
    change_impact_analysis="""
    * Improving the demo-to-proposal ratio can lead to more efficient use of sales resources and potentially higher conversion rates.
    * However, a significant increase in the ratio may also indicate a more conservative approach in pursuing new prospects, potentially limiting overall sales growth.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Demo", "Product", "Product Adoption", "Product Usage", "Proposal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
