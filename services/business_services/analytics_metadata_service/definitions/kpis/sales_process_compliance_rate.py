"""
Sales Process Compliance Rate KPI

The percentage of sales reps who are following the defined sales process as established by the sales enablement team.
"""

from analytics_models import KPI

SALES_PROCESS_COMPLIANCE_RATE = KPI(
    name="Sales Process Compliance Rate",
    code="SALES_PROCESS_COMPLIANCE_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales reps who are following the defined sales process as established by the sales enablement team.",
    kpi_definition="The percentage of sales reps who are following the defined sales process as established by the sales enablement team.",
    expected_business_insights="Identifies adherence to standardized sales procedures, which can impact the consistency and predictability of sales outcomes.",
    measurement_approach="Measures how frequently sales reps follow the predefined sales process.",
    
    # Formula
    formula="(Number of Sales Followed Process / Total Number of Sales) * 100",
    calculation_formula="(Number of Sales Followed Process / Total Number of Sales) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales process compliance rate may indicate better adoption of the defined sales process and improved sales performance.
    * A decreasing rate could signal resistance to the sales process, lack of understanding, or the need for process refinement.
    """,
    diagnostic_questions="""
    * Are there specific stages or aspects of the sales process where compliance tends to be lower?
    * How are sales reps being trained and supported to ensure understanding and adherence to the defined sales process?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide regular training and reinforcement of the sales process to ensure understanding and adoption.
    * Seek feedback from sales reps on the effectiveness of the sales process and make adjustments as needed.
    * Use sales enablement tools and technologies to automate and guide the sales process, making it easier for reps to comply.
    """,
    visualization_suggestions="""
    * Line charts showing the compliance rate over time to identify trends and patterns.
    * Comparison charts to visualize compliance rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low sales process compliance can lead to inconsistent sales performance and missed opportunities.
    * High compliance without corresponding sales results may indicate a need to revisit the effectiveness of the defined sales process.
    """,
    tracking_tools="""
    * Sales enablement platforms like Highspot or Seismic that provide guidance and support for the sales process.
    * CRM systems with built-in sales process tracking and reporting capabilities.
    """,
    integration_points="""
    * Integrate sales process compliance data with performance management systems to align individual and team goals with process adherence.
    * Link compliance metrics with customer relationship management systems to understand the impact of the sales process on customer interactions and outcomes.
    """,
    change_impact_analysis="""
    * Improving sales process compliance can lead to more predictable and consistent sales outcomes, contributing to overall business performance.
    * However, overly rigid enforcement of the sales process may stifle creativity and adaptability in sales approaches, potentially affecting customer relationships.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
