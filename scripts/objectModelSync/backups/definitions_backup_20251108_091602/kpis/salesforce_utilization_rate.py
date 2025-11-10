"""
Salesforce Utilization Rate KPI

The degree to which the sales team is effectively using salesforce automation tools or customer relationship management (CRM) systems.
"""

from analytics_models import KPI

SALESFORCE_UTILIZATION_RATE = KPI(
    name="Salesforce Utilization Rate",
    code="SALESFORCE_UTILIZATION_RATE",
    category="Sales Development",
    
    # Core Definition
    description="The degree to which the sales team is effectively using salesforce automation tools or customer relationship management (CRM) systems.",
    kpi_definition="The degree to which the sales team is effectively using salesforce automation tools or customer relationship management (CRM) systems.",
    expected_business_insights="Reveals how well the sales team is adopting and leveraging the CRM tool for sales activities, which can impact sales efficiency and data quality.",
    measurement_approach="Looks at the percentage of the salesforce actively using the CRM system and the depth of their usage, including data entry and engagement with CRM features.",
    
    # Formula
    formula="(Number of Active CRM Users / Total Number of Sales Team Members) * 100",
    calculation_formula="(Number of Active CRM Users / Total Number of Sales Team Members) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing Salesforce Utilization Rate may indicate better adoption of CRM tools and improved data management.
    * A decreasing rate could signal resistance to CRM implementation or lack of training on the system.
    """,
    diagnostic_questions="""
    * Are there specific features within the CRM system that are underutilized by the sales team?
    * How does our Salesforce Utilization Rate compare to industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide comprehensive training and ongoing support for sales team members to maximize CRM utilization.
    * Regularly review and update the CRM system to ensure it aligns with the evolving needs of the sales team.
    * Incentivize CRM usage through performance metrics and recognition for effective utilization.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of Salesforce Utilization Rate over time.
    * Pie charts illustrating the distribution of CRM tool usage across the sales team.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low Salesforce Utilization Rate can lead to inaccurate data, missed opportunities, and decreased productivity.
    * Resistance to CRM adoption may indicate broader issues with organizational change management or communication.
    """,
    tracking_tools="""
    * CRM platforms like Salesforce, HubSpot, or Zoho CRM for comprehensive sales and customer management.
    * Data analytics tools to track and analyze CRM usage patterns and identify areas for improvement.
    """,
    integration_points="""
    * Integrate CRM data with marketing automation systems to align sales and marketing efforts and improve lead management.
    * Link CRM with customer support systems to provide a seamless experience for customers across different touchpoints.
    """,
    change_impact_analysis="""
    * Improving Salesforce Utilization Rate can lead to better customer insights, improved sales forecasting, and more targeted marketing efforts.
    * However, pushing for higher CRM usage may require a cultural shift and change management efforts within the sales team.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product Usage", "Prospect Engagement", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
