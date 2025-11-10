"""
Average Lead Qualification Time KPI

The average time taken to assess and qualify a new sales lead.
"""

from analytics_models import KPI

AVERAGE_LEAD_QUALIFICATION_TIME = KPI(
    name="Average Lead Qualification Time",
    code="AVERAGE_LEAD_QUALIFICATION_TIME",
    category="Outside Sales",
    
    # Core Definition
    description="The average time taken to assess and qualify a new sales lead.",
    kpi_definition="The average time taken to assess and qualify a new sales lead.",
    expected_business_insights="Helps in understanding the efficiency of the lead qualification process and can pinpoint bottlenecks that need improvement.",
    measurement_approach="Measures the average time taken to qualify a lead from initial contact.",
    
    # Formula
    formula="Total Time to Qualify Leads / Total Number of Qualified Leads",
    calculation_formula="Total Time to Qualify Leads / Total Number of Qualified Leads",
    
    # Analysis
    trend_analysis="""
    * Shortening lead qualification times may indicate improved efficiency in the sales process or better targeting of potential leads.
    * An increasing average lead qualification time could signal issues with lead quality, sales team capacity, or changes in market dynamics.
    """,
    diagnostic_questions="""
    * Are there specific criteria or benchmarks used to qualify leads, and are they still relevant and effective?
    * How does the lead qualification time vary across different sales reps or regions, and what factors contribute to these differences?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement lead scoring systems to prioritize high-quality leads and reduce time spent on low-potential prospects.
    * Provide ongoing training and support for sales reps to improve their ability to quickly assess lead potential.
    * Regularly review and update lead qualification criteria to ensure they align with changing market conditions and customer needs.
    """,
    visualization_suggestions="""
    * Line charts showing the average lead qualification time over time to identify trends and potential seasonality.
    * Comparison bar charts to visualize lead qualification times across different sales reps or territories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long lead qualification times can result in missed opportunities and decreased conversion rates.
    * Rapidly decreasing lead qualification times may indicate a drop in lead quality or insufficient attention to thorough qualification processes.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software with lead tracking and scoring capabilities to streamline lead qualification processes.
    * Sales analytics tools to identify patterns and bottlenecks in the lead qualification process.
    """,
    integration_points="""
    * Integrate lead qualification time data with sales performance metrics to understand the impact of lead quality on overall sales results.
    * Link lead qualification time with marketing campaign data to assess the effectiveness of lead generation efforts.
    """,
    change_impact_analysis="""
    * Reducing lead qualification time can lead to increased sales productivity and potentially higher revenue.
    * However, a significant decrease in lead qualification time without proper lead quality assessment may result in increased customer dissatisfaction and higher churn rates.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Lead", "Lead Qualification", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
