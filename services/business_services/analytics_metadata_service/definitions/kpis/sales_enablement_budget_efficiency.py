"""
Sales Enablement Budget Efficiency KPI

The efficiency of the sales enablement budget, measured by the ROI generated per dollar spent.
"""

from analytics_models import KPI

SALES_ENABLEMENT_BUDGET_EFFICIENCY = KPI(
    name="Sales Enablement Budget Efficiency",
    code="SALES_ENABLEMENT_BUDGET_EFFICIENCY",
    category="Sales Enablement",
    
    # Core Definition
    description="The efficiency of the sales enablement budget, measured by the ROI generated per dollar spent.",
    kpi_definition="The efficiency of the sales enablement budget, measured by the ROI generated per dollar spent.",
    expected_business_insights="Assesses how effectively the sales enablement budget is being utilized to generate increased sales productivity and revenue.",
    measurement_approach="Measures the return on investment for the sales enablement budget.",
    
    # Formula
    formula="(Sales Growth Attributed to Sales Enablement / Sales Enablement Budget Spent)",
    calculation_formula="(Sales Growth Attributed to Sales Enablement / Sales Enablement Budget Spent)",
    
    # Analysis
    trend_analysis="""
    * An increasing ROI per dollar spent may indicate that sales enablement initiatives are effectively driving revenue growth.
    * A decreasing ROI could signal inefficiencies in the sales enablement budget allocation or a lack of impact from the initiatives.
    """,
    diagnostic_questions="""
    * Are there specific sales enablement activities or programs that consistently deliver higher ROI?
    * How does the ROI from the sales enablement budget compare with industry benchmarks or with previous periods?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly assess the performance of sales enablement initiatives and reallocate budget to activities with higher ROI.
    * Invest in training and development programs to enhance the effectiveness of the sales team, thus improving the ROI of sales enablement efforts.
    * Utilize technology to automate repetitive tasks and streamline sales processes, maximizing the impact of the sales enablement budget.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of ROI generated per dollar spent over time.
    * Pareto charts to identify the sales enablement activities that contribute the most to ROI.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low ROI from the sales enablement budget may lead to decreased motivation and engagement among the sales team.
    * A consistently declining ROI could indicate a need for a fundamental reevaluation of sales enablement strategies and budget allocation.
    """,
    tracking_tools="""
    * Sales enablement platforms like Highspot or Seismic to track the impact of enablement activities on revenue generation.
    * CRM systems such as Salesforce or HubSpot to analyze the correlation between sales enablement efforts and actual sales performance.
    """,
    integration_points="""
    * Integrate ROI data from the sales enablement budget with financial reporting systems to provide a comprehensive view of overall business performance.
    * Link sales enablement ROI with sales performance metrics to understand the direct impact of enablement efforts on sales outcomes.
    """,
    change_impact_analysis="""
    * Improving the ROI of the sales enablement budget can lead to increased sales productivity and revenue growth.
    * Conversely, a declining ROI may result in missed sales opportunities and reduced competitiveness in the market.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
