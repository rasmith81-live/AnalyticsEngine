"""
Appointments per Period KPI

The number of appointments set by the Sales Development team per time period. 
Can be filtered by various time periods (daily, weekly, monthly, quarterly, annually).
"""

from analytics_models import KPI

APPOINTMENTS_PER_PERIOD = KPI(
    name="Appointments per Period",
    code="APPOINTMENTS_PER_PERIOD",
    category="Sales Development",
    
    # Core Definition
    description="The number of appointments set by the Sales Development team per time period, supporting multiple time period filters (daily, weekly, monthly, quarterly, annually).",
    kpi_definition="The number of appointments set by the Sales Development team per time period. This metric can be filtered by various time periods (daily, weekly, monthly, quarterly, annually) to provide flexible analysis of appointment setting effectiveness. Provides insight into how effectively the team is generating leads and engaging with potential customers.",
    expected_business_insights="Helps assess the activity level of sales reps and their effectiveness at initiating sales conversations. Reveals patterns in appointment setting across different time periods and helps identify trends, seasonality, and team productivity.",
    measurement_approach="Tracks the total number of appointments or meetings set by sales representatives within a specified time period. Can be analyzed as total appointments or normalized per rep. Supports filtering by time period, sales representative, territory, and other dimensions.",
    
    # Formula
    formula="Total Number of Appointments / Time Period. Aggregations: COUNT(appointments), AVG(appointments_per_rep), SUM(appointments)",
    calculation_formula="Base: Total Number of Appointments in Period. Per Rep: Total Appointments / Number of Reps. Rate: Appointments / Time Period",
    
    # Analysis
    trend_analysis="""
    * Appointments per period may show an increasing trend if the sales development team is effectively targeting and engaging with potential leads.
    * A decreasing trend could indicate a need for improved lead generation strategies, decline in customer interest, or seasonal variations.
    * Variability across periods may reflect campaign effectiveness, market conditions, or team capacity.
    * Day-of-week or time-of-year patterns may emerge when analyzing by shorter time periods.
    """,
    diagnostic_questions=[
        'Are there specific industries or segments that are responding more positively to our appointment setting efforts?',
        'How do our appointment numbers compare to industry benchmarks or seasonal variations?',
        'What is the distribution of appointments across sales reps (are some significantly more productive)?',
        'Are there patterns by day of week, time of month, or season?',
        'How does appointment volume correlate with lead quality and conversion rates?',
        'What is the optimal appointment volume per rep to maintain quality?'
    ],
    
    # Action & Visualization
    actionable_tips=[
        'Implement targeted outreach campaigns to specific industries or customer segments that have shown higher appointment conversion rates.',
        'Provide additional training and resources to the sales development team to improve their lead generation and appointment setting skills.',
        'Utilize customer relationship management (CRM) software to track and follow up on appointments more effectively.',
        'Analyze patterns to optimize outreach timing and frequency.',
        'Set realistic targets based on historical performance and seasonality.'
    ],
    visualization_suggestions=[
        {"type": "line_chart", "description": "Track appointment trends over time (daily, weekly, monthly, quarterly) to identify patterns and seasonality."},
        {"type": "bar_chart", "description": "Compare appointment numbers across different sales development team members or territories."},
        {"type": "heatmap", "description": "Show appointment patterns by day of week and time of day."},
        {"type": "histogram", "description": "Display distribution of appointments per rep to identify outliers."},
        {"type": "area_chart", "description": "Show cumulative appointments over time with period comparisons."}
    ],
    
    # Risk & Integration
    risk_warnings=[
        'A consistently low number of appointments per period may lead to missed sales opportunities and revenue loss.',
        'An excessively high number of appointments without corresponding sales conversions could indicate a need for better lead qualification processes.',
        'High variance in appointments across reps may indicate training needs or territory imbalances.',
        'Focusing solely on appointment quantity without considering quality can lead to inefficiencies and wasted resources.'
    ],
    tracking_tools=[
        'CRM systems like Salesforce or HubSpot for tracking and managing appointment setting activities.',
        'Sales engagement platforms such as Outreach or SalesLoft to streamline outreach and follow-up processes.',
        'Business intelligence tools for analyzing appointment trends across multiple time periods.',
        'Calendar and scheduling tools integrated with CRM for accurate appointment tracking.'
    ],
    integration_points=[
        'Integrate appointment setting data with sales performance metrics to analyze the effectiveness of appointments in driving actual sales.',
        'Link appointment data with marketing campaign results to understand the impact of marketing efforts on appointment generation.',
        'Connect with lead scoring systems to correlate appointment volume with lead quality.',
        'Integrate with forecasting models to predict pipeline based on appointment trends.'
    ],
    change_impact_analysis="""
    * Improving appointment numbers can lead to increased sales opportunities and revenue growth.
    * However, a focus solely on increasing appointments without considering their quality can lead to inefficiencies and wasted resources.
    * Changes in appointment patterns may indicate shifts in market dynamics, campaign effectiveness, or team productivity.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
        "aggregation_methods": ["count", "sum", "average_per_rep"],
        "dimensions": ["sales_rep", "territory", "lead_source", "industry", "campaign"],
        "replaces": ["APPOINTMENTS_PER_MONTH"],
        "required_objects": ["Appointment", "Competitive Analysis", "Deal", "Knowledge Base", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket", "Territory Assignment"]
    }
)
