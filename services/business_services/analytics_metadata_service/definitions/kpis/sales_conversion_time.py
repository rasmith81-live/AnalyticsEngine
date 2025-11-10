"""
Sales Conversion Time KPI

The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process.
"""

from analytics_models import KPI

SALES_CONVERSION_TIME = KPI(
    name="Sales Conversion Time",
    code="SALES_CONVERSION_TIME",
    category="Sales Performance",
    
    # Core Definition
    description="The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process.",
    kpi_definition="The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process.",
    expected_business_insights="Sheds light on sales process efficiency and customer decision timeframes.",
    measurement_approach="Measures the average time taken from initial contact to a completed sale.",
    
    # Formula
    formula="Average Time from Lead Generation to Closing the Sale",
    calculation_formula="Average Time from Lead Generation to Closing the Sale",
    
    # Analysis
    trend_analysis="""
    * A decreasing sales conversion time may indicate improvements in the sales process, such as better lead qualification or more effective closing techniques.
    * An increasing conversion time could signal issues in the sales process, such as longer lead nurturing times or ineffective follow-up strategies.
    """,
    diagnostic_questions="""
    * What are the average times spent in each stage of the sales process, from lead qualification to closing?
    * Are there specific points in the sales process where leads tend to get stuck or delayed?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement sales automation tools to streamline lead management and follow-up processes.
    * Provide additional training and resources for sales representatives to improve their efficiency in moving leads through the sales process.
    * Analyze and optimize the sales process to identify and eliminate bottlenecks that may be prolonging conversion times.
    """,
    visualization_suggestions="""
    * Line charts showing the average conversion time over specific time periods to identify trends.
    * Funnel charts to visualize the drop-off points in the sales process where leads may be getting delayed.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long conversion times can lead to lost opportunities and potential revenue.
    * Rapidly decreasing conversion times may indicate a focus on quantity over quality, potentially leading to customer dissatisfaction or churn.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track lead interactions and monitor sales pipeline velocity.
    * Sales analytics platforms to identify patterns and insights that can help improve the sales process.
    """,
    integration_points="""
    * Integrate sales conversion time data with marketing analytics to understand the quality of leads being generated and their impact on the sales process.
    * Link with customer feedback systems to correlate conversion times with customer satisfaction and identify areas for improvement.
    """,
    change_impact_analysis="""
    * Reducing sales conversion time can lead to increased revenue and improved sales team morale, but it may also require additional resources and investments in technology.
    * Significantly increasing sales conversion time may indicate a need for reevaluation of sales strategies and resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Lead", "Lead Qualification", "Lost Sale", "Opportunity", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
