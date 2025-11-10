"""
Outbound Call Conversion Rate KPI

The percentage of outbound calls that result in a desired action, such as a meeting or sale.
"""

from analytics_models import KPI

OUTBOUND_CALL_CONVERSION_RATE = KPI(
    name="Outbound Call Conversion Rate",
    code="OUTBOUND_CALL_CONVERSION_RATE",
    category="Inside Sales",
    
    # Core Definition
    description="The percentage of outbound calls that result in a desired action, such as a meeting or sale.",
    kpi_definition="The percentage of outbound calls that result in a desired action, such as a meeting or sale.",
    expected_business_insights="Measures the effectiveness of outbound calling as a sales tactic.",
    measurement_approach="The percentage of outbound calls that result in a successful sale.",
    
    # Formula
    formula="(Number of Successful Sales / Number of Outbound Calls) * 100",
    calculation_formula="(Number of Successful Sales / Number of Outbound Calls) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing outbound call conversion rate may indicate improved sales pitch effectiveness or better lead quality.
    * A decreasing rate could signal issues with the sales process, such as ineffective follow-up or poor targeting of prospects.
    """,
    diagnostic_questions="""
    * Are there specific market segments or customer profiles that have a higher conversion rate?
    * How does our outbound call conversion rate compare with industry benchmarks or historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training to improve communication and persuasion skills.
    * Refine lead qualification criteria to ensure better targeting of potential customers.
    * Implement a structured follow-up process to increase the likelihood of conversion.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of outbound call conversion rates over time.
    * Pie charts to compare conversion rates across different sales teams or territories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low conversion rate can lead to wasted resources and decreased morale among sales teams.
    * A high conversion rate without corresponding sales growth may indicate a need for better lead quality assessment.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze call outcomes.
    * Sales enablement tools to provide sales teams with the necessary resources and content for effective calls.
    """,
    integration_points="""
    * Integrate outbound call conversion data with lead generation systems to identify the most promising leads.
    * Link conversion rate analysis with customer relationship management systems to track the entire sales process from call to close.
    """,
    change_impact_analysis="""
    * Improving the outbound call conversion rate can lead to increased sales revenue and customer acquisition.
    * However, a focus solely on increasing conversion rates may lead to overlooking the quality of customer interactions and long-term customer satisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Lead", "Lost Sale", "Meeting", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
