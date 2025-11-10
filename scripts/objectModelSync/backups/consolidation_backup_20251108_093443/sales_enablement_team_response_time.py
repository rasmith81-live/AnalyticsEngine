"""
Sales Enablement Team Response Time KPI

The average time taken by the Sales Enablement Team to respond to requests or inquiries from the sales team.
"""

from analytics_models import KPI

SALES_ENABLEMENT_TEAM_RESPONSE_TIME = KPI(
    name="Sales Enablement Team Response Time",
    code="SALES_ENABLEMENT_TEAM_RESPONSE_TIME",
    category="Sales Enablement",
    
    # Core Definition
    description="The average time taken by the Sales Enablement Team to respond to requests or inquiries from the sales team.",
    kpi_definition="The average time taken by the Sales Enablement Team to respond to requests or inquiries from the sales team.",
    expected_business_insights="Indicates the efficiency and effectiveness of the sales enablement team in supporting sales operations.",
    measurement_approach="Measures the average time taken by the sales enablement team to respond to queries or requests from the sales team.",
    
    # Formula
    formula="Average Time from Request to Response by Sales Enablement Team",
    calculation_formula="Average Time from Request to Response by Sales Enablement Team",
    
    # Analysis
    trend_analysis="""
    * Response time may decrease as the Sales Enablement Team becomes more efficient in handling inquiries and requests.
    * An increasing average response time could indicate a growing workload for the Sales Enablement Team or potential communication issues.
    """,
    diagnostic_questions="""
    * Are there specific types of inquiries or requests that consistently take longer to respond to?
    * How does our average response time compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement standardized processes for handling and prioritizing inquiries to improve response efficiency.
    * Provide additional training or resources to the Sales Enablement Team to help them address inquiries more effectively.
    * Utilize automation or technology solutions to streamline the response process where possible.
    """,
    visualization_suggestions="""
    * Line charts showing the average response time over different time periods to identify trends.
    * Stacked bar charts comparing response times for different types of inquiries or requests.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Long response times can lead to frustration and dissatisfaction among the sales team, impacting overall productivity and morale.
    * Consistently high response times may indicate a need for additional resources or process improvements within the Sales Enablement Team.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with ticketing or case management capabilities to track and manage inquiries.
    * Communication and collaboration tools to facilitate efficient internal communication and task assignment within the Sales Enablement Team.
    """,
    integration_points="""
    * Integrate response time tracking with sales performance metrics to understand the impact of timely responses on sales outcomes.
    * Link response time data with customer feedback systems to identify any correlations between response efficiency and customer satisfaction.
    """,
    change_impact_analysis="""
    * Improving response time can enhance the overall sales process and customer experience, potentially leading to increased sales and customer loyalty.
    * However, overly rapid responses without adequate information or support may impact the quality of the sales enablement function.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
